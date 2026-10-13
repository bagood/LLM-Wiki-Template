from collections.abc import AsyncIterator
from contextlib import AbstractAsyncContextManager
from typing import Protocol

from pydantic import JsonValue

from llm_wiki_mcp.domain.models import (
    AuditEvent,
    Edge,
    EvidenceIdentity,
    EvidenceRecord,
    GraphNode,
    Job,
    PageRecord,
    Snapshot,
    Span,
    Workflow,
)


class PageRepository(Protocol):
    """All reads use retained snapshot bytes, never the current filesystem by accident."""

    async def get(self, wiki_id: str, snapshot_id: str, page_id: str) -> PageRecord: ...

    def scan(self, wiki_id: str, snapshot_id: str) -> AsyncIterator[PageRecord]: ...


class EvidenceRepository(Protocol):
    async def read(
        self, wiki_id: str, snapshot_id: str, identity: EvidenceIdentity, span: Span
    ) -> EvidenceRecord: ...


class SnapshotRepository(Protocol):
    async def active(self, wiki_id: str) -> Snapshot: ...

    async def get(self, wiki_id: str, snapshot_id: str) -> Snapshot: ...

    async def publish(self, snapshot: Snapshot) -> None: ...

    async def retain(self, wiki_id: str, snapshot_id: str, workflow_id: str) -> None: ...


class SearchRepository(Protocol):
    async def search(
        self,
        wiki_id: str,
        snapshot_id: str,
        query: str,
        filters: dict[str, JsonValue],
        limit: int,
        position: str | None,
    ) -> list[tuple[PageRecord, float]]: ...


class GraphRepository(Protocol):
    async def node(self, wiki_id: str, snapshot_id: str, page_id: str) -> GraphNode: ...

    async def edges(
        self, wiki_id: str, snapshot_id: str, page_id: str, direction: str
    ) -> list[Edge]: ...


class WorkflowRepository(Protocol):
    """Mutations, idempotency receipts, and audit writes commit in one transaction."""

    def transaction(self) -> AbstractAsyncContextManager[None]: ...

    async def get(self, wiki_id: str, workflow_id: str) -> Workflow: ...

    async def create(self, workflow: Workflow) -> None: ...

    async def save(self, workflow: Workflow, expected_version: int) -> None: ...

    async def idempotency_receipt(
        self, principal: str, operation: str, key: str, payload_hash: str
    ) -> dict[str, JsonValue] | None: ...

    async def record_receipt(
        self,
        principal: str,
        operation: str,
        key: str,
        payload_hash: str,
        result: dict[str, JsonValue],
    ) -> None: ...


class JobRepository(Protocol):
    async def get(self, wiki_id: str, job_id: str) -> Job: ...

    async def enqueue(self, job: Job, principal: str, key: str, payload_hash: str) -> Job: ...

    async def claim(self, worker_id: str, lease_seconds: int) -> Job | None: ...

    async def heartbeat(self, job_id: str, worker_id: str) -> None: ...

    async def finish(self, job: Job, worker_id: str) -> None: ...


class AuditRepository(Protocol):
    async def append(self, event: AuditEvent) -> None: ...

    async def for_workflow(self, principal: str, workflow_id: str) -> list[AuditEvent]: ...
