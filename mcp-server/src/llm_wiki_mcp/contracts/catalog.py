from dataclasses import dataclass
from typing import Literal

from pydantic import BaseModel

from llm_wiki_mcp.contracts import inputs as i
from llm_wiki_mcp.contracts import outputs as o
from llm_wiki_mcp.domain.errors import ErrorCode
from llm_wiki_mcp.domain.models import Scope

Category = Literal["discovery", "retrieval", "graph", "reasoning", "workflow", "quality", "admin"]


@dataclass(frozen=True)
class ToolContract:
    name: str
    category: Category
    phase: Literal["P2", "P3", "P4"]
    input_model: type[BaseModel]
    output_model: type[BaseModel]
    scope: Scope
    owner_required: bool = False
    idempotent: bool = False
    max_result_bytes: int = 65536
    errors: tuple[ErrorCode, ...] = tuple(ErrorCode)

    @property
    def read_only(self) -> bool:
        return self.name not in {
            "workflow_create",
            "workflow_checkpoint",
            "workflow_finalize",
            "workflow_cancel",
            "admin_rebuild_index",
        }

    @property
    def required_scopes(self) -> tuple[Scope, ...]:
        return ("wiki:read", self.scope) if self.scope == "workflow:write" else (self.scope,)

    @property
    def annotations(self) -> dict[str, bool]:
        return {
            "readOnlyHint": self.read_only,
            "destructiveHint": False,
            "idempotentHint": self.read_only or self.idempotent,
            "openWorldHint": False,
        }


CATALOG: tuple[ToolContract, ...] = (
    ToolContract(
        "wiki_list", "discovery", "P2", i.WikiListInput, o.Envelope[o.WikiListData], "wiki:read"
    ),
    ToolContract(
        "wiki_overview",
        "discovery",
        "P2",
        i.WikiOverviewInput,
        o.Envelope[o.WikiOverviewData],
        "wiki:read",
    ),
    ToolContract(
        "wiki_search",
        "discovery",
        "P2",
        i.WikiSearchInput,
        o.Envelope[o.WikiSearchData],
        "wiki:read",
    ),
    ToolContract(
        "wiki_resolve",
        "discovery",
        "P2",
        i.WikiResolveInput,
        o.Envelope[o.WikiResolveData],
        "wiki:read",
    ),
    ToolContract(
        "wiki_get_page",
        "retrieval",
        "P2",
        i.WikiGetPageInput,
        o.Envelope[o.WikiGetPageData],
        "wiki:read",
    ),
    ToolContract(
        "wiki_get_pages",
        "retrieval",
        "P2",
        i.WikiGetPagesInput,
        o.Envelope[o.WikiGetPagesData],
        "wiki:read",
    ),
    ToolContract(
        "wiki_get_evidence",
        "retrieval",
        "P2",
        i.WikiGetEvidenceInput,
        o.Envelope[o.WikiGetEvidenceData],
        "wiki:read",
    ),
    ToolContract(
        "wiki_neighbors",
        "graph",
        "P2",
        i.WikiNeighborsInput,
        o.Envelope[o.WikiNeighborsData],
        "wiki:read",
    ),
    ToolContract(
        "wiki_subgraph",
        "graph",
        "P2",
        i.WikiSubgraphInput,
        o.Envelope[o.WikiSubgraphData],
        "wiki:read",
    ),
    ToolContract(
        "wiki_find_paths",
        "graph",
        "P2",
        i.WikiFindPathsInput,
        o.Envelope[o.WikiFindPathsData],
        "wiki:read",
    ),
    ToolContract(
        "wiki_provenance",
        "graph",
        "P2",
        i.WikiProvenanceInput,
        o.Envelope[o.WikiProvenanceData],
        "wiki:read",
    ),
    ToolContract(
        "wiki_collect_context",
        "reasoning",
        "P3",
        i.WikiCollectContextInput,
        o.Envelope[o.WikiCollectContextData],
        "wiki:read",
    ),
    ToolContract(
        "wiki_compare",
        "reasoning",
        "P3",
        i.WikiCompareInput,
        o.Envelope[o.WikiCompareData],
        "wiki:read",
    ),
    ToolContract(
        "wiki_check_coverage",
        "reasoning",
        "P3",
        i.WikiCheckCoverageInput,
        o.Envelope[o.WikiCheckCoverageData],
        "wiki:read",
    ),
    ToolContract(
        "wiki_check_citations",
        "reasoning",
        "P3",
        i.WikiCheckCitationsInput,
        o.Envelope[o.WikiCheckCitationsData],
        "wiki:read",
    ),
    ToolContract(
        "workflow_create",
        "workflow",
        "P3",
        i.WorkflowCreateInput,
        o.Envelope[o.WorkflowData],
        "workflow:write",
        idempotent=True,
    ),
    ToolContract(
        "workflow_get",
        "workflow",
        "P3",
        i.WorkflowGetInput,
        o.Envelope[o.WorkflowData],
        "wiki:read",
        owner_required=True,
    ),
    ToolContract(
        "workflow_checkpoint",
        "workflow",
        "P3",
        i.WorkflowCheckpointInput,
        o.Envelope[o.WorkflowData],
        "workflow:write",
        True,
        True,
    ),
    ToolContract(
        "workflow_finalize",
        "workflow",
        "P3",
        i.WorkflowFinalizeInput,
        o.Envelope[o.WorkflowFinalizeData],
        "workflow:write",
        True,
        True,
    ),
    ToolContract(
        "workflow_cancel",
        "workflow",
        "P3",
        i.WorkflowCancelInput,
        o.Envelope[o.WorkflowData],
        "workflow:write",
        True,
        True,
    ),
    ToolContract(
        "wiki_validate",
        "quality",
        "P4",
        i.WikiValidateInput,
        o.Envelope[o.WikiValidateData],
        "wiki:read",
    ),
    ToolContract(
        "wiki_index_status",
        "quality",
        "P4",
        i.WikiIndexStatusInput,
        o.Envelope[o.WikiIndexStatusData],
        "wiki:read",
    ),
    ToolContract(
        "admin_rebuild_index",
        "admin",
        "P4",
        i.AdminRebuildIndexInput,
        o.Envelope[o.AdminJobData],
        "index:admin",
        idempotent=True,
    ),
    ToolContract(
        "admin_get_job",
        "admin",
        "P4",
        i.AdminGetJobInput,
        o.Envelope[o.AdminJobData],
        "index:admin",
    ),
)
