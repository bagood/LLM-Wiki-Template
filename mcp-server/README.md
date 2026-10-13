# LLM Wiki MCP — P0 foundation

P0 freezes 24 production contracts and proves a local FastAPI/MCP transport spike.
Production retrieval/index/workflow implementations arrive in P1–P4. The default
factory publishes no tools; the explicit development factory publishes only the probe.

Install uv 0.13.0+ and run from this directory:

```sh
uv python install
uv sync --locked --all-groups
uv run --locked python tools/validate_p0.py
uv run --locked uvicorn llm_wiki_mcp.app:create_dev_app --factory --host 127.0.0.1 --port 8000
```

The canonical endpoint is `http://127.0.0.1:8000/mcp`. `/mcp/` is deliberately 404,
and no POST redirect is required. The probe takes
`{"request":{"message":"hello","repeat":2}}` and returns bounded deterministic
echoes in structured content and compatible JSON text. No model API key is needed.
`/health/ready` covers P0 transport initialization; production storage readiness
and authentication arrive in P4. Keep this fixed-identity development app local.

The validation command performs a clean temporary locked install, Ruff, mypy, all
contract/unit/real-process integration tests, an FTS5 probe, and original-wiki hash
comparison. Evidence is written to `artifacts/validation/p0/`, outside originals.
Set `UV_BINARY` if the current uv executable is not on PATH. Normal validation
never changes frozen schemas/fixtures. To deliberately update contract schemas,
review model/example changes then run `uv run python tools/export_contracts.py`.

See [tool contracts](docs/tool-catalog.md), [workflow rules](docs/workflow-contract.md),
[ADRs](docs/adr/), [fixtures](tests/fixtures/README.md), and
[compatibility](../docs/compatibility.md). The phase report separates executed
checks, outstanding review acceptance, and future cloud access dependencies.
