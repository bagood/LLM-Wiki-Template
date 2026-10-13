# ADR 0002: SDK mounting and protocol ownership

Status: proposed for owner review; implemented and tested in P0.

Pin CPython 3.14.8 (standard GIL) and official MCP SDK 2.3.0. FastAPI owns lifespan;
the SDK owns JSON-RPC, protocol validation, and both protocol eras. Create
`streamable_http_app()` before entering `session_manager.run()` in the parent
lifespan. The root mount follows health routes. Its internal `/mcp` is the sole
canonical public path; `/mcp/` and `/mcp/mcp` return 404 without a redirect.

Modern clients use 2026-07-28 self-contained requests; legacy clients negotiate
2025-11-25 and may carry sessions. P0 tests both with real Uvicorn subprocesses,
typed requests, structured/text output, errors, and repeat startup/shutdown.
No second protocol parser or transport workflow state is implemented.

The probe is absent by default and explicitly enabled by `create_dev_app`.
This local development app uses the SDK's default loopback host/origin protection.
Its identity source is fixed in the factory, never supplied by identity headers.
P4 will implement the protected resource server and real readiness/storage checks.
