from llm_wiki_mcp.domain.access import AccessPolicy
from llm_wiki_mcp.domain.models import Principal


class ProbeService:
    def __init__(self, access: AccessPolicy) -> None:
        self.access = access

    def echo(self, principal: Principal, message: str, repeat: int) -> list[str]:
        self.access.require(principal, "wiki:read", "development-probe")
        return [message] * repeat
