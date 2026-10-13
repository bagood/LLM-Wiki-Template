from pydantic import Field

from llm_wiki_mcp.domain.errors import DomainError, ErrorCode
from llm_wiki_mcp.domain.models import Identifier, Model, Sha256, Step, WorkflowState

MAX_RESULT_BYTES = 65536
DEFAULT_CONTEXT_BYTES = 49152

TRANSITIONS: dict[WorkflowState, frozenset[WorkflowState]] = {
    "created": frozenset(("running", "failed", "cancelled")),
    "running": frozenset(("waiting_for_input", "completed", "failed", "cancelled")),
    "waiting_for_input": frozenset(("running", "failed", "cancelled")),
    "completed": frozenset(),
    "failed": frozenset(),
    "cancelled": frozenset(),
}


def require_transition(current: WorkflowState, target: WorkflowState) -> None:
    if target not in TRANSITIONS[current]:
        raise DomainError(ErrorCode.INVALID_TRANSITION, f"Cannot move {current} to {target}")


def validate_step_dag(steps: list[Step]) -> None:
    by_id = {s.step_id: s for s in steps}
    if len(by_id) != len(steps):
        raise DomainError(ErrorCode.INVALID_INPUT, "Step IDs must be unique")
    visited: set[str] = set()
    visiting: set[str] = set()

    def visit(step_id: str) -> None:
        if step_id not in by_id:
            raise DomainError(ErrorCode.INVALID_INPUT, "Unknown step dependency")
        if step_id in visiting:
            raise DomainError(ErrorCode.INVALID_INPUT, "Cyclic workflow dependency")
        if step_id in visited:
            return
        visiting.add(step_id)
        for dep in by_id[step_id].depends_on:
            visit(dep)
        visiting.remove(step_id)
        visited.add(step_id)

    for step_id in by_id:
        visit(step_id)


class CursorBinding(Model):
    """Signed opaque cursor payload; principal and all query parameters bind a read."""

    principal: Identifier
    operation: str
    wiki_id: Identifier | None
    snapshot_id: Identifier | None
    query_hash: Sha256
    position: str
    expires_at_unix: int = Field(ge=0)
