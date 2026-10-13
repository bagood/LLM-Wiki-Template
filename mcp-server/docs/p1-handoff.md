# P1 handoff

P0 implementation and automated checks are ready; the owner must accept the
decisions/contracts before the formal P0 completion gate closes.

- Storage ports: `repositories/interfaces.py` defines page, evidence, search,
  graph, snapshot, workflow, job, and audit interfaces. Implement concrete
  filesystem/index ports without importing controllers or tool contracts.
- Compose services through `container.Repositories` in the application factory.
  Mounted MCP handlers must continue resolving container dependencies explicitly.
- Generic and template profiles: ADR 0003 and the pinned generic/parser fixtures.
  Preserve unknown metadata; keep base OKF separate from producer quality rules.
- Frozen schemas: `contracts/catalog.json`; change models/examples through reviewed
  exports. Scope/ownership/version/idempotency and workflow associations are explicit.
- Snapshot/citation contract: ADR 0005. Retain snapshot bytes and raw-read spans;
  do not substitute current filesystem bytes or invent global generic source IDs.
- SQLite/FTS5: ADR 0004; P0 environment report qualifies local FTS5. P4 still
  qualifies the container. Derived databases belong outside registered originals.
- Corpus: `tests/fixtures/manifest.json` pins 28 completed sources, 52 content
  pages, five BULL source IDs, three candidates/six warnings, and all fixture hashes.
- Compatibility evidence: `artifacts/validation/p0/phase-report.json`, real-client
  traces and server lifecycle logs. CI, Docker and cloud integrations remain separate.

Do not change the original wiki, execute source text, fetch external provenance,
or register unimplemented production tools while building the P1 index.
