from typing import Literal

from pydantic import Field, JsonValue, model_validator

from llm_wiki_mcp.domain.errors import ToolError
from llm_wiki_mcp.domain.models import (
    Citation,
    Edge,
    EvidenceIdentity,
    EvidenceRecord,
    GraphNode,
    Identifier,
    Job,
    Model,
    PageRecord,
    Profile,
    ReportContext,
    Snapshot,
    Warning,
    Workflow,
)


class Envelope[T](Model):
    schema_version: Literal["1.0"] = "1.0"
    wiki_id: Identifier | None
    snapshot_id: Identifier | None
    data: T | None
    error: ToolError | None = None
    citations: list[Citation] = Field(default_factory=list)
    warnings: list[Warning] = Field(default_factory=list)
    truncated: bool = False
    next_cursor: str | None = None

    @model_validator(mode="after")
    def result_invariants(self) -> Envelope[T]:
        if (self.data is None) == (self.error is None):
            raise ValueError("exactly one of data and error must be present")
        if self.truncated and not any(w.code == "CONTENT_OMITTED" for w in self.warnings):
            raise ValueError("trimming must advertise omissions")
        if self.next_cursor is not None and not self.truncated:
            raise ValueError("continuation implies truncated content")
        if any(
            c.wiki_id != self.wiki_id or c.snapshot_id != self.snapshot_id for c in self.citations
        ):
            raise ValueError("citations must belong to the response wiki and snapshot")
        return self


class Counts(Model):
    content_pages: int = Field(ge=0)
    sources: int = Field(ge=0)
    entities: int = Field(ge=0)
    concepts: int = Field(ge=0)
    overviews: int = Field(ge=0)


class WikiSummary(Model):
    wiki_id: Identifier
    scope: str
    profile: Profile
    okf_version: str
    capabilities: list[str]
    active_snapshot_id: Identifier | None
    counts: Counts


class WikiListData(Model):
    wikis: list[WikiSummary]


class WikiOverviewData(Model):
    navigation: list[GraphNode]
    coverage: Counts
    limitations: list[str]
    contexts: list[ReportContext]
    candidates: list[GraphNode]


class SearchHit(Model):
    page_id: Identifier
    section: str | None
    uri: str
    snippet: str
    score: float
    score_components: dict[str, float]
    citation_ids: list[Identifier]
    contexts: list[ReportContext]


class WikiSearchData(Model):
    hits: list[SearchHit]
    total_matches: int = Field(ge=0)


class WikiResolveData(Model):
    matches: list[GraphNode]
    candidates: list[GraphNode]
    ambiguous: bool


class WikiGetPageData(Model):
    page: PageRecord


class PageOutcome(Model):
    page_id: Identifier
    page: PageRecord | None
    error: ToolError | None = None

    @model_validator(mode="after")
    def one_outcome(self) -> PageOutcome:
        if (self.page is None) == (self.error is None):
            raise ValueError("each batch item requires a page or error")
        return self


class WikiGetPagesData(Model):
    results: list[PageOutcome]
    complete: bool

    @model_validator(mode="after")
    def partial_batch(self) -> WikiGetPagesData:
        if self.complete and any(r.error is not None for r in self.results):
            raise ValueError("failed batch items cannot be reported complete")
        return self


class WikiGetEvidenceData(Model):
    evidence: EvidenceRecord


class WikiNeighborsData(Model):
    nodes: list[GraphNode]
    edges: list[Edge]


class WikiSubgraphData(WikiNeighborsData):
    visited_nodes: int = Field(ge=0)
    elapsed_ms: float = Field(ge=0)


class ConnectionPath(Model):
    nodes: list[GraphNode]
    edges: list[Edge]


class WikiFindPathsData(Model):
    paths: list[ConnectionPath]
    interpretation: Literal["connection_only"] = "connection_only"


class WikiProvenanceData(Model):
    chain: list[Edge]
    evidence_identities: list[EvidenceIdentity]
    dependence_caveats: list[str]


class ContextPassage(Model):
    page_id: Identifier
    markdown: str
    citation_ids: list[Identifier]
    contexts: list[ReportContext]


class WikiCollectContextData(Model):
    passages: list[ContextPassage]
    evidence_identities: list[EvidenceIdentity]
    limitations: list[str]
    follow_up_candidates: list[GraphNode]


class ComparisonCell(Model):
    page_id: Identifier
    field: str
    value: JsonValue
    missing: bool
    passages: list[ContextPassage]


class WikiCompareData(Model):
    cells: list[ComparisonCell]
    structured_differences: list[str]
    unresolved_semantic_questions: list[str]


class CoverageCell(Model):
    topic_id: Identifier
    required_context: dict[str, JsonValue]
    accepted_source_ids: list[Identifier]
    missing_fields: list[str]
    unresolved_citation_ids: list[Identifier]


class WikiCheckCoverageData(Model):
    cells: list[CoverageCell]
    complete: bool
    completeness_scope: Literal["indexed_metadata"] = "indexed_metadata"


class CitationCheck(Model):
    citation_id: Identifier
    exists: bool
    hash_matches: bool | None
    span_valid: bool | None
    identity_valid: bool | None
    context_matches: bool | None
    semantic_support: Literal["not_assessed"] = "not_assessed"
    issues: list[str]


class WikiCheckCitationsData(Model):
    checks: list[CitationCheck]
    unresolved_claim_ids: list[Identifier]


class WorkflowData(Model):
    workflow: Workflow
    next_eligible_step_ids: list[Identifier]


class WorkflowFinalizeData(WorkflowData):
    outcome: Literal["completed", "incomplete"]
    gaps: list[str]
    pages_used: list[str]

    @model_validator(mode="after")
    def completion_state(self) -> WorkflowFinalizeData:
        if self.outcome == "completed" and (self.workflow.state != "completed" or self.gaps):
            raise ValueError("completion requires terminal state and no required gaps")
        if self.outcome == "incomplete" and self.workflow.state != "waiting_for_input":
            raise ValueError("incomplete finalization remains waiting_for_input")
        return self


class ValidationFinding(Model):
    code: str
    severity: Literal["warning", "error"]
    detail: str
    page_uri: str | None


class WikiValidateData(Model):
    scope: Literal["bundle", "profile", "index"]
    valid: bool
    findings: list[ValidationFinding]


class WikiIndexStatusData(Model):
    active_snapshot: Snapshot | None
    age_seconds: float | None = Field(default=None, ge=0)
    jobs: list[Job]
    failed_evidence_ids: list[Identifier]
    rebuild_needed: bool


class AdminJobData(Model):
    job: Job
