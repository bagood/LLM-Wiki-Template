from datetime import datetime
from typing import Annotated, Literal

from pydantic import BaseModel, ConfigDict, Field, JsonValue, model_validator

Identifier = Annotated[str, Field(min_length=1, max_length=200)]
Sha256 = Annotated[str, Field(pattern=r"^[a-f0-9]{64}$")]
Profile = Literal["okf_bundle", "template_workspace"]
Scope = Literal["wiki:read", "workflow:write", "index:admin"]


class Model(BaseModel):
    model_config = ConfigDict(extra="forbid")


class Span(Model):
    """One-based inclusive lines; zero-based half-open UTF-8 byte offsets."""

    start_line: int = Field(ge=1)
    end_line: int = Field(ge=1)
    start_byte: int | None = Field(default=None, ge=0)
    end_byte: int | None = Field(default=None, ge=0)

    @model_validator(mode="after")
    def ordered(self) -> Span:
        if self.end_line < self.start_line:
            raise ValueError("end_line precedes start_line")
        if (self.start_byte is None) != (self.end_byte is None):
            raise ValueError("byte offsets must be supplied together")
        if self.start_byte is not None and self.end_byte is not None:
            if self.end_byte < self.start_byte:
                raise ValueError("end_byte precedes start_byte")
        return self


class ReportContext(Model):
    original: dict[str, JsonValue] = Field(default_factory=dict)
    normalized: dict[str, JsonValue] = Field(default_factory=dict)


class EvidenceIdentity(Model):
    provenance_id: Identifier
    declaring_page_uri: str
    resource_uri: str
    accepted_source_id: Identifier | None = None
    identity_mapping_id: Identifier | None = None


class Citation(Model):
    citation_id: Identifier
    wiki_id: Identifier
    snapshot_id: Identifier
    page_uri: str
    page_hash: Sha256
    section: str | None = None
    page_span: Span
    provenance: EvidenceIdentity | None = None
    raw_uri: str | None = None
    raw_hash: Sha256 | None = None
    raw_span: Span | None = None
    raw_read: bool = False
    contexts: list[ReportContext] = Field(default_factory=list)
    declaration: Literal["declared", "resolved", "unresolved"] = "declared"
    byte_integrity: Literal["verified", "not_checked", "failed"] = "not_checked"
    human_verification: Literal["reviewed", "not_reviewed"] = "not_reviewed"
    semantic_support: Literal["not_assessed"] = "not_assessed"
    independence: Literal["not_assessed", "dependent"] = "not_assessed"

    @model_validator(mode="after")
    def raw_coordinates(self) -> Citation:
        has_raw = any(x is not None for x in (self.raw_uri, self.raw_hash, self.raw_span))
        if has_raw and not self.raw_read:
            raise ValueError("raw coordinates require an actual raw read")
        if self.raw_read and not all(
            x is not None for x in (self.raw_uri, self.raw_hash, self.raw_span)
        ):
            raise ValueError("raw reads require URI, hash, and span")
        return self


class Warning(Model):
    code: str
    detail: str
    page_uri: str | None = None
    omitted_items: int = Field(default=0, ge=0)
    omitted_bytes: int = Field(default=0, ge=0)


class PageRecord(Model):
    wiki_id: Identifier
    snapshot_id: Identifier
    page_id: Identifier
    uri: str
    content_hash: Sha256
    type: str
    title: str | None = None
    metadata: dict[str, JsonValue] = Field(default_factory=dict)
    markdown: str
    span: Span
    total_lines: int = Field(ge=1)
    contexts: list[ReportContext] = Field(default_factory=list)


class EvidenceRecord(Model):
    identity: EvidenceIdentity
    uri: str
    content_hash: Sha256
    markdown: str
    span: Span
    total_lines: int = Field(ge=1)
    completeness: Literal["complete", "excerpt"]
    integrity: Literal["verified"] = "verified"
    contexts: list[ReportContext] = Field(default_factory=list)


Relation = Literal[
    "links_to",
    "navigation_link",
    "cites",
    "derived_from",
    "summarizes",
    "engages_entity",
    "engages_concept",
    "related_report",
    "context_match",
]


class GraphNode(Model):
    page_id: Identifier
    uri: str
    type: str | None = None
    materialized: bool = True
    target_status: Literal["resolved", "candidate", "unresolved"] = "resolved"


class Edge(Model):
    edge_id: Identifier
    origin: str
    target: str
    relation: Relation
    basis: Literal["markdown", "frontmatter", "manifest", "adapter"]
    span: Span | None = None
    metadata_key: str | None = None
    target_status: Literal["resolved", "candidate", "unresolved"]
    derived: bool = False


class Snapshot(Model):
    wiki_id: Identifier
    snapshot_id: Identifier
    tree_hash: Sha256
    created_at: datetime
    retained_until: datetime | None = None


class Principal(Model):
    subject: Identifier
    scopes: frozenset[Scope]
    wiki_ids: frozenset[str]


WorkflowState = Literal[
    "created", "running", "waiting_for_input", "completed", "failed", "cancelled"
]


class WorkflowBudget(Model):
    max_calls: int = Field(default=100, ge=1, le=1000)
    max_attempts_per_step: int = Field(default=3, ge=1, le=10)
    max_elapsed_seconds: int = Field(default=3600, ge=1, le=86400)
    max_returned_bytes: int = Field(default=1048576, ge=1, le=16777216)
    max_traversed_nodes: int = Field(default=1000, ge=1, le=10000)
    host_token_limit: int | None = Field(default=None, ge=1)
    host_cost_limit: float | None = Field(default=None, ge=0)


class WorkflowUsage(Model):
    calls: int = Field(default=0, ge=0)
    returned_bytes: int = Field(default=0, ge=0)
    traversed_nodes: int = Field(default=0, ge=0)
    elapsed_seconds: float = Field(default=0, ge=0)
    host_reported_tokens: int | None = Field(default=None, ge=0)
    host_reported_cost: float | None = Field(default=None, ge=0)


class Step(Model):
    step_id: Identifier
    description: str = Field(min_length=1, max_length=2000)
    depends_on: list[Identifier] = Field(default_factory=list)
    mandatory: bool = True
    status: Literal["pending", "running", "completed", "failed", "waived"] = "pending"
    attempts: int = Field(default=0, ge=0)


class Claim(Model):
    claim_id: Identifier
    text: str = Field(min_length=1, max_length=4000)
    citation_ids: list[Identifier] = Field(default_factory=list, max_length=100)
    synthesis: bool = False
    required_context: dict[str, JsonValue] = Field(default_factory=dict)


class Artifact(Model):
    artifact_id: Identifier
    kind: Literal["finding", "decision", "answer", "scope_reduction"]
    text: str = Field(min_length=1, max_length=16000)
    claims: list[Claim] = Field(default_factory=list, max_length=100)
    citation_ids: list[Identifier] = Field(default_factory=list, max_length=100)


class Workflow(Model):
    workflow_id: Identifier
    wiki_id: Identifier
    snapshot_id: Identifier
    owner: Identifier
    version: int = Field(ge=1)
    goal: str
    constraints: dict[str, JsonValue] = Field(default_factory=dict)
    state: WorkflowState
    steps: list[Step]
    budget: WorkflowBudget
    usage: WorkflowUsage = Field(default_factory=WorkflowUsage)
    artifacts: list[Artifact] = Field(default_factory=list)
    evidence_references: list[Identifier] = Field(default_factory=list)
    unresolved_questions: list[str] = Field(default_factory=list)
    created_at: datetime
    expires_at: datetime


class Job(Model):
    job_id: Identifier
    wiki_id: Identifier
    owner: Identifier
    state: Literal["queued", "running", "completed", "failed", "cancelled"]
    published_snapshot_id: Identifier | None = None
    diagnostics: list[str] = Field(default_factory=list)


class AuditEvent(Model):
    event_id: Identifier
    principal: Identifier
    wiki_id: Identifier
    snapshot_id: Identifier | None = None
    workflow_id: Identifier | None = None
    operation: str
    outcome: str
    returned_bytes: int = Field(ge=0)
    occurred_at: datetime
