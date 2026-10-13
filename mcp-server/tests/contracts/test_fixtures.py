import hashlib
import json
import subprocess
import sys
from pathlib import Path

import pytest
import yaml
from markdown_it import MarkdownIt

ROOT = Path(__file__).resolve().parents[2]
FIXTURES = ROOT / "tests/fixtures"


class UniqueSafeLoader(yaml.SafeLoader):
    """Fixture qualification only; the production OKF adapter is a P1 deliverable."""


def unique_mapping(loader: UniqueSafeLoader, node: yaml.MappingNode) -> dict:
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node)
        if key in result:
            raise yaml.constructor.ConstructorError(
                None, None, "duplicate key", key_node.start_mark
            )
        result[key] = loader.construct_object(value_node)
    return result


UniqueSafeLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


def metadata(path: Path) -> dict:
    text = path.read_text()
    if not text.startswith("---\n"):
        return {}
    return yaml.load(text.split("---\n", 2)[1], Loader=UniqueSafeLoader)


def test_all_fixture_hashes_and_tree_manifest(artifacts: Path) -> None:
    manifest = json.loads((FIXTURES / "manifest.json").read_text())
    actual = {
        p.relative_to(FIXTURES).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
        for folder in ("stock-analysis", "generic-okf", "parser-cases")
        for p in sorted((FIXTURES / folder).rglob("*"))
        if p.is_file()
    }
    assert actual == manifest["files"]
    tree = hashlib.sha256(
        "".join(f"{p}\0{h}\n" for p, h in sorted(actual.items())).encode()
    ).hexdigest()
    assert tree == manifest["tree_hash"]
    (artifacts / "fixture-manifest.json").write_bytes((FIXTURES / "manifest.json").read_bytes())


def test_stock_counts_evidence_identity_and_candidates(artifacts: Path) -> None:
    stock = FIXTURES / "stock-analysis"
    manifest = json.loads((stock / "manifest.json").read_text())
    pin = json.loads((FIXTURES / "manifest.json").read_text())
    assert len(manifest["sources"]) == 28
    assert all(r["page_complete"] for r in manifest["sources"].values())
    assert not manifest["pending_tail"]
    assert len(list((stock / "wiki/entities").glob("*.md"))) - 1 == 12
    assert len(list((stock / "wiki/concepts").glob("*.md"))) - 1 == 11
    assert (stock / "wiki/overview.md").is_file()
    assert len(pin["bull_source_ids"]) == 5
    for source_id, source in manifest["sources"].items():
        assert (
            hashlib.sha256((stock / source["raw_file"]).read_bytes()).hexdigest()
            == source["sha256"]
        )
        if source_id in pin["bull_source_ids"]:
            assert source["relative_path"].endswith("/BULL.md")
    validator = ROOT.parent / ".agents/skills/llm-wiki-markdown/scripts/validate_wiki.py"
    execution = subprocess.run(
        [sys.executable, str(validator), "--wiki-dir", str(stock)],
        check=True,
        text=True,
        capture_output=True,
    )
    result = json.loads(execution.stdout)
    assert not result["structural_errors"] and not result["evidence_errors"]
    assert sorted(result["warnings"]) == sorted(pin["warnings"])
    assert len(result["warnings"]) == 6
    for candidate in pin["candidate_targets"]:
        assert not (stock / f"wiki/entities/{candidate}.md").exists()
    (artifacts / "stock-validation.json").write_text(execution.stdout)


def test_generic_profile_has_no_stock_requirements() -> None:
    root = FIXTURES / "generic-okf"
    assert not (root / "manifest.json").exists()
    assert not (root / "raw").exists()
    assert metadata(root / "notes.md") == {"type": "note"}
    unknown = metadata(root / "experiment.md")
    assert unknown["type"] == "future-experiment"
    assert unknown["custom_field"] == {"unknown": "preserved"}
    weather = metadata(root / "Météo.md")
    assert unknown["sources"][0]["id"] == weather["sources"][0]["id"]
    assert unknown["sources"][0]["resource"] != weather["sources"][0]["resource"]
    assert metadata(root / "index.md")["okf_version"] == "0.2"
    assert metadata(root / "log.md") == {}
    tokens = MarkdownIt().parse((root / "index.md").read_text())
    links = [c.attrGet("href") for t in tokens for c in (t.children or []) if c.type == "link_open"]
    assert "M%C3%A9t%C3%A9o.md" in links
    assert not (root / "missing.md").exists()


@pytest.mark.parametrize("name", ["malformed-yaml.md", "duplicate-keys.md", "unsafe-yaml.md"])
def test_error_fixtures_reject_yaml_without_execution(name: str) -> None:
    with pytest.raises(yaml.YAMLError):
        metadata(FIXTURES / "parser-cases" / name)
    assert not (ROOT / "SHOULD_NOT_EXIST").exists()
