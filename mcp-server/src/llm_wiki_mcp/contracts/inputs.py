from typing import Annotated, Literal

from pydantic import Field, JsonValue, model_validator

from llm_wiki_mcp.domain.models import (
    Artifact,
    Citation,
    Claim,
    Identifier,
    Model,
    Relation,
    Span,
    Step,
    WorkflowBudget,
)

PageIds = Annotated[list[Identifier], Field(min_length=1, max_length=10)]
IdempotencyKey = Annotated[str, Field(min_length=8, max_length=200)]


class WikiListInput(Model):
    cursor: str | None = Field(default=None, max_length=4096)
    limit: int = Field(default=20, ge=1, le=100)


class WikiInput(Model):
    wiki_id: Identifier


class WikiOverviewInput(WikiInput):
    snapshot_id: Identifier | None = None


class ResearchInput(WikiInput):
    snapshot_id: Identifier
    workflow_id: Identifier | None = None


class Filters(Model):
    types: list[str] = Field(default_factory=list, max_length=20)
    metadata: dict[str, JsonValue] = Field(default_factory=dict)


class WikiSearchInput(ResearchInput):
    query: str = Field(min_length=1, max_length=2000)
    filters: Filters = Field(default_factory=Filters)
    limit: int = Field(default=20, ge=1, le=100)
    cursor: str | None = Field(default=None, max_length=4096)


class WikiResolveInput(ResearchInput):
    label: str = Field(min_length=1, max_length=500)
    type: str | None = None


class WikiGetPageInput(ResearchInput):
    page_id: Identifier
    section: str | None = Field(default=None, max_length=500)
    line_range: Span | None = None
    max_lines: int = Field(default=200, ge=1, le=1000)
    cursor: str | None = Field(default=None, max_length=4096)

    @model_validator(mode="after")
    def one_selector(self) -> WikiGetPageInput:
        if self.section is not None and self.line_range is not None:
            raise ValueError("select either section or line_range")
        return self


class WikiGetPagesInput(ResearchInput):
    page_ids: PageIds
    per_page_bytes: int = Field(default=4096, ge=256, le=65536)


class WikiGetEvidenceInput(ResearchInput):
    source_id: Identifier
    declaring_page_id: Identifier | None = None
    line_range: Span | None = None
    max_lines: int = Field(default=200, ge=1, le=1000)
    cursor: str | None = Field(default=None, max_length=4096)


class WikiNeighborsInput(ResearchInput):
    page_id: Identifier
    direction: Literal["outgoing", "incoming", "both"] = "both"
    relations: list[Relation] = Field(default_factory=list)
    include_navigation: bool = False
    limit: int = Field(default=20, ge=1, le=100)
    cursor: str | None = Field(default=None, max_length=4096)


class GraphBudget(Model):
    max_nodes: int = Field(default=200, ge=1, le=200)
    max_edges: int = Field(default=1000, ge=1, le=1000)
    max_elapsed_ms: int = Field(default=1000, ge=1, le=5000)


class WikiSubgraphInput(ResearchInput):
    seed_ids: PageIds
    depth: int = Field(default=2, ge=0, le=5)
    relations: list[Relation] = Field(default_factory=list)
    include_navigation: bool = False
    budget: GraphBudget = Field(default_factory=GraphBudget)
    cursor: str | None = Field(default=None, max_length=4096)


class WikiFindPathsInput(ResearchInput):
    from_id: Identifier
    to_id: Identifier
    relations: list[Relation] = Field(default_factory=list)
    include_navigation: bool = False
    max_hops: int = Field(default=2, ge=1, le=5)
    limit: int = Field(default=5, ge=1, le=20)
    budget: GraphBudget = Field(default_factory=GraphBudget)
    cursor: str | None = Field(default=None, max_length=4096)


class WikiProvenanceInput(ResearchInput):
    page_id: Identifier
    section: str | None = None
    depth: int = Field(default=2, ge=1, le=5)
    budget: GraphBudget = Field(default_factory=GraphBudget)
    cursor: str | None = Field(default=None, max_length=4096)


class WikiCollectContextInput(ResearchInput):
    seed_ids: list[Identifier] = Field(default_factory=list, max_length=10)
    query: str | None = Field(default=None, min_length=1, max_length=2000)
    filters: Filters = Field(default_factory=Filters)
    max_evidence: int = Field(default=20, ge=1, le=100)
    max_bytes: int = Field(default=49152, ge=1024, le=65536)
    cursor: str | None = Field(default=None, max_length=4096)

    @model_validator(mode="after")
    def seeds_or_query(self) -> WikiCollectContextInput:
        if bool(self.seed_ids) == bool(self.query):
            raise ValueError("supply seed_ids or query, exclusively")
        return self


class WikiCompareInput(ResearchInput):
    page_ids: Annotated[list[Identifier], Field(min_length=2, max_length=10)]
    fields: list[str] = Field(default_factory=list, max_length=30)
    sections: list[str] = Field(default_factory=list, max_length=20)


class WikiCheckCoverageInput(ResearchInput):
    topic_ids: PageIds
    required_contexts: list[dict[str, JsonValue]] = Field(default_factory=list, max_length=100)
    required_fields: list[str] = Field(default_factory=list, max_length=30)


class WikiCheckCitationsInput(ResearchInput):
    claims: list[Claim] = Field(min_length=1, max_length=100)
    citations: list[Citation] = Field(min_length=1, max_length=100)


class WorkflowCreateInput(WikiInput):
    snapshot_id: Identifier
    goal: str = Field(min_length=1, max_length=4000)
    constraints: dict[str, JsonValue] = Field(default_factory=dict)
    template: Literal["research_question", "compare_reports", "trace_claim"] | None = None
    steps: list[Step] = Field(default_factory=list, max_length=30)
    budget: WorkflowBudget = Field(default_factory=WorkflowBudget)
    expires_in_seconds: int = Field(default=86400, ge=60, le=2592000)
    idempotency_key: IdempotencyKey

    @model_validator(mode="after")
    def plan_selector(self) -> WorkflowCreateInput:
        if bool(self.template) == bool(self.steps):
            raise ValueError("supply a template or explicit steps, exclusively")
        if any(s.status != "pending" or s.attempts for s in self.steps):
            raise ValueError("new steps must be pending with zero attempts")
        return self


class WorkflowGetInput(WikiInput):
    workflow_id: Identifier


class WorkflowMutationInput(WorkflowGetInput):
    expected_version: int = Field(ge=1)
    idempotency_key: IdempotencyKey


class ScopeReduction(Model):
    reason: str = Field(min_length=1, max_length=2000)
    waived_step_ids: list[Identifier] = Field(default_factory=list, max_length=30)
    removed_requirements: list[str] = Field(default_factory=list, max_length=30)


class WorkflowCheckpointInput(WorkflowMutationInput):
    event: Literal["start", "step_started", "step_completed", "wait", "resume", "scope_reduction"]
    step_id: Identifier | None = None
    artifacts: list[Artifact] = Field(default_factory=list, max_length=30)
    unresolved_questions: list[str] = Field(default_factory=list, max_length=30)
    scope_reduction: ScopeReduction | None = None

    @model_validator(mode="after")
    def event_payload(self) -> WorkflowCheckpointInput:
        if self.event in ("step_started", "step_completed") and self.step_id is None:
            raise ValueError("step events require step_id")
        if (self.event == "scope_reduction") != (self.scope_reduction is not None):
            raise ValueError("scope reduction requires an explicit reason and reduction payload")
        return self


class WorkflowFinalizeInput(WorkflowMutationInput):
    answer: Artifact

    @model_validator(mode="after")
    def answer_kind(self) -> WorkflowFinalizeInput:
        if self.answer.kind != "answer":
            raise ValueError("finalization requires an answer artifact")
        return self


class WorkflowCancelInput(WorkflowMutationInput):
    reason: str = Field(min_length=1, max_length=2000)


class WikiValidateInput(WikiInput):
    snapshot_id: Identifier | None = None
    scope: Literal["bundle", "profile", "index"] = "bundle"
    page_ids: list[Identifier] = Field(default_factory=list, max_length=10)


class WikiIndexStatusInput(WikiInput):
    pass


class AdminRebuildIndexInput(WikiInput):
    mode: Literal["full", "incremental"] = "incremental"
    idempotency_key: IdempotencyKey


class AdminGetJobInput(WikiInput):
    job_id: Identifier
