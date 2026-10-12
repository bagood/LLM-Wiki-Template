# P4 — Docker and operational hardening development plan

Status: planned; development validation has not been run. Estimated effort: **3–5 engineer-days**. Dependency: P3 complete. Parent: [MCP development plan](../MCP-DEVELOPMENT-PLAN.md). Previous: [P3](PHASE-3-REASONING-AND-WORKFLOWS.md). Next: [P5](PHASE-5-EVALUATION-AND-RELEASE.md).

## Objective and scope

Package the FastAPI MCP server for Docker deployment, add two quality and two administration tools, and prove authorization, durability, health, recovery, and backup behavior. The implemented inventory reaches **24 production tools**.

Deploy one worker with local persistent volumes initially. Select the hosting platform, public hostname, and authorization service during implementation. This phase establishes a protected reachable endpoint; P5 proves actual AI cloud-host workflows and measures release targets.

## Entry checks

- [ ] P3's 20 tools, ownership/concurrency checks, and process-restart evidence pass.
- [ ] Confirm deployment platform, HTTPS hostname, DNS/ingress ownership, OAuth/OIDC issuer/audience, and test credentials/access are available.
- [ ] Define writable index/state/backup destinations, registered read-only wiki mounts, and snapshot/workflow retention.
- [ ] Preserve a copy of P3's passing workload and original-workspace hashes for container regression checks.

## Tools to implement

| Category | Tool | Required behavior |
|---|---|---|
| Quality | `wiki_validate` | Read-only bundle/profile/index findings with integrity, provenance, candidate, and index-consistency distinctions. |
| Quality | `wiki_index_status` | Authorized active snapshot, age, running/failed build status, unusable evidence, and rebuild need. |
| Administration | `admin_rebuild_index` | Persist an authorized idempotent rebuild job and return its ID without editing the wiki. |
| Administration | `admin_get_job` | Return authorized job status, diagnostics, attempts, and published snapshot. |

Hide administrative tools from nonadmin discovery and still enforce access when callers invoke their names directly. Keep quality checks available to authorized wiki readers.

## Implementation sequence

### 1. Build the production image and Compose profiles

- [ ] Create a multi-stage Dockerfile using a verified Python 3.14 slim patch/digest and locked dependencies; configure an unprivileged runtime user.
- [ ] Exclude the corpus, secrets, virtual environments, artifacts, and development dependencies from image layers with `.dockerignore` and explicit copy rules.
- [ ] Set one Uvicorn worker and a graceful shutdown interval. Bind inside the container as required, while the development profile publishes only on host `127.0.0.1`.
- [ ] Create `compose.yaml` profiles for local development and protected deployment, with separate read-only workspace, index, and workflow volumes.
- [ ] Document patch/digest refresh and Python 3.15 qualification. Do not widen runtime support until its own install/test/container matrix passes.

### 2. Implement durable rebuild jobs and quality tools

- [ ] Reuse P1 validation/build services; expose findings without mutating originals or presenting a candidate warning as a corrupted accepted source.
- [ ] Add persistent job records with wiki/owner, mode, payload hash, state, attempt, lease, heartbeat, error, and output snapshot.
- [ ] Persist before acknowledging rebuild requests; limit one publisher per wiki, with bounded retries and lease recovery after worker/container restart.
- [ ] Rebuild into staging and publish atomically. A failed job leaves the previous active snapshot usable.
- [ ] Make job execution independent of the initiating HTTP connection. Status reads must survive disconnection and restart.
- [ ] Implement internal shutdown/cancellation handling and stale-job recovery; do not claim a public job-cancel tool that is absent from the 24-tool catalog.

### 3. Integrate production authorization and isolation

- [ ] Implement protected-resource discovery and token verification for the selected issuer/audience/expiry; inject authenticated principals into MCP operations explicitly.
- [ ] Enforce `wiki:read`, `workflow:write`, `index:admin`, per-wiki access, workflow ownership, and job visibility. Document the exact role/scope mapping established in P0.
- [ ] Verify 401/403 and metadata discovery paths through ingress, including direct requests to mounted MCP handlers; FastAPI route dependencies alone are insufficient.
- [ ] Configure allowed hosts/origins, body/result limits, rate/expensive-operation budgets, and runtime secret delivery.
- [ ] Ensure token/content minimization in logs, metrics, error details, and validation traces. No model-provider key is required in the server runtime.

### 4. Add ingress, probes, and observability

- [ ] Configure public HTTPS routing to the canonical MCP path, preserving required headers and streaming responses without buffering/POST redirects.
- [ ] Keep host/origin allowlists consistent with the external hostname. Document modern/legacy support and any legacy session routing choice.
- [ ] Implement `/health/live`, `/health/ready`, and restricted `/metrics`; readiness depends on initialized storage and a usable index.
- [ ] Emit correlation IDs, tool/error/latency/truncation measurements, index age/integrity findings, workflow transitions, and job recovery metrics.
- [ ] Test graceful shutdown with in-flight reads/checkpoints and an interrupted staging build. New work must not receive false success during shutdown.

### 5. Implement backup/restore and operating documentation

- [ ] Back up workflow/job state and required retained snapshot content consistently; use a transaction-aware database backup method, not an arbitrary copy of an open database file.
- [ ] Restore to separate test volumes and validate snapshot references before resuming an existing workflow ID.
- [ ] Rebuild disposable indexes without losing durable workflow state. Treat loss of referenced retained content as a restore failure rather than silently rebasing workflows.
- [ ] Document deployment/configuration, token setup, probes, log access, rebuilds, stale jobs, volume ownership, retention, restore, upgrade/rollback, and incident diagnosis.
- [ ] Scan the runtime image and record an actionable dependency/image finding report; fix material runtime issues or document an explicit reviewed disposition before release.

## Required deliverables

| Deliverable | Planned location in `mcp-server/` |
|---|---|
| Container build and deployment configuration | `Dockerfile`, `compose.yaml`, `.dockerignore`, `.env.example` |
| Quality/admin and operational routes | Package `controllers/mcp/{quality,admin}.py`, `controllers/http/{health,admin}.py` |
| Persistent jobs, worker, authorization integration | Package `workers/index_jobs.py`, repository migrations, configured security components |
| Deployment/backup/restore guide | `docs/operations.md`, `docs/client-integration.md` |
| Container/auth/job/restore scenarios | `tests/e2e/test_container_deployment.py`, `test_remote_authorization.py`, `test_job_recovery.py`, `test_backup_restore.py` |

## Validation checks

| Check | Method | Pass condition and evidence |
|---|---|---|
| P4-V01 — Reproducible container | Build from lockfile, inspect runtime interpreter/user/layers, and scan image. | Python patch/digest recorded; lock unchanged; nonroot runtime; no corpus/secrets/dev packages copied; scan findings reviewed. Save image digest/report. |
| P4-V02 — Inventory and scopes | Discover/call tools with research, viewer, and admin principals, including direct denied calls. | Full admin inventory has 24 unique tools; restricted lists match policy; hidden admin calls remain denied; quality tools work for authorized readers. |
| P4-V03 — Mount and workflow durability | Run P3 workflow, restart/recreate container with the same volumes, and resume. | Same workflow/version/artifacts and snapshot survive; wiki mount rejects writes; full original-workspace hashes unchanged. |
| P4-V04 — Rebuild jobs | Submit duplicate requests, disconnect, terminate/restart worker mid-build, and force a build failure. | One logical idempotent job; recoverable leases/attempts; status persists; old index remains usable until atomic publication. Save job/snapshot traces. |
| P4-V05 — Remote authorization | Exercise real issuer tokens, absent/expired/wrong-audience tokens, insufficient scopes, unauthorized wiki, and other-owner IDs. | Correct 401/403/discovery behavior and no unauthorized result/state mutation through tools or resources. |
| P4-V06 — Ingress/transport | Call both supported protocol modes through public HTTPS; test origins/hosts, metadata headers, streaming, and canonical path. | Domain results correct; headers preserved; forbidden origin/host rejected; no duplicated path, buffering failure, or required redirect. |
| P4-V07 — Probe and telemetry | Simulate unavailable storage/index and inspect live/ready/metrics/logs. | Readiness fails when service unusable while liveness reflects process health; metrics protected; required signals present without tokens. |
| P4-V08 — Backup/restore | Back up state plus retained snapshots, restore into clean separate volumes, resume a saved workflow, and rebuild current index. | Restored citations and versions match original; recovery succeeds without mixing snapshots or losing durable state. Save restore transcript. |
| P4-V09 — Shutdown/limit regression | Stop during reads/checkpoint/build and exceed request/traversal/operation budgets. | Committed mutations persist; incomplete work is recoverable; no false success or budget bypass; P2/P3 integrity and ownership checks still pass. |

## Planned validation commands

Run from `mcp-server/` after creating the deployment and tests. The deployment tests own isolated Compose project names, temporary fixture mounts, and persistent test volumes; they must not remove or overwrite user volumes. Configure issuer/endpoint test access through the documented environment, not command-line tokens.

```sh
mkdir -p artifacts/validation/p4
docker compose config --quiet
docker compose build
uv run --locked pytest tests/e2e/test_container_deployment.py tests/e2e/test_remote_authorization.py tests/e2e/test_job_recovery.py tests/e2e/test_backup_restore.py --junitxml=artifacts/validation/p4/tests.xml
uv run --locked ruff check src tests
uv run --locked mypy src/llm_wiki_mcp
```

Remote authorization/ingress and restore tests are mandatory integration gates. If credentials or platform access are unavailable, mark those checks `BLOCKED` and this phase incomplete; mock results cannot stand in for their evidence.

## Completion gate and handoff

- [ ] All P4-V checks pass; no mandatory test is skipped, blocked, or only mocked.
- [ ] Save image/config hashes, inventories, authorization/ingress traces, job recovery, restart/restore proof, scan disposition, and original-workspace hashes under `artifacts/validation/p4/`.
- [ ] Create `phase-report.json` with application revision/image digest, runtime, endpoint/issuer configuration identifiers, fixture/snapshot hashes, each check/result/evidence path, and reviewer outcome; exclude credentials.
- [ ] Hand P5 the protected public endpoint, client setup, reproducible image, 24-tool inventory, operating guide, and verified recovery/backup evidence.

Lost state, bypassed access, inconsistent restored citations, or an untested public ingress blocks completion. Resolve the failure and rerun affected deployment and regression checks.
