# Workflow contract v1.0

P0 specifies these rules; P3 implements persistence/services.

| State | Allowed next states |
|---|---|
| created | running, failed, cancelled |
| running | waiting_for_input, completed, failed, cancelled |
| waiting_for_input | running, failed, cancelled |
| completed, failed, cancelled | none |

A template expands to a step DAG before create is committed. Explicit plans need
unique IDs, existing dependencies, and no cycles. New steps are pending with zero
attempts; the application validates DAGs with `validate_step_dag`. Starting a step
requires all dependencies completed or explicitly waived. Mandatory steps cannot
be skipped. Completion requires validated artifact references and no unresolved
required evidence. Skipped mandatory steps yield MANDATORY_STEP_INCOMPLETE.

Finalization with completed steps but missing required evidence returns an
`incomplete` result, names gaps, and moves running to waiting_for_input. It retains
the submitted answer as an artifact without falsely accepting its citations. To
finalize again, resume to running, resolve the gaps, and supply the current version.
Explicit scope reduction records a reason, named waived steps/removed requirements,
and a durable event; it never erases the prior constraints or unresolved findings.

Create/get/checkpoint/finalize/cancel require `wiki_id`. Only create chooses a
snapshot; subsequent calls use the workflow's pinned snapshot. Get, mutations,
and associated research require the owner, in addition to wiki grants. Mutations
require workflow:write plus wiki:read, expected_version, and an idempotency key
(create has no expected version). Jobs require index:admin and a per-wiki grant.

Attempt increments occur when a step starts. Server calls (including failed
associated research), elapsed wall time from creation, traversed nodes, and
returned UTF-8 bytes are server-observed. Exhaustion yields BUDGET_EXCEEDED and
requires an explicit reduction that fits the remaining budget or cancellation;
clients cannot reset usage. Defaults/hard caps: calls 100/1000; attempts per step
3/10; elapsed seconds 3600/86400; bytes 1 MiB/16 MiB; traversed nodes 1000/10000.
Optional token/cost limits and usage are always host-reported and unverified.

Expiry defaults to one day, with 60 seconds minimum and 30 days maximum. An expired
workflow rejects research/checkpoint/finalize with WORKFLOW_EXPIRED; get remains
available for owner inspection and cancellation remains allowed. An expiry worker
records failed state and the reason. Snapshot expiry is separately SNAPSHOT_EXPIRED.
Active workflows retain required snapshot bytes. Reopening expired/terminal work
requires a new explicit create and audit reference to the previous workflow; no
automatic repinning or mutation of history occurs.

Process restart recovers the last committed workflow/version/receipt. Resume is
get then checkpoint on the same ID. Never rely on an MCP session for persistence.
Checkpoints store findings, decisions, citations, gaps, and concise answer artifacts,
not private chain-of-thought. Call auditing and checkpoint assertions are separate.
