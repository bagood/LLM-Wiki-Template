# P3 — Reasoning and workflows development plan

Status: planned; development validation has not been run. Estimated effort: **5–7 engineer-days**. Dependency: P2 complete. Parent: [MCP development plan](../MCP-DEVELOPMENT-PLAN.md). Previous: [P2](PHASE-2-DISCOVERY-RETRIEVAL-AND-GRAPH.md). Next: [P4](PHASE-4-DOCKER-AND-OPERATIONAL-HARDENING.md).

## Objective and scope

Add four reasoning-support tools and five durable workflow tools, bringing the implemented inventory to **20 production tools**. Enable an AI host to plan, investigate, compare, checkpoint, resume, and finalize research using the wiki without converting its answers into accepted source evidence.

Reasoning stays in the connected host. Services assemble and check evidence deterministically; they do not require model API keys, sampling, private chain-of-thought, or a server-hosted model. This phase tests durable process restart; P4 validates persistence inside the final container deployment and P5 validates real AI hosts.

## Entry checks

- [ ] P2's 11 tools, real-client evidence journey, access checks, and snapshot tests pass.
- [ ] P0 defines workflow states, legal transitions, idempotency, ownership, budgets, and incomplete finalization.
- [ ] P1 supports retained snapshot content and explicit expired-snapshot errors.
- [ ] Confirm the BULL fixture's five accepted source summaries and expected strategy/horizon coverage.

## Tools to implement

| Category | Tool | Required behavior |
|---|---|---|
| Reasoning support | `wiki_collect_context` | Assemble a bounded evidence packet with context distinctions, citations, limitations, omissions, and relevant follow-up candidates. |
| Reasoning support | `wiki_compare` | Align requested fields/passages, preserve distinct report contexts, and surface missing/incomparable values. |
| Reasoning support | `wiki_check_coverage` | Return corpus/metadata-scoped topic and context coverage with accepted-source counts and gaps. |
| Reasoning support | `wiki_check_citations` | Check identity, existence, hash, span, and context; use `semantic_support: not_assessed` where entailment needs judgment. |
| Workflow | `workflow_create` | Persist a host-provided goal/plan or reviewed template, pinned snapshot, owner, constraints, and budgets. |
| Workflow | `workflow_get` | Return the owner's durable plan, findings, unresolved questions, progress, and eligible next steps. |
| Workflow | `workflow_checkpoint` | Atomically validate/store a step event and artifact references using version and idempotency controls. |
| Workflow | `workflow_finalize` | Check required steps and references; complete a valid artifact or retain a nonterminal incomplete result. |
| Workflow | `workflow_cancel` | Persist terminal cancellation and its audit event; reject later mutations. |

Resume through `workflow_get` followed by checkpoints; keep the original workflow ID across conversations/processes.

## Implementation sequence

### 1. Implement evidence assembly and comparison

- [ ] Build context packets from exact/search seeds and bounded graph expansion; apply the selected snapshot and filters throughout.
- [ ] Deduplicate accepted evidence IDs while retaining separate 5dd/10dd and strategy contexts; do not count summaries, aliases, or workflow output as extra evidence.
- [ ] Keep explicit source claims, inferred workflow findings, integrity status, verification declarations, and source independence as distinct fields.
- [ ] Enforce a 48 KiB default context packet and the 64 KiB total tool-result ceiling; preserve citations and advertise omitted passages/ranges.
- [ ] Compare structured values only when their context/units make the comparison meaningful. Return passages and unresolved questions for semantic disagreement rather than inventing `contradicts` edges.
- [ ] Compute coverage from indexed metadata and declared requirements; missing required metadata is unknown/missing, not proof that the underlying report lacks all discussion.
- [ ] Validate proposed claim citations against actual snapshot spans. Do not label successful structural citation checks as semantic endorsement.

### 2. Implement the workflow repository and service

- [ ] Add migrations for `workflows`, `workflow_steps`, `workflow_events`, and artifact references in the separate durable state database.
- [ ] Persist owner, goal, constraints, snapshot, step DAG, attempts, status, unresolved questions, expiry, concise findings, budgets, and optimistic version.
- [ ] Validate DAG references/cycles and legal state transitions for `created`, `running`, `waiting_for_input`, `completed`, `failed`, and `cancelled`.
- [ ] Enforce mandatory steps and pinned evidence references before finalization. Missing required evidence remains incomplete unless the host explicitly records a reviewed scope change that allows a gaps-only answer.
- [ ] Scope idempotency to principal, operation, and payload hash; identical retries return the previous result, while changed payloads using the same key fail without extra mutation.
- [ ] Use expected versions and transactional event/state updates. Return success only after commit; stale concurrent writers return `VERSION_CONFLICT`.
- [ ] Enforce server-observed call/attempt/time/output limits. Label model token/cost usage as host-reported rather than independently verified.
- [ ] Wire the common optional `workflow_id` association into research calls; validate owner/snapshot and atomically account for associated calls. Keep unassociated wiki reads separate from workflow budget/audit claims.
- [ ] Audit actual tool calls separately from host checkpoint claims; store concise decision/evidence artifacts, not private reasoning transcripts.

### 3. Implement controllers, ownership, and restart behavior

- [ ] Register four reasoning tools and five workflow tools in separate modules with appropriate schemas, scopes, and read/mutation annotations.
- [ ] Check workflow ownership on every get/checkpoint/finalize/cancel and workflow resource read, even for guessed IDs.
- [ ] After restart, reopen the same state database and resume via workflow ID, without dependence on a remembered transport session.
- [ ] Reconcile retained snapshot requirements with active workflows. An expired snapshot produces a clear failure/replan path; it must not silently use the active snapshot.
- [ ] Validate retry behavior after a simulated commit followed by a disconnected/lost response.
- [ ] Add bounded workflow retention and expiry behavior; retain audit evidence according to the documented policy.

### 4. Add reviewed research templates

- [ ] Provide `research_question`, `compare_reports`, and `trace_claim` prompts plus tool-accessible guidance for clients without prompt support.
- [ ] Let the host supply a novel plan; templates are optional and do not execute instructions embedded in source documents.
- [ ] Implement a deterministic test host that calls tools and checkpoints the BULL comparison. This tests orchestration/persistence; it is not the real-provider evaluation required in P5.
- [ ] Validate the matrix: BULL 5dd detailed analysis and entry present, 5dd hold missing; 10dd detailed analysis, entry, and hold present.
- [ ] Draft and check an example attributed answer, preserving historical report dates, technical cut-offs, distinct invalidations, unavailable fills, and a Pages used list.

## Required deliverables

| Deliverable | Planned location in `mcp-server/` |
|---|---|
| Evidence/workflow services and durable repository | `src/llm_wiki_mcp/services/{evidence,workflow}.py`, `repositories/sqlite_workflow.py` |
| Reasoning/workflow controllers, prompts, resource | Package `controllers/mcp/{reasoning,workflow}.py`, `controllers/{prompts,resources}.py` |
| State machine and workflow/citation contract documentation | `docs/workflows.md`, `contracts/`, updated `docs/tool-catalog.md` |
| Evidence, concurrency, ownership, restart scenarios | `tests/unit/test_evidence_services.py`, `tests/integration/test_workflow_transactions.py`, `test_workflow_ownership.py`, `tests/e2e/test_workflow_resume.py` |
| BULL matrix and orchestration scenario | `tests/fixtures/expected/bull-coverage.json`, `tests/e2e/test_bull_workflow.py` |

## Validation checks

| Check | Method | Pass condition and evidence |
|---|---|---|
| P3-V01 — Inventory and independence | Discover all tools; run without server model credentials. | 20 implemented names including all P2 tools; evidence/workflow calls need no model-provider API key or sampling. Save inventory. |
| P3-V02 — Evidence packet budgets | Assemble relevant and over-budget contexts with repeated provenance and several horizons. | Correct snapshot/citations, distinct contexts, deduplicated accepted IDs, declared omissions, and bounded serialized results. |
| P3-V03 — Comparison and citation honesty | Compare missing/incompatible values; supply invalid spans, wrong hashes/IDs, and a structurally valid citation for an unsupported prose claim. | Invalid references fail; missing/incomparable values remain explicit; valid structure does not receive an invented semantic-support verdict. |
| P3-V04 — BULL acceptance case | Execute the discover → plan → retrieve → assess → check → finalize sequence. | Correct six-cell strategy/horizon matrix; missing 5dd hold explicit; no current-price/fill claim or merged invalidations; cited artifact includes Pages used. |
| P3-V05 — Transaction and retry safety | Race two checkpoints; retry identical and changed payloads; disconnect after a committed checkpoint. | One version transition/event per accepted mutation; stale/conflicting calls fail; retry returns committed outcome without duplicates. |
| P3-V06 — Restart and snapshot retention | Stop the server after a checkpoint, restart with the same databases, retrieve and continue; publish a newer fixture snapshot. | Same workflow ID/version/artifacts and pinned bytes survive; newer snapshot does not alter retained evidence. Save before/after records and client trace. |
| P3-V07 — State/step/budget gates | Attempt cyclic plans, skipped required steps, incomplete finalization, budget exhaustion, terminal-state mutations, and expired snapshot use. | Illegal operations fail consistently; unresolved mandatory evidence does not become completed; cancellation persists; no silent rebase. |
| P3-V08 — Owner isolation | Read/mutate workflow and resource views as another principal. | All denied without content disclosure or state change; own workflow remains accessible under its permissions. |
| P3-V09 — Audit and wiki boundaries | Compare actual call audit versus claimed checkpoints; compare original workspace hashes. | Host-reported outcomes are labeled; workflow output adds no accepted source/page; original workspace unchanged. |

## Planned validation commands

Run from `mcp-server/` after implementing the test modules. Restart tests must use actual process termination/restart and persistent test paths rather than only reconstructing in-memory objects.

```sh
mkdir -p artifacts/validation/p3
uv run --locked pytest tests/unit/test_evidence_services.py tests/integration/test_workflow_transactions.py tests/integration/test_workflow_ownership.py tests/e2e/test_workflow_resume.py tests/e2e/test_bull_workflow.py tests/contracts/test_architecture.py --junitxml=artifacts/validation/p3/tests.xml
uv run --locked ruff check src tests
uv run --locked mypy src/llm_wiki_mcp
```

Retain affected P2 tool/schema/access regressions. Save reviewed BULL output separately from deterministic test reports: structural citation validation cannot establish prose fidelity by itself.

## Completion gate and handoff

- [ ] All P3-V checks pass; a reviewer accepts the attributed BULL comparison and missing-evidence handling.
- [ ] Store the workflow transition/retry traces, restart records, BULL coverage/artifact review, inventories, and workspace hashes under `artifacts/validation/p3/`.
- [ ] Create `phase-report.json` with revision, runtime, fixtures/snapshots, each check/result/evidence path, semantic review, and outstanding host-integration work. Required checks not executed remain `NOT_RUN`.
- [ ] Hand P4 the 20-tool application, persistent workflow schema, restart tests, retention requirements, and audit/state contracts.

Any duplicate mutation, ownership leak, false citation endorsement, or lost workflow after restart blocks completion. Correct it and rerun the affected concurrency/recovery regressions.
