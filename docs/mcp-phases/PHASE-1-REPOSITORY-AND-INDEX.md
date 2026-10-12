# P1 — Repository and index development plan

Status: planned; development validation has not been run. Estimated effort: **4–6 engineer-days**. Dependency: P0 complete. Parent: [MCP development plan](../MCP-DEVELOPMENT-PLAN.md). Previous: [P0](PHASE-0-CONTRACTS-AND-COMPATIBILITY.md). Next: [P2](PHASE-2-DISCOVERY-RETRIEVAL-AND-GRAPH.md).

## Objective and scope

Implement read-only OKF repositories and a rebuildable SQLite search/graph index. Produce verified evidence identities, exact retrieval spans, and atomic snapshots that later tools can query without reading inconsistent document versions.

This phase implements repository/adapter functionality and a local rebuild CLI. Public research tools arrive in P2; workflow execution and durable administrative job processing arrive in P3/P4. Original wiki files remain authoritative and unchanged.

## Entry checks

- [ ] Review passing P0 evidence, repository interfaces, input/citation contracts, and fixture hashes.
- [ ] Confirm the Python environment is locked and the configured SQLite runtime supports FTS5.
- [ ] Allocate separate writable index/test locations and a read-only original workspace root.
- [ ] Confirm the registered wiki IDs, bundle/workspace roots, profile selection, and approved local evidence roots.

## Implementation sequence

### 1. Implement filesystem and OKF adapters

- [ ] Read strict UTF-8 Markdown and safely parse YAML with duplicate-key rejection and size/depth limits; never interpret frontmatter as executable configuration.
- [ ] Preserve complete frontmatter, including unknown fields and types, body bytes, heading hierarchy, lifecycle fields, and original line/UTF-8 span mapping.
- [ ] Treat reserved index/log files as navigation/operational records, separate from the 52 content-page count.
- [ ] Implement `okf_bundle` without requiring a manifest, raw originals, stock metadata, titles, or a synthesis threshold.
- [ ] Implement `template_workspace` identity, completion, hashes, raw attachments, aliases, declared engagements, and validation rules behind the separate adapter.
- [ ] Normalize stock `report_context` only when valid; retain original timestamp strings, missing values, horizons, provisional dates, and the distinction between wiki generation and report dates.

### 2. Resolve links and construct graph records

- [ ] Use Markdown tokens to parse inline/reference links, citations, headings/fragments, images, and supported local attachments.
- [ ] Resolve relative and bundle-root paths, percent encoding, Unicode filenames, and approved `../../raw/...` targets with containment checks after normalization.
- [ ] Reject path traversal and symlink escape; retain external URIs without fetching them. Report unsupported Markdown constructs explicitly.
- [ ] Create the edge types in the parent plan, preserving extraction basis and origin spans/metadata keys. Label computed `context_match` edges separately from explicit links.
- [ ] Preserve unresolved candidate records with `materialized: false`; do not invent knowledge pages or semantic support/contradiction from links.
- [ ] Separate navigation hubs, page provenance, accepted originals, and attachments. Keep generic provenance identity local to the declaring page unless explicitly canonicalized.

### 3. Implement the SQLite index repository

- [ ] Add versioned migrations for snapshots, pages, sections, provenance entries, raw sources, edges, citations, candidate targets, validation findings, and FTS records.
- [ ] Enforce `(wiki_id, snapshot_id)` scoping and repository transactions; store accepted evidence IDs/hashes and exact indexed content required for later reads.
- [ ] Build FTS5/BM25 over title, aliases, descriptions, headings, and body sections; expose exact identity/alias resolution and context-filtered queries behind interfaces.
- [ ] Store backlinks through indexed edges; implement bounded adjacency/path primitives for P2 without moving graph logic into controllers.
- [ ] Preserve deduplication rules: identical-content aliases map to the accepted source; related reports remain distinct but are not automatically independent.

### 4. Implement index construction and snapshot publication

- [ ] Expose a CLI such as `python -m llm_wiki_mcp.cli.index --wiki-id agentic-stock-analysis --mode full --config <config-path>`; document the actual interface implemented.
- [ ] Build into staging, validate, and atomically switch the active snapshot only after success. A failed/interrupted build leaves the previous active snapshot available.
- [ ] Detect additions, edits, removals, and alias changes by hashes; produce a new snapshot for incremental updates without editing the workspace.
- [ ] Retain indexed content and verified evidence views for pinned snapshots; never combine an old page record with newly changed filesystem bytes.
- [ ] Quarantine missing/tampered accepted raw evidence and mark affected provenance. Manual knowledge-page edits are surfaced as drift, not automatically discarded.
- [ ] Define snapshot retention/deletion behavior; missing retained versions return `SNAPSHOT_EXPIRED`, not current content under an old ID.

### 5. Build fixture and baseline verification

- [ ] Index both P0 fixtures and the stock baseline; count content pages separately from navigation records and raw artifacts.
- [ ] Reconcile every accepted source with manifest ID, original path, SHA-256, line count, and completion status.
- [ ] Store all declared candidate targets and warning records. Different link spellings may normalize to one target while preserving individual findings.
- [ ] Run change/corruption experiments only on temporary fixture copies; compare complete original-workspace tree hashes before/after normal rebuilds.

## Required deliverables

| Deliverable | Planned location |
|---|---|
| Safe parser and profile adapters | `src/llm_wiki_mcp/adapters/{okf,template_workspace,stock_analysis}.py` |
| Filesystem/index repositories and migrations | `src/llm_wiki_mcp/repositories/`, `migrations/` |
| Build/validation services and rebuild CLI | `services/{indexing,validation}.py`, `cli/index.py` |
| Schema, indexing, and retention guide | `docs/index-design.md` |
| Parser/resolver, baseline, snapshot, and integrity tests | `tests/unit/`, `tests/integration/test_index_baseline.py`, `test_snapshot_consistency.py`, `test_index_integrity.py` |

All implementation paths are relative to the future `mcp-server/` project.

## Validation checks

| Check | Method | Pass condition and evidence |
|---|---|---|
| P1-V01 — Generic OKF acceptance | Index the nonfinancial fixture, including a `type`-only page and unknown fields/types. | Valid documents remain retrievable; missing optional/profile fields do not fail base conformance. Save parsed metadata. |
| P1-V02 — Baseline reconciliation | Index the pinned stock fixture and compare manifest and page counts. | 28 completed originals, 12 entities, 11 concepts, one overview; 52 content pages; three candidate targets and six baseline warning findings. Save reconciliation JSON. |
| P1-V03 — Links and spans | Exercise relative/root/reference links, encoding, fragments, attachments, cycles, and span reconstruction. | Resolved targets and excerpt bytes match fixtures; every edge retains its declared extraction basis; navigation and candidate status remain distinct. |
| P1-V04 — Integrity and identity | Tamper/remove raw files, add duplicate aliases, reuse a generic provenance ID across pages, and edit a knowledge page in fixture copies. | Invalid accepted evidence is unusable; aliases add no evidence vote; generic IDs do not collide; manual page drift remains visible. |
| P1-V05 — FTS and metadata | Run exact/alias/lexical lookups with ticker, role, strategy, and horizon filters. | Relevant hits and filter sets match reviewed fixtures; report dates and generation times stay separate. Save query/result samples. |
| P1-V06 — Atomic publication and recovery | Interrupt/fail a staged rebuild while reading the active snapshot. | Readers see a complete previous or new snapshot, never mixed rows; previous snapshot remains queryable after failed publication. |
| P1-V07 — Incremental and retained reads | Add/edit/delete fixture pages, publish a new snapshot, then query old/new and expired versions. | New index reflects changes; retained reads return old bytes; expired versions return `SNAPSHOT_EXPIRED`. |
| P1-V08 — Root isolation and immutability | Test traversal/symlink escapes and compare original workspace tree hashes before/after builds. | Out-of-root reads fail; original files are byte-identical; no external URLs were fetched. |
| P1-V09 — Layer and migration correctness | Run prior boundary checks and create/reopen a database from migrations. | Repositories satisfy interfaces; migrations yield a readable consistent database; transport-free services remain intact. |

## Planned validation commands

Run from `mcp-server/` after the named tests exist. Tests create their own temporary databases/configuration and exercise the CLI, including failure injection.

```sh
mkdir -p artifacts/validation/p1
uv sync --locked --all-groups
uv run --locked pytest tests/unit/test_okf_parser.py tests/unit/test_link_resolver.py tests/integration/test_index_baseline.py tests/integration/test_snapshot_consistency.py tests/integration/test_index_integrity.py tests/contracts/test_architecture.py --junitxml=artifacts/validation/p1/tests.xml
uv run --locked ruff check src tests
uv run --locked mypy src/llm_wiki_mcp
```

Also validate the untouched supplied workspace from the repository root using the existing helper environment:

```sh
uv run --script .agents/skills/llm-wiki-markdown/scripts/validate_wiki.py --wiki-dir wiki-agentic-stock-analysis
```

This helper checks the existing producer profile; it does not replace index consistency or semantic review tests. Store its output outside the workspace.

## Completion gate and handoff

- [ ] Every P1-V check passes, with no mandatory test skipped.
- [ ] Baseline reconciliation, candidate findings, old/new snapshot traces, and before/after tree hashes are saved under `artifacts/validation/p1/`.
- [ ] Create `phase-report.json` identifying revision, runtime, fixture hashes, database schema version, snapshot IDs, each check/result/evidence path, and reviewer outcome. Unexecuted checks remain `NOT_RUN`.
- [ ] Hand P2 the repository interfaces/implementations, validated snapshot, search/graph query primitives, citation/span models, and documented rebuild command.

Do not start P2 against a partly built index or accept raw-hash failure as a harmless warning. Fix failed checks and rerun impacted regressions before marking P1 complete.
