from dataclasses import dataclass

from llm_wiki_mcp.config import Settings
from llm_wiki_mcp.domain.access import AccessPolicy, IdentitySource, TokenVerifier
from llm_wiki_mcp.domain.models import Principal
from llm_wiki_mcp.repositories.interfaces import (
    AuditRepository,
    EvidenceRepository,
    GraphRepository,
    JobRepository,
    PageRepository,
    SearchRepository,
    SnapshotRepository,
    WorkflowRepository,
)
from llm_wiki_mcp.services.probe import ProbeService


@dataclass(frozen=True)
class Repositories:
    pages: PageRepository
    evidence: EvidenceRepository
    snapshots: SnapshotRepository
    search: SearchRepository
    graph: GraphRepository
    workflows: WorkflowRepository
    jobs: JobRepository
    audit: AuditRepository


@dataclass(frozen=True)
class DevelopmentIdentity:
    """A fixed factory-supplied identity; never reads caller-controlled identity headers."""

    value: Principal

    async def principal(self) -> Principal:
        return self.value


@dataclass(frozen=True)
class Container:
    settings: Settings
    identity: IdentitySource | None
    access: AccessPolicy
    probe: ProbeService
    repositories: Repositories | None = None
    token_verifier: TokenVerifier | None = None


def create_container(
    settings: Settings,
    *,
    identity: IdentitySource | None = None,
    repositories: Repositories | None = None,
    token_verifier: TokenVerifier | None = None,
) -> Container:
    if settings.development_probe and identity is None:
        identity = DevelopmentIdentity(
            Principal(
                subject="development-reader",
                scopes=frozenset(("wiki:read",)),
                wiki_ids=frozenset(("development-probe",)),
            )
        )
    access = AccessPolicy()
    return Container(settings, identity, access, ProbeService(access), repositories, token_verifier)
