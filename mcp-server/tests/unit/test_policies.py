from datetime import UTC, datetime, timedelta
from pathlib import Path

import pytest
from pydantic import ValidationError

from llm_wiki_mcp.config import Settings, WikiRegistration
from llm_wiki_mcp.domain.access import AccessPolicy
from llm_wiki_mcp.domain.errors import DomainError, ErrorCode
from llm_wiki_mcp.domain.models import Principal, Step, Workflow, WorkflowBudget
from llm_wiki_mcp.domain.policies import require_transition, validate_step_dag


def workflow() -> Workflow:
    now = datetime.now(UTC)
    return Workflow(
        workflow_id="w",
        wiki_id="garden",
        snapshot_id="s",
        owner="reader-1",
        version=1,
        goal="Research",
        state="running",
        steps=[],
        budget=WorkflowBudget(),
        created_at=now,
        expires_at=now + timedelta(days=1),
    )


def test_per_wiki_scope_and_workflow_ownership() -> None:
    access = AccessPolicy()
    reader = Principal(
        subject="reader-1", scopes=frozenset(("wiki:read",)), wiki_ids=frozenset(("garden",))
    )
    access.require(reader, "wiki:read", "garden")
    access.require_association(reader, workflow(), "garden", "s")
    for scope, wiki in (("wiki:read", "private"), ("index:admin", "garden")):
        with pytest.raises(DomainError) as caught:
            access.require(reader, scope, wiki)
        assert caught.value.error.code == ErrorCode.ACCESS_DENIED
    other = reader.model_copy(update={"subject": "reader-2"})
    with pytest.raises(DomainError):
        access.require_workflow(other, workflow())
    with pytest.raises(DomainError) as caught:
        access.require_association(reader, workflow(), "garden", "new-snapshot")
    assert caught.value.error.code == ErrorCode.VERSION_CONFLICT


def test_terminal_states_and_step_dependencies() -> None:
    require_transition("created", "running")
    require_transition("running", "waiting_for_input")
    require_transition("waiting_for_input", "running")
    for terminal in ("completed", "cancelled", "failed"):
        with pytest.raises(DomainError):
            require_transition(terminal, "running")
    validate_step_dag(
        [
            Step(step_id="a", description="Read"),
            Step(step_id="b", description="Check", depends_on=["a"]),
        ]
    )
    for steps in (
        [Step(step_id="a", description="Read", depends_on=["a"])],
        [Step(step_id="a", description="Read", depends_on=["missing"])],
        [Step(step_id="a", description="Read"), Step(step_id="a", description="Check")],
    ):
        with pytest.raises(DomainError):
            validate_step_dag(steps)


def test_state_paths_cannot_overlap_originals(tmp_path: Path) -> None:
    registration = WikiRegistration(wiki_id="garden", root=tmp_path, profile="okf_bundle")
    with pytest.raises(ValidationError):
        Settings(wikis=[registration], index_path=tmp_path / "index.sqlite3")
    with pytest.raises(ValidationError):
        Settings(index_path=tmp_path / "same", workflow_path=tmp_path / "same")
