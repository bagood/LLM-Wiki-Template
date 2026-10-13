from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from mcp.server import MCPServer

from llm_wiki_mcp.config import Settings
from llm_wiki_mcp.container import Container, create_container
from llm_wiki_mcp.controllers.mcp.probe import register_probe


def create_app(settings: Settings | None = None, container: Container | None = None) -> FastAPI:
    settings = settings or Settings()
    container = container or create_container(settings)
    server = MCPServer("llm-wiki-mcp-p0")
    if settings.development_probe:
        register_probe(server, container)

    # Creating this app initializes the manager. The host owns the mounted lifecycle.
    mcp_app = server.streamable_http_app(json_response=True)
    mcp_app.router.redirect_slashes = False

    @asynccontextmanager
    async def lifespan(app: FastAPI) -> AsyncIterator[None]:
        app.state.ready = False
        async with server.session_manager.run():
            app.state.ready = True
            try:
                yield
            finally:
                app.state.ready = False

    app = FastAPI(title="LLM Wiki MCP P0", lifespan=lifespan, redirect_slashes=False)
    app.state.container = container
    app.state.mcp_server = server
    app.state.ready = False

    @app.get("/health/live")
    async def live() -> dict[str, bool]:
        return {"live": True}

    @app.get("/health/ready")
    async def ready() -> dict[str, bool]:
        # P0 readiness covers the transport only. Storage/index readiness arrives in P4.
        return {"ready": app.state.ready}

    app.mount("/", mcp_app)
    return app


def create_dev_app() -> FastAPI:
    """Explicit opt-in for the local protocol spike."""
    return create_app(Settings(development_probe=True))
