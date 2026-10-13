from typing import Protocol

from llm_wiki_mcp.domain.errors import DomainError, ErrorCode
from llm_wiki_mcp.domain.models import Principal, Scope, Workflow


class IdentitySource(Protocol):
    async def principal(self) -> Principal: ...


class TokenVerifier(Protocol):
    """P4 adapter validates signature, issuer, audience, and expiry before returning."""

    async def verify(self, token: str) -> Principal: ...


class AccessPolicy:
    def require(self, principal: Principal, scope: Scope, wiki_id: str) -> None:
        if scope not in principal.scopes or wiki_id not in principal.wiki_ids:
            raise DomainError(ErrorCode.ACCESS_DENIED, "Scope or wiki access is unavailable")

    def require_workflow(self, principal: Principal, workflow: Workflow) -> None:
        self.require(principal, "wiki:read", workflow.wiki_id)
        if principal.subject != workflow.owner:
            raise DomainError(ErrorCode.ACCESS_DENIED, "Workflow belongs to another principal")

    def require_association(
        self, principal: Principal, workflow: Workflow, wiki_id: str, snapshot_id: str
    ) -> None:
        self.require_workflow(principal, workflow)
        if workflow.wiki_id != wiki_id or workflow.snapshot_id != snapshot_id:
            raise DomainError(
                ErrorCode.VERSION_CONFLICT, "Workflow snapshot does not match the read"
            )
