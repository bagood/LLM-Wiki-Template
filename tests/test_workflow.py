"""Behavioral tests for evidence identity, completion, recovery and portability.

Run from the template root:
uv run --python 3.12 --with PyYAML==6.0.3 python -m unittest discover -s tests -v
"""
from __future__ import annotations

import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path
from urllib.parse import quote

SCRIPTS = Path(__file__).resolve().parents[1] / ".agents/skills/llm-wiki-markdown/scripts"
sys.path.insert(0, str(SCRIPTS))
import yaml
from common import ContractError, collect_mentions, digest, load_manifest, read_page, validate
from ingest_markdown import complete, finish, ingest
from build_index_md import build


def write_page(path, metadata, body):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("---\n" + yaml.safe_dump(metadata, sort_keys=False, allow_unicode=True) + "---\n\n" + body, encoding="utf-8")


def basic(kind, title):
    return {"type": kind, "title": title, "description": f"Evidence about {title}.",
            "created": "2026-10-05T00:00:00Z", "generated": {"by": "process:test-fixture", "at": "2026-10-05T00:00:00Z"}}


def source_page(workspace, record, concepts=None, entities=None):
    sid = record["source_id"]
    fm = {**basic("source", sid), "source_id": sid, "raw_file": record["raw_file"],
          "content_sha256": record["sha256"], "coverage": {"complete": True, "total_lines": record["total_lines"],
          "ranges": [[1, record["total_lines"]]] if record["total_lines"] else []},
          "entities": entities or [], "concepts": concepts or [], "limitations": record["warnings"],
          "sources": [{"id": sid, "resource": "../../" + quote(record["raw_file"], safe="/")}]}
    body = f"# {sid}\n\n<!-- BEGIN GENERATED -->\nA test claim.[^{sid}]\n\n[^{sid}]: [Raw]({fm['sources'][0]['resource']})\n<!-- END GENERATED -->\n\n## Human notes\n"
    write_page(workspace / record["page"], fm, body)
    return {"source_id": sid, "page": record["page"], "coverage": fm["coverage"], "entities": fm["entities"], "concepts": fm["concepts"]}


def aggregate(workspace):
    counts = collect_mentions(workspace)
    for kind, page_type in (("concepts", "concept"), ("entities", "entity")):
        for ref, record in counts[kind].items():
            if not record["qualifies"]:
                continue
            fm = {**basic(page_type, Path(ref).stem), "source_count": record["count"],
                  "sources": [{"id": sid, "resource": "../sources/" + sid + ".md"} for sid in record["source_ids"]]}
            body = "# Topic\n\nClaim." + "".join(f"[^{sid}]" for sid in record["source_ids"]) + "\n\n"
            body += "\n".join(f"[^{sid}]: [Source](../sources/{sid}.md)" for sid in record["source_ids"])
            write_page(workspace / "wiki" / ref, fm, body)
    write_page(workspace / "wiki/overview.md", basic("overview", "Overview"), "# Overview\n\n[Sources](sources/index.md)\n")
    build(workspace)


class WorkflowTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.base = Path(self.tmp.name)
        self.inputs = self.base / "notes"
        self.inputs.mkdir()
        self.wiki = self.base / "wiki-test"

    def tearDown(self):
        self.tmp.cleanup()

    def note(self, name, text):
        path = self.inputs / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return path

    def snapshot(self):
        return ingest(self.wiki, [self.inputs], "test-notes")

    def acknowledge(self, record, concepts=None, entities=None):
        receipt = source_page(self.wiki, record, concepts, entities)
        complete(self.wiki, record["source_id"], receipt)

    def test_snapshots_exact_and_same_stems_coexist(self):
        a = self.note("a/same.md", "# A\nFirst source.\n")
        b = self.note("b/same.md", "# B\nSecond source.\n")
        report = self.snapshot()
        self.assertEqual(len(report["new"]), 2)
        self.assertEqual(len({x["source_id"] for x in report["new"]}), 2)
        for record, path in zip(report["new"], [a, b]):
            self.assertEqual((self.wiki / record["raw_file"]).read_bytes(), path.read_bytes())

    def test_duplicates_alias_without_second_vote(self):
        self.note("a.md", "# Same\nOne claim.\n")
        self.note("nested/b.md", "# Same\nOne claim.\n")
        report = self.snapshot()
        self.assertEqual((len(report["new"]), len(report["aliases"])), (1, 1))
        self.acknowledge(report["new"][0], ["concepts/memory.md"])
        record = collect_mentions(self.wiki)["concepts"]["concepts/memory.md"]
        self.assertEqual(record["count"], 1)
        self.assertFalse(record["qualifies"])

    def test_threshold_counts_once_per_source(self):
        self.note("a.md", "# A\nFirst.\n")
        self.note("b.md", "# B\nSecond.\n")
        for record in self.snapshot()["new"]:
            self.acknowledge(record, ["concepts/memory.md", "concepts/memory.md"])
        counts = collect_mentions(self.wiki)["concepts"]["concepts/memory.md"]
        self.assertEqual(counts["count"], 2)
        self.assertTrue(counts["qualifies"])
        aggregate(self.wiki)
        self.assertTrue(validate(self.wiki)["valid"])

    def test_changed_input_keeps_previous_snapshot(self):
        file = self.note("a.md", "Original\n")
        record = self.snapshot()["new"][0]
        file.write_text("Changed\n")
        report = self.snapshot()
        self.assertEqual(len(report["changed"]), 1)
        self.assertEqual((self.wiki / record["raw_file"]).read_text(), "Original\n")

    def test_recovery_snapshot_and_unacknowledged_page(self):
        self.note("a.md", "# A\nClaim.\n")
        record = self.snapshot()["new"][0]
        self.assertEqual(len(self.snapshot()["pending"]), 1)
        receipt = source_page(self.wiki, record)
        original = (self.wiki / record["page"]).read_bytes()
        self.assertEqual(len(self.snapshot()["pending"]), 1)
        complete(self.wiki, record["source_id"], receipt)
        self.assertEqual((self.wiki / record["page"]).read_bytes(), original)
        self.assertEqual(self.snapshot()["pending"], [])
        self.assertTrue(self.snapshot()["pending_tail"])

    def test_tail_recovery_and_unchanged_run(self):
        self.note("a.md", "# A\nClaim.\n")
        self.acknowledge(self.snapshot()["new"][0])
        self.assertTrue(self.snapshot()["pending_tail"])
        aggregate(self.wiki)
        finish(self.wiki)
        before = {p.relative_to(self.wiki): p.read_bytes() for p in self.wiki.rglob("*") if p.is_file()}
        report = self.snapshot()
        self.assertFalse(report["pending_tail"])
        self.assertEqual(finish(self.wiki)["action"], "unchanged")
        after = {p.relative_to(self.wiki): p.read_bytes() for p in self.wiki.rglob("*") if p.is_file()}
        self.assertEqual(before, after)

    def test_incomplete_long_source_is_not_acknowledged(self):
        self.note("long.md", "# Long\n" + "ordinary line\n" * 2100 + "DECISIVE FINAL CLAIM\n")
        record = self.snapshot()["new"][0]
        receipt = source_page(self.wiki, record)
        fm, body = read_page(self.wiki / record["page"])
        fm["coverage"]["ranges"] = [[1, 2000]]
        write_page(self.wiki / record["page"], fm, body)
        with self.assertRaises(ContractError):
            complete(self.wiki, record["source_id"], receipt)
        self.assertFalse(load_manifest(self.wiki)["sources"][record["source_id"]]["page_complete"])

    def test_invalid_yaml_preserves_indexes_and_counter_fails(self):
        self.note("a.md", "# A\nClaim.\n")
        record = self.snapshot()["new"][0]
        self.acknowledge(record)
        aggregate(self.wiki)
        index = (self.wiki / "wiki/index.md").read_bytes()
        (self.wiki / record["page"]).write_text("---\ntype: [oops\n---\n")
        with self.assertRaises(ContractError):
            build(self.wiki)
        with self.assertRaises(ContractError):
            collect_mentions(self.wiki)
        self.assertEqual((self.wiki / "wiki/index.md").read_bytes(), index)

    def test_duplicate_yaml_keys_are_errors(self):
        self.note("a.md", "# A\n")
        record = self.snapshot()["new"][0]
        (self.wiki / record["page"]).write_text("---\ntype: source\ntype: concept\n---\n")
        self.assertFalse(validate(self.wiki)["valid"])

    def test_indexes_rebuild_byte_identically(self):
        self.note("a.md", "# A\nClaim.\n")
        self.acknowledge(self.snapshot()["new"][0])
        aggregate(self.wiki)
        before = {p.relative_to(self.wiki): p.read_bytes() for p in self.wiki.rglob("index.md")}
        for p in self.wiki.rglob("index.md"):
            p.unlink()
        build(self.wiki)
        self.assertEqual(before, {p.relative_to(self.wiki): p.read_bytes() for p in self.wiki.rglob("index.md")})

    def test_missing_citation_is_error_candidates_are_warnings(self):
        self.note("a.md", "# A\nClaim.\n")
        record = self.snapshot()["new"][0]
        self.acknowledge(record, ["concepts/future.md"])
        aggregate(self.wiki)
        report = validate(self.wiki)
        self.assertTrue(report["valid"])
        self.assertTrue(any("candidate" in x for x in report["warnings"]))
        page = self.wiki / record["page"]
        page.write_text(page.read_text() + "\nBroken claim.[^absent]\n")
        self.assertFalse(validate(self.wiki)["valid"])

    def test_attachments_and_missing_attachment(self):
        asset = self.inputs / "assets/diagram.png"
        asset.parent.mkdir()
        asset.write_bytes(b"example-image")
        self.note("nested/a.md", "# A\n![Image](../assets/diagram.png)\n![Missing](../assets/missing.png)\n")
        record = self.snapshot()["new"][0]
        self.assertEqual(len(record["assets"]), 1)
        self.assertTrue(record["warnings"])
        self.assertEqual((self.wiki / record["assets"][0]["path"]).read_bytes(), b"example-image")
        self.acknowledge(record)
        asset_copy = self.wiki / record["assets"][0]["path"]
        asset_copy.write_bytes(b"changed")
        self.assertFalse(validate(self.wiki)["valid"])

    def test_symlink_and_output_exclusion(self):
        self.note("a.md", "# A\n")
        outside = self.base / "outside.md"
        outside.write_text("outside")
        (self.inputs / "linked.md").symlink_to(outside)
        self.wiki = self.inputs / "wiki-output"
        first = self.snapshot()
        self.assertEqual(len(first["new"]), 1)
        self.acknowledge(first["new"][0])
        aggregate(self.wiki)
        self.assertEqual(len(self.snapshot()["new"]), 0)

    def test_utf8_unicode_and_empty_file(self):
        self.note("研究 (記憶).md", "# 研究\nClaim.\n")
        self.note("empty.md", "")
        (self.inputs / "bad.md").write_bytes(b"\xff\xfe")
        report = self.snapshot()
        self.assertEqual((len(report["new"]), len(report["errors"])), (2, 1))
        for record in report["new"]:
            self.acknowledge(record)
        aggregate(self.wiki)
        self.assertTrue(validate(self.wiki)["valid"])

    def test_portable_after_copy_and_source_root_move(self):
        self.note("a.md", "# A\nClaim.\n")
        self.acknowledge(self.snapshot()["new"][0])
        aggregate(self.wiki)
        finish(self.wiki)
        copied = self.base / "another-location/wiki"
        shutil.copytree(self.wiki, copied)
        self.assertTrue(validate(copied)["valid"])
        moved = self.base / "moved-notes"
        self.inputs.rename(moved)
        report = ingest(copied, [moved], "test-notes")
        self.assertEqual((len(report["new"]), len(report["skipped"])), (0, 1))

    def test_bundle_scope_tolerates_unknown_optional_fields(self):
        bundle = self.base / "bundle"
        write_page(bundle / "custom.md", {"type": "Unknown producer type", "custom": [1, 2]}, "# Custom\n[Future](missing.md)\n")
        self.assertTrue(validate(bundle, "bundle")["valid"])
        self.assertFalse(validate(bundle, "workspace")["valid"])

    def test_handwritten_index_is_protected(self):
        self.note("a.md", "# A\nClaim.\n")
        self.acknowledge(self.snapshot()["new"][0])
        aggregate(self.wiki)
        index = self.wiki / "wiki/index.md"
        index.write_text("# My index\n")
        with self.assertRaises(ContractError):
            build(self.wiki)
        self.assertEqual(index.read_text(), "# My index\n")

    def test_raw_tamper_and_receipt_mismatch(self):
        self.note("a.md", "# A\nClaim.\n")
        record = self.snapshot()["new"][0]
        receipt = source_page(self.wiki, record)
        with self.assertRaises(ContractError):
            complete(self.wiki, record["source_id"], {**receipt, "concepts": ["concepts/fake.md"]})
        (self.wiki / record["raw_file"]).write_text("mutated")
        with self.assertRaises(ContractError):
            complete(self.wiki, record["source_id"], receipt)

    def test_manual_changes_reported(self):
        self.note("a.md", "# A\nClaim.\n")
        record = self.snapshot()["new"][0]
        self.acknowledge(record)
        aggregate(self.wiki)
        finish(self.wiki)
        page = self.wiki / record["page"]
        page.write_text(page.read_text() + "\nA human note.\n")
        self.assertIn(record["page"], self.snapshot()["manual_changes"])

    def test_missing_qualifying_page_prevents_finish(self):
        self.note("a.md", "# A\n")
        self.note("b.md", "# B\n")
        for record in self.snapshot()["new"]:
            self.acknowledge(record, ["concepts/memory.md"])
        with self.assertRaises(ContractError):
            finish(self.wiki)
        self.assertTrue(load_manifest(self.wiki)["pending_tail"])

    def test_provenance_id_cannot_point_to_another_source(self):
        self.note("a.md", "# A\n")
        self.note("b.md", "# B\n")
        for record in self.snapshot()["new"]:
            self.acknowledge(record, ["concepts/memory.md"])
        aggregate(self.wiki)
        path = self.wiki / "wiki/concepts/memory.md"
        fm, body = read_page(path)
        fm["sources"][0]["resource"] = fm["sources"][1]["resource"]
        write_page(path, fm, body)
        report = validate(self.wiki)
        self.assertFalse(report["valid"])
        self.assertTrue(any("wrong source page" in x for x in report["evidence_errors"]))

    def test_heading_anchor_and_code_links(self):
        self.note("a.md", "# Topic `Memory`\nClaim.\n")
        record = self.snapshot()["new"][0]
        receipt = source_page(self.wiki, record)
        path = self.wiki / record["page"]
        text = path.read_text()
        text += '\n[Location](../../' + record["raw_file"] + '#topic-memory)\n\n```md\n[Example only](missing.md)\n```\n'
        path.write_text(text)
        complete(self.wiki, record["source_id"], receipt)
        self.assertTrue(validate(self.wiki, only=path)["valid"])

    def test_incremental_tail_updates_qualifying_evidence(self):
        self.note("a.md", "# A\n")
        record = self.snapshot()["new"][0]
        self.acknowledge(record, ["concepts/memory.md"])
        aggregate(self.wiki)
        finish(self.wiki)
        before = (self.wiki / record["page"]).read_bytes()
        self.note("b.md", "# B\n")
        second = self.snapshot()
        self.acknowledge(second["new"][0], ["concepts/memory.md"])
        self.assertFalse(validate(self.wiki)["valid"])
        aggregate(self.wiki)
        finish(self.wiki)
        self.assertEqual((self.wiki / record["page"]).read_bytes(), before)
        fm, _ = read_page(self.wiki / "wiki/concepts/memory.md")
        self.assertEqual(fm["source_count"], 2)

    def test_missing_generated_page_marks_tail_pending(self):
        self.note("a.md", "# A\n")
        self.acknowledge(self.snapshot()["new"][0])
        aggregate(self.wiki)
        finish(self.wiki)
        (self.wiki / "wiki/overview.md").unlink()
        self.assertTrue(self.snapshot()["pending_tail"])

    def test_reserved_source_filename_does_not_enter_bundle_reserved_names(self):
        self.note("index.md", "# Input navigation\nSubstantive source knowledge.\n")
        record = self.snapshot()["new"][0]
        self.assertNotEqual(Path(record["page"]).name, "index.md")
        self.acknowledge(record)
        aggregate(self.wiki)
        self.assertTrue(validate(self.wiki)["valid"])

    def test_input_root_stable_when_ingesting_subset(self):
        a = self.note("nested/a.md", "# A\n")
        record = self.snapshot()["new"][0]
        report = ingest(self.wiki, [a], "test-notes", self.inputs)
        self.assertEqual(len(report["new"]), 0)
        self.assertEqual(report["skipped"][0]["source_id"], record["source_id"])

    def test_manifest_path_traversal_is_rejected(self):
        self.note("a.md", "# A\n")
        record = self.snapshot()["new"][0]
        manifest = load_manifest(self.wiki)
        manifest["sources"][record["source_id"]]["raw_file"] = "../outside.md"
        (self.wiki / "manifest.json").write_text(json.dumps(manifest))
        with self.assertRaises(ContractError):
            load_manifest(self.wiki)

    def test_cli_runs_from_unrelated_working_directory(self):
        import subprocess
        self.note("a.md", "# A\n")
        process = subprocess.run([sys.executable, str(SCRIPTS / "ingest_markdown.py"),
                                  "--wiki-dir", str(self.wiki), "--corpus", "test-notes",
                                  "--inputs", str(self.inputs)], cwd=self.base, capture_output=True, text=True)
        self.assertEqual(process.returncode, 0, process.stderr)
        self.assertEqual(len(json.loads(process.stdout)["new"]), 1)

    def test_validation_is_read_only(self):
        self.note("a.md", "# A\n")
        self.acknowledge(self.snapshot()["new"][0])
        aggregate(self.wiki)
        finish(self.wiki)
        before = {p.relative_to(self.wiki): digest(p.read_bytes()) for p in self.wiki.rglob("*") if p.is_file()}
        self.assertTrue(validate(self.wiki)["valid"])
        self.assertTrue(validate(self.wiki / "wiki", "bundle")["valid"])
        after = {p.relative_to(self.wiki): digest(p.read_bytes()) for p in self.wiki.rglob("*") if p.is_file()}
        self.assertEqual(before, after)

    def test_discovery_blocks_tampered_accepted_evidence(self):
        self.note("a.md", "# A\n")
        record = self.snapshot()["new"][0]
        (self.wiki / record["raw_file"]).write_text("tampered")
        report = self.snapshot()
        self.assertEqual(report["blocked"], [record["source_id"]])
        self.assertEqual(report["pending"], [])
        self.assertTrue(report["errors"])


if __name__ == "__main__":
    unittest.main()
