from enum import StrEnum

from pydantic import BaseModel, ConfigDict


class ErrorCode(StrEnum):
    WIKI_NOT_FOUND = "WIKI_NOT_FOUND"
    PAGE_NOT_FOUND = "PAGE_NOT_FOUND"
    AMBIGUOUS_IDENTITY = "AMBIGUOUS_IDENTITY"
    EVIDENCE_UNAVAILABLE = "EVIDENCE_UNAVAILABLE"
    INTEGRITY_FAILURE = "INTEGRITY_FAILURE"
    SNAPSHOT_EXPIRED = "SNAPSHOT_EXPIRED"
    VERSION_CONFLICT = "VERSION_CONFLICT"
    BUDGET_EXCEEDED = "BUDGET_EXCEEDED"
    INVALID_CURSOR = "INVALID_CURSOR"
    WORKFLOW_NOT_FOUND = "WORKFLOW_NOT_FOUND"
    WORKFLOW_EXPIRED = "WORKFLOW_EXPIRED"
    INVALID_TRANSITION = "INVALID_TRANSITION"
    MANDATORY_STEP_INCOMPLETE = "MANDATORY_STEP_INCOMPLETE"
    IDEMPOTENCY_CONFLICT = "IDEMPOTENCY_CONFLICT"
    ACCESS_DENIED = "ACCESS_DENIED"
    JOB_NOT_FOUND = "JOB_NOT_FOUND"
    INVALID_INPUT = "INVALID_INPUT"


class ToolError(BaseModel):
    model_config = ConfigDict(extra="forbid")
    code: ErrorCode
    detail: str
    retryable: bool = False


class DomainError(Exception):
    def __init__(self, code: ErrorCode, detail: str, *, retryable: bool = False) -> None:
        self.error = ToolError(code=code, detail=detail, retryable=retryable)
        super().__init__(detail)
