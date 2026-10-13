from typing import Literal

from mcp.server import MCPServer
from mcp.types import ToolAnnotations
from pydantic import Field

from llm_wiki_mcp.container import Container
from llm_wiki_mcp.domain.models import Model


class ProbeRequest(Model):
    message: str = Field(min_length=1, max_length=128)
    repeat: int = Field(default=1, ge=1, le=3, strict=True)


class ProbeResult(Model):
    schema_version: Literal["1.0"] = "1.0"
    echoes: list[str]
    provider_required: Literal[False] = False


def register_probe(server: MCPServer, container: Container) -> None:
    @server.tool(
        annotations=ToolAnnotations(
            read_only_hint=True,
            destructive_hint=False,
            idempotent_hint=True,
            open_world_hint=False,
        )
    )
    async def dev_protocol_probe(request: ProbeRequest) -> ProbeResult:
        """Development compatibility probe: deterministically echo bounded input."""
        if container.identity is None:
            raise RuntimeError("Development identity was not configured")
        principal = await container.identity.principal()
        return ProbeResult(echoes=container.probe.echo(principal, request.message, request.repeat))
