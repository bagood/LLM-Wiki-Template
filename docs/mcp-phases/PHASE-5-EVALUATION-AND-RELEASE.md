# P5 — Evaluation and release development plan

Status: planned; development validation has not been run. Estimated effort: **3–4 engineer-days**. Dependency: P4 complete. Parent: [MCP development plan](../MCP-DEVELOPMENT-PLAN.md). Previous: [P4](PHASE-4-DOCKER-AND-OPERATIONAL-HARDENING.md).

## Objective and scope

Prove that the Dockerized FastAPI server supports accurate, traceable agent workflows through two independent real AI host/provider integrations, meets the parent's measured quality/performance targets, and has sufficient operating/client documentation for release.

Release the existing **24-tool** scope. Evaluation findings should fix the implementation or document remaining blockers; they must not silently broaden into wiki authoring, embeddings, distributed deployment, or unqualified provider compatibility claims.

## Entry checks

- [ ] P0–P4 reports pass, including public HTTPS, real authorization, 24-tool discovery, restart/job recovery, and backup restore.
- [ ] Record the candidate revision/image digest, fixture/snapshot hashes, runtime, and supported protocol modes.
- [ ] Obtain two independent AI host/provider integrations, their models/settings/versions, and permission to run the planned evaluation workloads.
- [ ] Define benchmark hardware and an isolated test environment using the pinned stock and generic fixtures.
- [ ] Assign a reviewer for semantic fidelity, context preservation, and documented gaps.

## Implementation and evaluation sequence

### 1. Build a reviewed gold set

- [ ] Create at least **20 lexical discovery cases**, each with query, filters, relevant page IDs, relevance labels, and source-grounded rationale.
- [ ] Create agent workflow cases for BULL 5dd/10dd comparison; GPSO analysis/entry/hold linkage; terminal-return versus target-touch meaning; tactical versus structural invalidation; unresolved candidates; missing or unavailable evidence; and a nonfinancial generic OKF question.
- [ ] Specify expected facts, acceptable inferences, required citation spans, known gaps, and unacceptable claims for each case. Do not use a model-generated answer as the reference authority.
- [ ] Pin case data to fixture/snapshot hashes and separate lexical discovery scoring from prose/agent scoring.
- [ ] Implement report generation that records every case, including failures, retries, omissions, and reviewer decisions rather than only successful examples.

### 2. Test two real AI integrations

- [ ] Document each host/provider/model, protocol version, authentication path, native MCP or function-call adapter, and tool/resource/prompt support.
- [ ] Use independently implemented host/provider integrations; two SDK smoke-test clients alone do not satisfy this gate. State whether the provider and host implementations differ.
- [ ] For each integration run the same multi-call BULL case using discovery, workflow creation, retrieval/graph/provenance, comparison/coverage, checkpoint, citation check, and finalization.
- [ ] Interrupt after a durable checkpoint, start a new host conversation/client context, recover the explicit workflow ID, and complete the case.
- [ ] Demonstrate a tool-only workflow so lack of optional resource/prompt support does not prevent research.
- [ ] Test unknown/ambiguous topics, missing 5dd hold coverage, incomplete finalization, and source instructions containing an attempted prompt injection in an isolated fixture.
- [ ] Retain redacted server/host tool traces and resulting cited artifacts. Host provider credentials stay with the host/adapter; the MCP server needs none.

### 3. Verify output quality and citation fidelity

- [ ] Check every accepted artifact citation against the pinned page/raw identity, hash, and spans; record semantic support review separately.
- [ ] Review historical attribution, report date versus generation date, distinct 5dd/10dd contexts, provisional calendar/expiry claims, and missing execution/fill evidence.
- [ ] Require visible uncertainty and missing coverage where the fixture has gaps; model-generated output must not appear in accepted evidence or source counts.
- [ ] Review generic fixture output to ensure stock fields/profile rules are optional.
- [ ] Record structured citation success independently from unsupported prose, hallucinations, or misleading comparisons. An answer cannot pass simply because its citation target exists.

### 4. Run compatibility, recovery, and isolation regression

- [ ] Exercise all 24 tool schemas/results and access-filtered discovery through the deployed endpoint.
- [ ] Run modern/legacy protocol cases against real clients, including metadata/version errors and partial/domain failures.
- [ ] Reuse P2–P4 tests for access/resource parity, traversal budgets, concurrency/idempotency, container restart, stale jobs, old/expired snapshots, and restore.
- [ ] Run the complete mandatory suite once for the candidate revision; repeat affected checks after any fixes. Do not mark required unavailable integrations as skipped passes.
- [ ] Record every supported interpreter/container target. Qualify Python 3.15 only through its dedicated installation/test/container gate; otherwise keep release support on Python 3.14.

### 5. Measure performance and discovery quality

- [ ] Define recall@10 as the mean, across cases, of relevant expected page IDs retrieved in the first ten hits divided by the total relevant expected page IDs. Publish query-level values and relevance sets; do not confuse recall with hit rate.
- [ ] Measure warm server-side p95 latency separately for search, retrieval, neighbors, context packets, and subgraphs at **10 concurrent clients** on the baseline corpus.
- [ ] Use at least 100 measured calls per operation after warmup, fixed request budgets/case mix, and documented hardware. Report failures and timeouts, not just successful-response timing.
- [ ] Measure full rebuild from an empty index at least three times, documenting configuration and observed duration; require each baseline run to meet the rebuild target.
- [ ] Keep ingress/network/model latency outside local service thresholds, and report end-to-end provider timing separately. Benchmark results apply only to the measured corpus/hardware.
- [ ] Compare entire original-workspace tree hashes before and after evaluations and rebuilds; store generated reports elsewhere.

### 6. Package the release and operating handoff

- [ ] Complete client setup examples, authentication/discovery instructions, expected scope/role behavior, generic/template input guide, tool catalog, error/cursor examples, and workflow resume guide.
- [ ] Complete deployment/backup/restore/upgrade/rollback documentation and known compatibility/retention limitations.
- [ ] Produce a versioned release candidate, image digest, schema/database migration version, lock/runtime identifiers, compatibility matrix, and evaluation report.
- [ ] Review residual issues and dispositions. Required correctness, access, durability, and target failures prevent completion; explicitly change the parent acceptance target through review if a target must be revised.
- [ ] Release only the tested candidate and documented supported integrations; validate a final deployed smoke call against that exact image/revision.

## Required deliverables

| Deliverable | Planned location in `mcp-server/` |
|---|---|
| Grounded lexical/workflow cases and expected citations | `evaluations/cases/`, `evaluations/gold/` |
| Reproducible scoring/benchmark and host harnesses | `evaluations/`, `tests/e2e/test_provider_workflows.py`, `test_release_compatibility.py` |
| Results and semantic review | `artifacts/validation/p5/`, `docs/evaluation-report.md` |
| Supported host/protocol/runtime matrix and client examples | `docs/compatibility.md`, `docs/client-integration.md` |
| Versioned release and operating checklist | `docs/release-checklist.md`, `docs/operations.md`, release metadata |

## Validation checks

| Check | Method | Pass condition and evidence |
|---|---|---|
| P5-V01 — Complete inventory/regression | Run mandatory contracts, integrity, isolation, recovery, and type/lint checks on the candidate. | 24 categorized production tools with valid schemas; every required test passes with no skip/blocked/expected-failure exemption. Save test report/catalog. |
| P5-V02 — Two independent integrations | Run and resume the same research workflow through each actual host/provider against public HTTPS. | Both complete with persisted checkpoint evidence, grounded artifact, and supported auth/transport; actual host/provider versions and redacted traces recorded. |
| P5-V03 — Citation and semantic quality | Check all accepted artifact citations and review every agent case against gold spans/contexts. | All citations resolve to the pinned snapshot; no accepted case merges horizons, invents fills/current prices, hides known gaps, or counts model output as evidence. Reviewer approves semantic fidelity. |
| P5-V04 — Lexical discovery | Score the reviewed set of at least 20 cases using the documented mean recall@10 formula. | Mean recall@10 **at least 0.90**; all case relevance sets and failures published. |
| P5-V05 — Warm latency | Benchmark each operation at ten concurrent clients with documented warmup/sample counts/hardware. | Search/retrieval/neighbors p95 **below 300 ms**; bounded context/subgraph p95 **below 1 second**; latency/failure samples retained. |
| P5-V06 — Full rebuild | Build an empty baseline index three times using the release container/runtime. | Each full rebuild **below 30 seconds**; output reconciliation passes and original workspace remains byte-identical. |
| P5-V07 — Recovery and hostile input | Repeat restart, retry/conflict, stale-job, snapshot expiry, restore, unauthorized IDs, and source-injection cases. | Durable state/evidence remains correct; access/budgets hold; source instructions remain data; real provider workflow handles gaps safely. |
| P5-V08 — Supported-runtime matrix | Run installation/tests/container build for every declared supported interpreter. | All declared targets pass; Python 3.15 is not claimed supported without its qualification evidence. |
| P5-V09 — Release reproducibility and documentation | Follow clean client/deployment instructions, restore/run the tested image, and make a final protected smoke call. | Docs sufficient for a reviewer to reproduce setup/resume/restore; final endpoint serves the tested revision/image; known limitations are recorded. |

## Planned validation commands

Run from `mcp-server/` after implementing the evaluation harnesses/tests. Real-host tests read documented host access and credentials from secure runtime configuration. They must report `BLOCKED` when that access is absent, not silently substitute mocks.

```sh
mkdir -p artifacts/validation/p5
uv sync --locked --all-groups
uv run --locked ruff check src tests
uv run --locked mypy src/llm_wiki_mcp
uv run --locked pytest tests --junitxml=artifacts/validation/p5/tests.xml
uv run --locked python -m evaluations.run --cases evaluations/cases --output artifacts/validation/p5
uv run --locked python -m evaluations.benchmark --concurrency 10 --samples-per-operation 100 --rebuild-runs 3 --output artifacts/validation/p5
```

The evaluation commands are interfaces to implement in this phase. Configuration must identify the exact deployment, fixture, snapshot, hardware, and release revision; command success without those identities is insufficient evidence.

## Completion gate and release decision

- [ ] All P5-V checks meet their pass conditions; required blocked, skipped, unexecuted, or failing checks keep the release incomplete.
- [ ] Save raw/aggregate discovery and performance data, host traces/artifacts, citation/semantic reviews, complete regression reports, workspace hashes, compatibility matrix, and final smoke trace under `artifacts/validation/p5/`.
- [ ] Create `phase-report.json` with revision/image/runtime/schema/lock identifiers, fixture/snapshot hashes, each check/result/evidence path, reviewer decisions, and final release disposition. Do not include secrets.
- [ ] Verify P0–P4 evidence still applies to the released candidate or rerun checks affected by changes.
- [ ] Publish the tested release artifacts and hand off operations with a reproducible client connection and durable workflow resume example.

Completion means the parent plan's release criteria are demonstrated, including two real integrations and measured targets. Document an unresolved blocker plainly rather than reporting a partial release as successful.
