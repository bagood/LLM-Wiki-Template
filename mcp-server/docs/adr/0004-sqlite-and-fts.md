# ADR 0004: SQLite and FTS5

Status: proposed for owner review; storage implementation is P1/P3.

Use SQLite with FTS5/BM25 for the initial corpus and relational graph adjacency
tables. Every page/section/edge/search row is scoped to wiki and snapshot; workflow
records carry owner, pinned snapshot, and optimistic version. Keep the index and
workflow databases in separate paths outside originals and evidence roots.
P0 checks FTS5 in its selected local interpreter; P4 repeats this in the container.

The initial table inventory follows the parent plan: snapshots, pages, sections,
provenance entries, raw sources, edges, citations, candidate targets, validation
findings, FTS, workflows, steps, events, jobs, and audit records. Build in staging
and atomically publish a validated snapshot. One writer/worker, short transactions,
local storage, and durable jobs are the initial deployment limits. Workflow event,
version, idempotency receipt, usage, and audit updates share one transaction.

SearchRepository and GraphRepository allow later measured improvements without
changing contracts. Embeddings and a remote graph database are deferred; they
never become the evidence authority.
