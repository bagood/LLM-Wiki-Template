import json
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

import jsonschema
import pytest
from pydantic import ValidationError

from llm_wiki_mcp.contracts.catalog import CATALOG
from llm_wiki_mcp.contracts.inputs import (
    WikiCollectContextInput,
    WikiGetPagesInput,
    WikiSearchInput,
)
from llm_wiki_mcp.contracts.outputs import Envelope, WikiListData
from llm_wiki_mcp.domain.models import Citation, Span

ROOT = Path(__file__).resolve().parents[2]


def test_exact_parent_catalog_and_seven_categories() -> None:
    parent = (ROOT.parent / "docs/MCP-DEVELOPMENT-PLAN.md").read_text()
    catalog_section = parent.split("## 6.")[1].split("### Optional knowledge maintenance")[0]
    names = re.findall(r"\| `(\w+)` \|", catalog_section)
    assert len(names) == 24
    assert Counter(names) == Counter(t.name for t in CATALOG)
    assert Counter(t.category for t in CATALOG) == {
        "discovery": 4,
        "retrieval": 3,
        "graph": 4,
        "reasoning": 4,
        "workflow": 5,
        "quality": 2,
        "admin": 2,
    }


def test_frozen_schemas_and_examples() -> None:
    subprocess.run([sys.executable, "tools/export_contracts.py", "--check"], cwd=ROOT, check=True)
    inventory = json.loads((ROOT / "contracts/catalog.json").read_text())
    assert len(inventory["tools"]) == 24
    for tool in inventory["tools"]:
        for side in ("input", "output"):
            schema = tool[f"{side}_schema"]
            jsonschema.Draft202012Validator.check_schema(schema)
            jsonschema.validate(tool["example"][side], schema)
        assert tool["max_result_bytes"] == 65536
        assert tool["error_codes"]


def test_scope_version_ownership_and_idempotency_contracts() -> None:
    for tool in CATALOG:
        fields = tool.input_model.model_fields
        if tool.name == "wiki_list":
            assert "wiki_id" not in fields
        else:
            assert fields["wiki_id"].is_required()
        if tool.category in ("retrieval", "graph", "reasoning"):
            assert fields["snapshot_id"].is_required()
            assert not fields["workflow_id"].is_required()
        if tool.name in ("workflow_checkpoint", "workflow_finalize", "workflow_cancel"):
            assert fields["expected_version"].is_required()
            assert fields["idempotency_key"].is_required()
            assert tool.owner_required
        if not tool.read_only:
            assert fields["idempotency_key"].is_required()
            assert tool.idempotent


def test_budget_and_evidence_contract_rejections() -> None:
    with pytest.raises(ValidationError):
        WikiSearchInput(wiki_id="garden", snapshot_id="s", query="q", limit=101)
    with pytest.raises(ValidationError):
        WikiGetPagesInput(wiki_id="garden", snapshot_id="s", page_ids=["notes.md"] * 11)
    with pytest.raises(ValidationError):
        WikiCollectContextInput(wiki_id="garden", snapshot_id="s", max_bytes=65537)
    with pytest.raises(ValidationError):
        Span(start_line=4, end_line=2)
    with pytest.raises(ValidationError):
        Citation(
            citation_id="c",
            wiki_id="garden",
            snapshot_id="s",
            page_uri="wiki://garden/p",
            page_hash="a" * 64,
            page_span=Span(start_line=1, end_line=1),
            raw_hash="a" * 64,
        )
    with pytest.raises(ValidationError):
        Envelope[WikiListData](
            wiki_id=None, snapshot_id=None, data=WikiListData(wikis=[]), truncated=True
        )
