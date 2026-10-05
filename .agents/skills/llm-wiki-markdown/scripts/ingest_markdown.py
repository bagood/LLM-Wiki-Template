# /// script
# requires-python = ">=3.12"
# dependencies = ["PyYAML==6.0.3"]
# ///
"""Snapshot Markdown, recover unfinished work, acknowledge pages, finish a run.

This helper never writes knowledge prose. All paths in the manifest are portable.
Run with --help for the three mutually exclusive operations.
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
import tempfile
from pathlib import Path
from urllib.parse import unquote, urlsplit

from common import (ContractError, atomic_write, content_pages, destinations, digest,
                    load_manifest, read_page, utc_now, validate, without_code, write_json)

EXCLUDED = {".git", ".hg", ".svn", ".agents", ".claude", ".venv", "node_modules", "assets", "attachments", "__pycache__"}


def slug(text):
    value = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return value[:40].rstrip("-") or "source"


def source_id(corpus, relative):
    return f"{slug(Path(relative).stem)}-{digest((corpus + chr(0) + relative).encode())[:16]}"


def discover(inputs, root, workspace):
    found, errors = set(), []
    for value in inputs:
        given = Path(value).absolute()
        if given.is_symlink():
            errors.append({"input": str(given), "error": "symlink inputs are excluded"})
            continue
        path = given.resolve()
        if not path.exists() or not path.is_relative_to(root):
            errors.append({"input": str(path), "error": "missing or outside input root"})
            continue
        if path.is_file() and path.suffix.lower() != ".md":
            errors.append({"input": str(path), "error": "only Markdown (.md) source files are accepted"})
            continue
        candidates = path.rglob("*") if path.is_dir() else [path]
        for file in candidates:
            if not file.is_file() or file.suffix.lower() != ".md":
                continue
            rel = file.relative_to(root)
            if file.is_relative_to(workspace) or any(part in EXCLUDED for part in rel.parts[:-1]):
                continue
            if any((root / Path(*rel.parts[:i])).is_symlink() for i in range(1, len(rel.parts) + 1)):
                continue
            found.add(file)
    return sorted(found), errors


def attachment_paths(text, file, root):
    links = destinations(text)[0]
    links += re.findall(r"!\[\[([^\]|]+)(?:\|[^\]]*)?\]\]", without_code(text))
    result, warnings = set(), []
    for link in links:
        parsed = urlsplit(link)
        if parsed.scheme or parsed.netloc or not parsed.path:
            continue
        if parsed.path.startswith("/"):
            warnings.append(f"absolute local resource not copied: {link}")
            continue
        local = file.parent / unquote(parsed.path)
        target = local.resolve()
        if target.suffix.lower() == ".md":
            continue  # note links are knowledge relationships, not attachment sources
        if not target.is_relative_to(root) or local.is_symlink():
            warnings.append(f"attachment outside input boundary or symlink: {link}")
        elif not target.is_file():
            warnings.append(f"missing attachment: {link}")
        else:
            result.add(target)
    return sorted(result), warnings


def page_valid(workspace, record):
    path = workspace / record["page"]
    if not path.is_file():
        return False
    return validate(workspace, only=path, check_indexes=False)["valid"]


def manual_changes(workspace, manifest):
    return [path for path, expected in manifest.get("page_hashes", {}).items()
            if (workspace / path).is_file() and digest((workspace / path).read_bytes()) != expected]


def ingest(workspace, inputs, corpus, input_root=None):
    workspace = Path(workspace).resolve()
    if not corpus.strip():
        raise ContractError("corpus key cannot be empty")
    if input_root:
        root = Path(input_root).resolve()
    elif len(inputs) == 1:
        path = Path(inputs[0]).resolve()
        root = path if path.is_dir() else path.parent
    else:
        raise ContractError("multiple inputs require --input-root for stable relative identities")
    if root == workspace or root.is_relative_to(workspace):
        raise ContractError("input root must be outside output workspace")
    files, errors = discover(inputs, root, workspace)
    if (workspace / "manifest.json").exists():
        manifest = load_manifest(workspace)
    else:
        if workspace.exists() and any(workspace.iterdir()):
            raise ContractError("output is nonempty and has no manifest; choose an empty output")
        workspace.mkdir(parents=True, exist_ok=True)
        for folder in ("raw", "wiki/sources", "wiki/entities", "wiki/concepts"):
            (workspace / folder).mkdir(parents=True, exist_ok=True)
        atomic_write(workspace / "wiki/log.md", "# Wiki update log\n")
        manifest = {"schema_version": 1, "okf_version": "0.2", "threshold": 2,
                    "sources": {}, "identities": {}, "pending_tail": False, "page_hashes": {}}
    report = {"workspace": str(workspace), "new": [], "skipped": [], "aliases": [],
              "changed": [], "errors": errors, "pending": [], "blocked": [], "manual_changes": manual_changes(workspace, manifest)}
    hashes = {r["sha256"]: sid for sid, r in manifest["sources"].items()}
    for file in files:
        rel = file.relative_to(root).as_posix()
        identity = corpus + ":" + rel
        # JSON tuple encoding prevents ambiguous corpus/path delimiter combinations.
        key = json.dumps([corpus, rel], ensure_ascii=False)
        try:
            data = file.read_bytes()
            text = data.decode("utf-8")
        except (OSError, UnicodeError) as exc:
            report["errors"].append({"input": rel, "error": str(exc)})
            continue
        sha = digest(data)
        existing = manifest["identities"].get(key)
        if existing:
            record = manifest["sources"][existing]
            if sha != record["sha256"]:
                report["changed"].append({"input": identity, "source_id": existing, "policy": "retained previous snapshot"})
            else:
                report["skipped"].append({"input": identity, "source_id": existing})
            continue
        if sha in hashes:
            sid = hashes[sha]
            manifest["identities"][key] = sid
            manifest["sources"][sid]["aliases"].append({"corpus": corpus, "relative_path": rel})
            report["aliases"].append({"input": identity, "source_id": sid})
            continue
        sid = source_id(corpus, rel)
        if sid in manifest["sources"]:
            raise ContractError(f"source ID collision: {sid}")
        attachments, warnings = attachment_paths(text, file, root)
        asset_data = {p: p.read_bytes() for p in attachments}
        raw_file = f"raw/{sid}/{rel}"
        assets = [{"path": f"raw/{sid}/{p.relative_to(root).as_posix()}", "sha256": digest(asset_data[p])} for p in attachments]
        destination = workspace / "raw" / sid
        if destination.exists():
            # A process may die after the raw rename but before the manifest write.
            expected = {raw_file: sha, **{x["path"]: x["sha256"] for x in assets}}
            actual = {p.relative_to(workspace).as_posix(): digest(p.read_bytes()) for p in destination.rglob("*") if p.is_file()}
            if actual != expected:
                raise ContractError(f"unregistered raw snapshot differs: {sid}; inspect before recovery")
        else:
            staging = Path(tempfile.mkdtemp(prefix=".snapshot-", dir=workspace / "raw"))
            try:
                target = staging / rel
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(data)
                for attachment in attachments:
                    target = staging / attachment.relative_to(root)
                    target.parent.mkdir(parents=True, exist_ok=True)
                    target.write_bytes(asset_data[attachment])
                staging.rename(destination)
            finally:
                if staging.exists():
                    shutil.rmtree(staging)
        record = {"source_id": sid, "corpus": corpus, "relative_path": rel,
                  "raw_file": raw_file, "sha256": sha, "total_lines": len(text.splitlines()),
                  "page": f"wiki/sources/{sid}.md", "assets": assets, "warnings": warnings,
                  "aliases": [], "created": utc_now(), "page_complete": False}
        manifest["sources"][sid] = record
        manifest["identities"][key] = sid
        hashes[sha] = sid
        manifest["pending_tail"] = True
        write_json(workspace / "manifest.json", manifest)
        report["new"].append(record)
    # Inspect every accepted source, including ones not supplied in this invocation.
    for sid, record in manifest["sources"].items():
        evidence = [{"path": record["raw_file"], "sha256": record["sha256"]}] + record["assets"]
        damaged = [item["path"] for item in evidence if not (workspace / item["path"]).is_file() or digest((workspace / item["path"]).read_bytes()) != item["sha256"]]
        if damaged:
            report["errors"].append({"source_id": sid, "error": "immutable evidence missing or changed", "paths": damaged})
            report["blocked"].append(sid)
            record["page_complete"] = False
            manifest["pending_tail"] = True
            continue
        if not record["page_complete"] or not page_valid(workspace, record):
            record["page_complete"] = False
            report["pending"].append(record)
            manifest["pending_tail"] = True
    if manifest["page_hashes"]:
        missing = [path for path in manifest["page_hashes"] if not (workspace / path).exists()]
        if missing:
            manifest["pending_tail"] = True
            report["missing_pages"] = missing
    write_json(workspace / "manifest.json", manifest)
    report["pending_tail"] = manifest["pending_tail"]
    return report


def complete(workspace, sid, receipt):
    workspace = Path(workspace).resolve()
    manifest = load_manifest(workspace)
    record = manifest["sources"].get(sid)
    if not record:
        raise ContractError("unknown source_id")
    report = validate(workspace, only=workspace / record["page"], check_indexes=False)
    if not report["valid"]:
        raise ContractError(json.dumps(report))
    fm, _ = read_page(workspace / record["page"])
    refs = {"entities": fm.get("entities", []), "concepts": fm.get("concepts", [])}
    expected = {"source_id": sid, "page": record["page"], "coverage": fm["coverage"], **refs}
    if receipt != expected:
        raise ContractError("receipt must exactly match source_id, page, coverage, entities, concepts")
    record["page_complete"] = True
    record["page_sha256"] = digest((workspace / record["page"]).read_bytes())
    manifest["pending_tail"] = True
    write_json(workspace / "manifest.json", manifest)
    return {"completed": sid, "pending_tail": True}


def finish(workspace):
    workspace = Path(workspace).resolve()
    manifest = load_manifest(workspace)
    if any(not r["page_complete"] for r in manifest["sources"].values()):
        raise ContractError("acknowledge all source pages before finishing")
    report = validate(workspace)
    if not report["valid"]:
        raise ContractError(json.dumps(report))
    for name in ("wiki/overview.md", "wiki/index.md", "wiki/log.md"):
        if not (workspace / name).is_file():
            raise ContractError(f"required template navigation missing: {name}")
    # Check current navigation against a freshly rendered cache, without mutation.
    from build_index_md import render_indexes
    for path, text in render_indexes(workspace / "wiki").items():
        if not path.is_file() or path.read_text(encoding="utf-8") != text:
            raise ContractError(f"index is stale or missing: {path}")
    if not manifest["pending_tail"]:
        return {"finished": True, "action": "unchanged"}
    for record in manifest["sources"].values():
        if digest((workspace / record["page"]).read_bytes()) != record["page_sha256"]:
            raise ContractError(f"source page changed after acknowledgment: {record['page']}")
    page_hashes = {p.relative_to(workspace).as_posix(): digest(p.read_bytes()) for p in content_pages(workspace / "wiki")}
    run_id = digest(json.dumps(page_hashes, sort_keys=True).encode())[:16]
    today = utc_now()[:10]
    log = workspace / "wiki/log.md"
    text = log.read_text(encoding="utf-8")
    marker = f"<!-- completed-run:{run_id} -->"
    if marker not in text:
        entry = f"## {today}\n\n- **Update**: Completed ingestion; {len(manifest['sources'])} distinct sources, {len(page_hashes)} knowledge pages. {marker}\n\n"
        head, _, rest = text.partition("\n")
        atomic_write(log, head + "\n\n" + entry + rest.lstrip())
    manifest["pending_tail"] = False
    manifest["page_hashes"] = page_hashes
    manifest["last_completed_run"] = run_id
    write_json(workspace / "manifest.json", manifest)
    return {"finished": True, "run_id": run_id, "validation": report}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--wiki-dir", required=True, help="Workspace holding raw/, wiki/, manifest.json")
    parser.add_argument("--corpus", help="Stable key for this collection, e.g. research-notes")
    parser.add_argument("--input-root", help="Stable root for relative identities; required for multiple inputs")
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--inputs", nargs="+", help="Markdown files or directories")
    mode.add_argument("--complete", metavar="SOURCE_ID", help="Validate and acknowledge a written source page")
    mode.add_argument("--finish", action="store_true", help="Validate aggregation, record log, mark run complete")
    parser.add_argument("--receipt", help="JSON receipt file required with --complete")
    args = parser.parse_args()
    try:
        if args.inputs:
            if not args.corpus:
                parser.error("--inputs requires --corpus")
            result = ingest(args.wiki_dir, args.inputs, args.corpus, args.input_root)
            failed = bool(result["errors"])
        elif args.complete:
            if not args.receipt:
                parser.error("--complete requires --receipt")
            result = complete(args.wiki_dir, args.complete, json.loads(Path(args.receipt).read_text(encoding="utf-8")))
            failed = False
        else:
            result, failed = finish(args.wiki_dir), False
        print(json.dumps(result, indent=2, ensure_ascii=False, default=str))
        return 1 if failed else 0
    except (ContractError, OSError, ValueError) as exc:
        print(json.dumps({"error": str(exc)}), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
