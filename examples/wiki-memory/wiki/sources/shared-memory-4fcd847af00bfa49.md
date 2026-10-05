---
type: source
title: Shared agent memory
description: A server-based memory pattern for many customers that acknowledges operating
  cost and context-dependent choices.
source_id: shared-memory-4fcd847af00bfa49
corpus: memory-example
original_path: shared-memory.md
raw_file: raw/shared-memory-4fcd847af00bfa49/shared-memory.md
content_sha256: d18954582ba38def06c025803d6267f45e19aead1271859b6c4f88d44e4eff85
created: '2026-10-05T15:35:21Z'
generated:
  by: llm-wiki-markdown/codex
  at: '2026-10-05T00:00:00Z'
coverage:
  complete: true
  total_lines: 13
  ranges:
  - - 1
    - 13
limitations: []
entities: []
concepts:
- concepts/agent-memory.md
- concepts/governed-server.md
sources:
- id: shared-memory-4fcd847af00bfa49
  resource: ../../raw/shared-memory-4fcd847af00bfa49/shared-memory.md
  title: Shared agent memory
---

# Shared agent memory

<!-- BEGIN GENERATED -->
## Summary

The note recommends a governed server interface for durable memory used by many customers. Central access checks allow clients to share business logic without putting that logic on every machine. It explicitly acknowledges infrastructure cost and says a small personal collection may not justify it; the recommendation depends on users and deployment context.[^shared-memory-4fcd847af00bfa49]

## Key claims

- A governed server interface is recommended for a service used by many customers.[^shared-memory-4fcd847af00bfa49] [Passage](../../raw/shared-memory-4fcd847af00bfa49/shared-memory.md#recommendation)
- Central access checks let multiple clients share business logic without distributing it to every machine.[^shared-memory-4fcd847af00bfa49] [Passage](../../raw/shared-memory-4fcd847af00bfa49/shared-memory.md#recommendation)
- A server requires operating infrastructure and may cost more than a small personal collection justifies.[^shared-memory-4fcd847af00bfa49] [Passage](../../raw/shared-memory-4fcd847af00bfa49/shared-memory.md#limitation)
- The choice of memory architecture depends on users and deployment context.[^shared-memory-4fcd847af00bfa49] [Passage](../../raw/shared-memory-4fcd847af00bfa49/shared-memory.md#limitation)

## Connections

- [Agent Memory](../concepts/agent-memory.md)
- [Governed Server](../concepts/governed-server.md)

[^shared-memory-4fcd847af00bfa49]: [Original note](../../raw/shared-memory-4fcd847af00bfa49/shared-memory.md)
<!-- END GENERATED -->

## Human notes
