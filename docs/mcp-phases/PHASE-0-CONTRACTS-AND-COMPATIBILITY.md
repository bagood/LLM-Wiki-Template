# P0 — Contracts and compatibility development plan

Status: planned; development validation has not been run. Estimated effort: **2–3 engineer-days**. Dependency: none. Parent: [MCP development plan](../MCP-DEVELOPMENT-PLAN.md). Next: [P1 — Repository and index](PHASE-1-REPOSITORY-AND-INDEX.md).

## Objective and scope

Establish the implementation contracts and prove that the selected Python/MCP SDK combination works inside FastAPI. This phase succeeds when a real MCP client calls a development probe over HTTP, the architecture boundaries are enforced, and the remaining phases have unambiguous schemas and acceptance fixtures.

Deliver a small protocol spike and project foundation. The production tool inventory is defined here but implemented in P2–P4; do not publish placeholder implementations as working production tools. Wiki authoring, embeddings, distributed deployment, and server-hosted model inference remain outside the initial release.

## Entry checks

- [ ] Read the parent plan's requirements, tool catalog, input profiles, and release targets.
- [ ] Record the existing workspace baseline: 28 completed sources, 12 entities, 11 concepts, one overview, and three unresolved candidate targets represented by six warnings.
- [ ] Identify an implementation owner and reviewer; record target host/provider integrations and the planned authorization/hosting services, including dependencies still unavailable.
- [ ] Confirm that development evidence and generated databases will be stored outside the original wiki.

## Implementation sequence

### 1. Initialize the Python project

- [ ] Create `mcp-server/` with `pyproject.toml`, `.python-version`, `uv.lock`, `src/llm_wiki_mcp/`, and the test directories in the parent plan.
- [ ] Select and record the exact stable Python 3.14 patch and official MCP SDK v2 patch; install FastAPI, Uvicorn, Pydantic, settings, parser, and development dependencies through the lockfile.
- [ ] Set `requires-python = ">=3.14,<3.15"`. Document a separate Python 3.15 qualification branch/job; widening interpreter support requires passing installation, tests, and container qualification later.
- [ ] Configure Ruff, a type checker, pytest, and a CI job that installs from the lockfile and checks the project on Python 3.14.

### 2. Record architecture decisions and boundaries

- [ ] Write architecture decision records for layered dependencies, SDK mounting, generic versus template profiles, SQLite/FTS5, snapshots, and provider-independent execution.
- [ ] Define repository interfaces for pages/raw evidence, search/graph snapshots, workflows, jobs, and audit events. Domain models and interfaces must not import controller or transport modules.
- [ ] Create an application factory and dependency container. Services receive repository interfaces; MCP controllers resolve dependencies explicitly rather than assuming FastAPI `Depends` runs inside the mounted SDK app.
- [ ] Define the principal/access interface, development test principals, per-wiki authorization, workflow ownership, and future token-verifier injection. P4 replaces the test identity source with production authorization.
- [ ] Add an import-boundary check that inspects the real package imports and fails on forbidden dependencies.

### 3. Freeze the public contracts

- [ ] Define typed input/output schemas for all **24** named production tools and the seven categories in the parent catalog.
- [ ] Document the response payload, portable page/evidence URIs, citation identity and spans, warnings, truncation, cursor binding, and typed errors.
- [ ] Specify which operations require `wiki_id`, `snapshot_id`, ownership, expected workflow version, and idempotency keys. `wiki_list` must work without knowing a wiki ID.
- [ ] Define an optional `workflow_id` association for research calls, activated with P3. Associated calls must validate ownership and the pinned snapshot and be counted/audited by the server; unrelated reads must not be represented as verified workflow activity.
- [ ] Define profile-specific validation separately from base OKF conformance. Generic provenance IDs are scoped to their declaring document unless an explicit identity mapping exists.
- [ ] Define workflow states, legal transitions, mandatory steps, incomplete finalization, budgets, scope reduction, expiry, and restart semantics before implementing persistence.
- [ ] Record default/hard budgets from the parent plan and a rule that trimming preserves citations and advertises omitted content.

### 4. Prove FastAPI/MCP compatibility

- [ ] Register a deterministic development-only probe such as `dev_protocol_probe`; give it a typed request and structured/text result. It must not appear in the eventual production catalog.
- [ ] Create the MCP ASGI app before referencing its transport manager, and enter that manager from FastAPI's lifespan.
- [ ] Choose one canonical public MCP URL; test its path and trailing slash without depending on POST redirects. Avoid a duplicated `/mcp/mcp` path.
- [ ] Run a real Uvicorn process and connect with the official SDK client using both the modern and legacy protocol behaviors selected in the parent plan.
- [ ] Verify malformed inputs, unsupported versions, header/body mismatch where applicable, and clean startup/shutdown. Keep protocol parsing inside the SDK.
- [ ] Run the spike with no model-provider credentials; no source instructions or local wiki files are executed.

### 5. Prepare acceptance fixtures

- [ ] Capture a documented, immutable test copy of the stock-analysis workspace with a tree-hash manifest, source identities, expected counts, candidate targets, and the five BULL source IDs.
- [ ] Define a minimal nonfinancial OKF bundle with a `type`-only document, an unknown type/field, an external provenance URI, reserved navigation, and a missing link.
- [ ] Add small fixtures for malformed YAML, duplicate keys, Unicode links, aliases, navigation hubs, and cyclic links. Mark which are valid, warnings, or errors.
- [ ] Pin expected fixtures to hashes; a future corpus change requires a reviewed fixture update rather than silently changing the expected results.

## Required deliverables

| Deliverable | Planned location |
|---|---|
| Installable foundation and application factory | `mcp-server/src/llm_wiki_mcp/` |
| Runtime/dependency lock and CI configuration | `mcp-server/pyproject.toml`, `uv.lock`, `.python-version`; repository CI |
| Architecture decisions and compatibility matrix | `mcp-server/docs/adr/`, `docs/compatibility.md` |
| Full production contract inventory and examples | `mcp-server/docs/tool-catalog.md`, `contracts/` |
| Documented baseline and generic fixture | `mcp-server/tests/fixtures/` |
| Real-client spike and boundary checks | `tests/integration/test_protocol_spike.py`, `tests/contracts/test_architecture.py`, `test_contract_inventory.py` |

Paths in this table are files to create during development, not artifacts already produced by this plan.

## Validation checks

| Check | Method | Pass condition and evidence |
|---|---|---|
| P0-V01 — Reproducible runtime | Install on a clean Python 3.14 environment from `uv.lock`; capture interpreter and dependency versions. | Installation succeeds without changing the lockfile; the selected runtime/SDK are stable releases. Save environment and lockfile hash. |
| P0-V02 — Real transport call | Start Uvicorn and make discovery/probe calls with real MCP clients for both protocol eras. | Correct schema/result in both modes; canonical endpoint works without a POST redirect. Save redacted request/response traces. |
| P0-V03 — Lifecycle and protocol failure behavior | Restart the spike; exercise malformed arguments, version errors, and metadata mismatch. | Repeated startup/shutdown succeeds; SDK errors are distinguishable from application failures; no uninitialized manager or leaked process. |
| P0-V04 — Layer isolation | Run the import-boundary check and type/lint checks. | Controllers may depend on services; services/repositories do not import controllers; domain models remain transport independent. |
| P0-V05 — Contract completeness | Compare schema inventory against the parent catalog and validate example payloads. | Exactly 24 unique production names in seven categories; input/output/error contracts, scope, and budgets documented for every tool. |
| P0-V06 — Fixture and design review | Check fixture hashes/counts and review profile, snapshot, citation, and workflow decisions. | Generic OKF does not require the stock manifest; no lost context or ambiguous evidence identity. Save reviewer findings and fixture manifest. |
| P0-V07 — Provider independence and immutability | Run the spike without model API keys and compare original wiki hashes. | Probe works; no provider API calls, wiki changes, or source execution occur. |

## Planned validation commands

Run from `mcp-server/` after the project and these tests exist. The integration test must launch a real server process; an in-process HTTP test alone does not satisfy P0-V02.

```sh
mkdir -p artifacts/validation/p0
uv sync --locked --all-groups
uv run --locked python --version
uv run --locked ruff check src tests
uv run --locked mypy src/llm_wiki_mcp
uv run --locked pytest tests/contracts/test_architecture.py tests/contracts/test_contract_inventory.py tests/integration/test_protocol_spike.py --junitxml=artifacts/validation/p0/tests.xml
```

Implement the named tests during this phase. Preserve their traces, environment report, and fixture manifest alongside the test report.

## Completion gate and handoff

- [ ] Every P0-V check passes; mandatory tests have no skips or expected-failure exemptions.
- [ ] A reviewer accepts the decisions and all contract examples resolve their ambiguities.
- [ ] Create `artifacts/validation/p0/phase-report.json` with phase, revision, runtime/SDK versions, fixture/lock hashes, each check's result and evidence path, failures, and review outcome. A missing execution record is `NOT_RUN`, never `PASS`.
- [ ] Record outstanding hosting/provider access dependencies for P4/P5 without treating the protocol spike as proof of cloud interoperability.
- [ ] Hand P1 the repository interfaces, fixture baseline, parser/profile contract, storage/snapshot decisions, and passing compatibility evidence.

If a required check fails, fix and rerun that check plus impacted regressions. P0 remains incomplete until every required gate passes.
