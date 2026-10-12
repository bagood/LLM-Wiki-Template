# P2 — Discovery, retrieval, and graph development plan

Status: planned; development validation has not been run. Estimated effort: **4–5 engineer-days**. Dependency: P1 complete. Parent: [MCP development plan](../MCP-DEVELOPMENT-PLAN.md). Previous: [P1](PHASE-1-REPOSITORY-AND-INDEX.md). Next: [P3](PHASE-3-REASONING-AND-WORKFLOWS.md).

## Objective and scope

Expose **11 production tools** that let an MCP client discover knowledge, retrieve bounded page/raw passages, explore graph links, and trace provenance. Every result must preserve snapshot identity, citations, limits, and access isolation.

Build on P1 repositories through thin controllers and services. Resources supplement the tools but must not be required by a host that only supports tool calls. Remove or disable P0's development probe in production configuration.

## Entry checks

- [ ] P1 validation and snapshot reconciliation pass; the index can be rebuilt and reopened.
- [ ] P0 tool/error/citation schemas and limits are available for implementation.
- [ ] Test principals cover authorized/unauthorized wikis, differing roles, and resource access.
- [ ] Stock and generic fixtures have reviewed expected graph/search results and stable hashes.

## Tools to implement

| Category | Tool | Required behavior |
|---|---|---|
| Discovery | `wiki_list` | List only authorized registered wikis, profiles, capabilities, counts, and active snapshots. |
| Discovery | `wiki_overview` | Return scope/navigation/limitations and coverage without inventing missing overview content. |
| Discovery | `wiki_search` | Combine lexical/exact matches and context filters with scored snippets and stable pagination. |
| Discovery | `wiki_resolve` | Resolve identities/aliases, retain ambiguity, and distinguish nonmaterialized candidates. |
| Retrieval | `wiki_get_page` | Return metadata and a bounded section/line view with hash, total lines, citations, and continuation. |
| Retrieval | `wiki_get_pages` | Retrieve up to ten pages from one snapshot, keeping individual item successes/failures. |
| Retrieval | `wiki_get_evidence` | Return verified accepted-original passages; report unavailable originals for bundle-only inputs. |
| Graph | `wiki_neighbors` | Filter outgoing/incoming relations while marking unresolved targets and navigation edges. |
| Graph | `wiki_subgraph` | Expand seeds with depth/node/edge/time limits, cycle handling, and explicit truncation. |
| Graph | `wiki_find_paths` | Return bounded connection paths with the basis of every edge and no invented semantic implication. |
| Graph | `wiki_provenance` | Follow page/citation relationships to available original evidence, with deduplicated accepted IDs and integrity/dependence caveats. |

For production principals allowed all P2 capabilities, `tools/list` contains exactly these 11 names. Later-phase names must not be exposed as successful stubs.

## Implementation sequence

### 1. Implement discovery and retrieval services

- [ ] Wire registered wiki and snapshot selection to P1 repositories; validate the principal before lookup or result construction.
- [ ] Implement identity/alias resolution and score explanations; return ambiguous matches explicitly instead of picking an arbitrary page.
- [ ] Apply supported context filters without silently ignoring unknown filter names. Generic fixtures remain usable without stock fields.
- [ ] Retrieve indexed snapshot content with line/section boundaries; missing or expired snapshots return the typed error contract.
- [ ] Verify raw identity/hash and report the span actually returned; a short query read must not claim full-source coverage or semantic verification.
- [ ] Construct portable citations and continuations; unavailable originals and failed batch items remain explicit.

### 2. Implement graph services

- [ ] Add outgoing/backlink queries and relation-filtered traversal; use visited sets and deterministic ordering.
- [ ] Enforce graph depth 2/default and 5/max, 200 nodes/max, 1,000 edges/max, and elapsed-time limits.
- [ ] Exclude navigation edges from evidence-oriented expansion by default; allow callers to request them explicitly.
- [ ] Explain paths using source spans/metadata origins. Do not interpret a hyperlink as support, contradiction, or causation.
- [ ] Trace provenance through summaries to accepted originals while retaining unresolved citations, scope distinctions, and related-source caveats.
- [ ] Bind graph continuation to the same principal, wiki, filters, and snapshot so a cursor cannot change access or mix versions.

### 3. Register thin MCP controllers

- [ ] Register the four discovery, three retrieval, and four graph tools in their own modules and wire shared service instances from the container.
- [ ] Validate inputs and outputs against P0 schemas; return `structuredContent` and the compatible text representation described in the parent plan.
- [ ] Enforce read-only annotations and service-side access checks. Return typed domain errors separately from SDK protocol errors.
- [ ] Enforce search 20/default and 100/max hits, raw 200/default and 1,000/max lines, batch ten/max pages, and a 64 KiB total tool-result ceiling.
- [ ] Trim content without losing citation identities; declare `truncated`, omitted ranges, and continuation. Byte limits apply to the serialized response, including its text representation.
- [ ] Update the tool catalog with executable examples and normal/failure/partial results for all 11 tools.

### 4. Add resource views and real-client coverage

- [ ] Expose index/page/evidence resource views using the same services and permissions as tools; each view identifies its actual snapshot and bounded content.
- [ ] Validate parsed resource URIs; block guessed/out-of-root paths and unauthorized wiki IDs.
- [ ] Test discovery and calls against a real FastAPI/Uvicorn-hosted server for both protocol eras. Do not make resource or prompt support necessary for tool-only clients.
- [ ] Capture redacted traces for one complete entity → summary → raw-evidence journey.

## Required deliverables

| Deliverable | Planned location in `mcp-server/` |
|---|---|
| Discovery/retrieval/graph services | `src/llm_wiki_mcp/services/{discovery,retrieval,graph}.py` |
| Categorized controllers and resources | `controllers/mcp/{discovery,retrieval,graph}.py`, `controllers/resources.py` under the package |
| Updated public schemas and examples | `contracts/`, `docs/tool-catalog.md` |
| Tool contracts and access/budget tests | `tests/contracts/test_p2_tools.py`, `tests/integration/test_p2_access_and_limits.py` |
| Entity-to-original and graph client scenarios | `tests/e2e/test_p2_evidence_journey.py`, `test_p2_protocol_clients.py` |

## Validation checks

| Check | Method | Pass condition and evidence |
|---|---|---|
| P2-V01 — Inventory and schemas | Discover all tools as an authorized research principal; validate examples and actual results. | Exactly 11 unique P2 names; correct categories, schemas, read-only hints, text/structured output, and no development probe. Save catalog snapshot. |
| P2-V02 — Discovery/filter behavior | Search/resolve BULL, aliases, ambiguous labels, unknown labels, generic types, and 5dd/10dd contexts. | Matches/ambiguity/filter sets align with fixture expectations; no hidden filter dropping or fabricated topic pages. |
| P2-V03 — Evidence journey | Resolve BULL, read its entity, trace provenance, retrieve a source summary, and request an original span. | Correct accepted ID/hash/line coordinates and dated report context at every step; span bytes match the selected evidence snapshot. Save complete trace. |
| P2-V04 — Graph correctness | Use cyclic, navigation-heavy, disconnected, and candidate-link fixtures; compare known paths/backlinks. | Finite deterministic traversal, explicit relation basis, correct candidate status, and no invented semantic edges. |
| P2-V05 — Pagination and budgets | Exhaust search/graph/raw continuations; exceed every documented hard limit and cross-use cursors. | Limits enforced; no page loss/duplication in unchanged snapshots; omissions explicit; invalid cursor bindings rejected; result stays within byte cap. |
| P2-V06 — Partial/error behavior | Mix valid/missing batch IDs; request missing raw, invalid identity, tampered evidence, and expired snapshot. | Per-item errors and stable domain codes; unavailable/tampered evidence never returned as verified. |
| P2-V07 — Access parity | Repeat tool/resource calls with denied wiki and guessed IDs. | Both interfaces enforce the same access boundary; failures expose no unauthorized content. |
| P2-V08 — Transport and architecture | Run modern/legacy real-client calls and prior boundary tests. | Both modes return equivalent domain results; controllers contain no SQL/parser/graph algorithm logic. |
| P2-V09 — Snapshot and wiki immutability | Publish a new fixture snapshot during reads and compare original workspace hashes after scenarios. | Each call uses one declared snapshot; old content remains correct; original workspace is byte-identical. |

## Planned validation commands

Run from `mcp-server/` once the named tests exist. E2E tests must start the server, use real MCP clients, and save traces outside the wiki.

```sh
mkdir -p artifacts/validation/p2
uv run --locked pytest tests/contracts/test_p2_tools.py tests/integration/test_p2_access_and_limits.py tests/e2e/test_p2_evidence_journey.py tests/e2e/test_p2_protocol_clients.py tests/contracts/test_architecture.py --junitxml=artifacts/validation/p2/tests.xml
uv run --locked ruff check src tests
uv run --locked mypy src/llm_wiki_mcp
```

Retain baseline P1 regression checks when changing repository behavior; do not use mocked service-only calls as the sole proof of MCP delivery.

## Completion gate and handoff

- [ ] All P2-V checks pass and all 11 production tools return genuine implemented results.
- [ ] Save the catalog, entity-to-original trace, cursor/budget evidence, access results, and before/after workspace hashes under `artifacts/validation/p2/`.
- [ ] Create `phase-report.json` with revision, runtime, fixtures/snapshots, each check/result/evidence path, and reviewer outcome. Required skipped/unexecuted checks prevent completion.
- [ ] Hand P3 the working context-preserving tool surface, graph/provenance services, output/citation models, access hooks, and client examples.

Fix any lost provenance, leaked content, snapshot mixing, or silent truncation before accepting this phase. A successful `tools/list` response alone is insufficient.
