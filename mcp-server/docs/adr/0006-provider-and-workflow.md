# ADR 0006: Provider-independent execution and durable workflow rules

Status: proposed for owner review; workflow implementation is P3.

The host supplies model inference, planning, and interpretation. The server returns
deterministic evidence, comparisons, and durable checkpoints. No model credentials,
sampling/roots dependency, source execution, or automatic wiki authoring is needed.
Microsoft Copilot and Codex are the owner-selected host targets; actual cloud
interoperability remains a P5 gate with access and client capabilities to qualify.

Legal workflow transitions are frozen in `domain/policies.py` and described in
`workflow-contract.md`. The workflow ID persists independently of transport
sessions. A fixed development principal exercises access policy in P0; P4 replaces
it with a token verifier enforcing issuer/audience/expiry, scopes, per-wiki grants,
and ownership. The verifier is an injected protocol, not a permissive stub.

Associated research calls carry optional `workflow_id` (activated in P3). Validate
owner, wiki, pinned snapshot, expiry, and nonterminal state before execution;
atomically count actual attempted calls and append server audit events, including
failures. Host checkpoints cannot manufacture verified activity. Unassociated
reads may be operationally audited but add no workflow usage/evidence execution.

Idempotency receipts bind principal, operation, key, and canonical payload hash.
Same-key same-payload retries return the saved result; changed payloads conflict.
Optimistic versions and receipts are durable before reporting success. Model
outputs remain artifacts and never accepted source evidence.
