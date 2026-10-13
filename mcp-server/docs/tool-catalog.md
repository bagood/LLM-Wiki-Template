# Production tool contracts v1.0

These are frozen P2–P4 contracts, not tools registered by P0. The local spike
registers only `dev_protocol_probe`, which is absent from the production inventory.
The machine-readable [catalog](../contracts/catalog.json) contains all input/output
JSON Schemas, validated examples (including unavailable evidence), error codes,
annotations, scope, owner requirements, and 64 KiB result budgets. Python models in
`contracts/` are authoritative; `tools/export_contracts.py --check` detects drift.
Examples use a synthetic snapshot and hash for schema illustration; actual
acceptance-corpus bytes and identities are pinned in `tests/fixtures/manifest.json`.

| Category | Names | Delivery | Access |
|---|---|---|---|
| discovery | wiki_list, wiki_overview, wiki_search, wiki_resolve | P2 | wiki:read |
| retrieval | wiki_get_page, wiki_get_pages, wiki_get_evidence | P2 | wiki:read |
| graph | wiki_neighbors, wiki_subgraph, wiki_find_paths, wiki_provenance | P2 | wiki:read |
| reasoning | wiki_collect_context, wiki_compare, wiki_check_coverage, wiki_check_citations | P3 | wiki:read |
| workflow | workflow_create, workflow_get, workflow_checkpoint, workflow_finalize, workflow_cancel | P3 | owner; mutations require workflow:write and wiki:read |
| quality | wiki_validate, wiki_index_status | P4 | wiki:read |
| admin | admin_rebuild_index, admin_get_job | P4 | index:admin and per-wiki grant |

`wiki_list` requires no wiki ID and lists only authorized registrations. Every
other call requires wiki_id. Overview accepts an optional snapshot; search/resolve,
retrieval, graph, and reasoning require a snapshot from discovery. Quality tools
use current state unless a supported optional snapshot is selected. Workflow
mutations resolve their stored snapshot and require expected_version/idempotency;
create pins a supplied snapshot. Read tools may optionally associate `workflow_id`
through ResearchInput in P3, enforcing owner/wiki/snapshot and server auditing.
Overview/list are discovery and do not count as associated verified research.

Every result is an MCP CallToolResult with `structuredContent` conforming to the
output schema and a JSON text equivalent. Success has `data` and `error: null`;
expected application failure has `data: null`, a typed error, and MCP `isError: true`.
Envelope fields are schema_version, wiki_id, snapshot_id, data, error, citations,
warnings, truncated, and next_cursor. wiki_list uses null wiki/snapshot in the
envelope; each item has its own active snapshot. SDK protocol errors are JSON-RPC
errors, not application payloads. Authentication failures use transport 401/403.

Batch get returns individual page/error outcomes and `complete: false` if any
item failed or was truncated. Partial results retain valid citations. Ambiguous
resolve returns matches and `ambiguous: true`; operations needing one identity
return AMBIGUOUS_IDENTITY until a canonical identity is selected. Bundle-only raw
retrieval returns EVIDENCE_UNAVAILABLE for external originals, never fetches URLs,
and requires declaring_page_id to disambiguate a document-scoped source ID.

Portable resource identifiers: `wiki://<wiki>/index`,
`wiki://<wiki>/page/<percent-encoded-bundle-relative-path>`,
`wiki://<wiki>/evidence/<accepted-source-id>`, and `workflow://<workflow-id>`.
Generic declarations retain their resource URI plus declaring page/id; a future
generic original view uses `wiki://<wiki>/evidence/<provenance-id>?page=<encoded-path>`.
Resources select current snapshots and advertise them; pinned reads use tools.
Snapshot is part of citation identity even though portable page identity is stable.
Use 1-based inclusive original lines and 0-based half-open UTF-8 byte offsets.
See ADR 0005 for citation integrity and workflow-contract.md for state rules.

All results cap serialized UTF-8 application payloads at 65,536 bytes; descriptions
and wire overhead are accounted separately in transport metrics. Defaults/hard
caps: search 20/100; batch 10 pages and 4096 bytes/page default (shared result cap
still applies); retrieval 200/1000 lines; graph depth 2/5, nodes 200, edges 1000,
elapsed 1000/5000 ms; paths 5/20; context evidence 20/100 and 48/64 KiB. Filters and
user text are bounded in schemas; overall request byte/complexity limits are P4.
Trim whole items/passages, preserve citation references, return CONTENT_OMITTED
warnings with omitted item/byte counts and a cursor. Never return clipped citation
JSON. If required citation overhead alone exceeds the cap, return BUDGET_EXCEEDED.

Cursors bind principal, tool, wiki, snapshot, query/filters/budgets, position, and
expiry, including list cursors bound to the authorized registration set. Input
changes invalidate the cursor. Continuations stay on the selected snapshot.
Graph paths explain connections, not entailment; `semantic_support` is not_assessed.
Coverage completeness is scoped to indexed metadata. Context reports preserve
original strings and distinct horizon/date sets. Host output adds no evidence votes.

Errors use stable uppercase codes with actionable detail and explicit retryability.
The catalog lists the common error vocabulary for every tool; a code only occurs
where its named resource/policy applies. Never turn access denial into a host path
disclosure. Index jobs persist idempotency receipts and have no wiki write power.
Production annotations become effective only when implemented services guarantee
their semantics. Administrative discovery is restricted to authorized principals.
