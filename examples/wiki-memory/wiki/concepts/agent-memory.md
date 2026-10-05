---
type: concept
title: Agent Memory
description: Durable memory whose storage and access pattern depend on collection
  size and who uses it.
aliases:
- durable memory
created: '2026-10-05T00:00:00Z'
generated:
  by: llm-wiki-markdown/codex
  at: '2026-10-05T00:00:00Z'
source_count: 2
sources:
- id: local-memory-015a1edd3c08060e
  resource: ../sources/local-memory-015a1edd3c08060e.md
- id: shared-memory-4fcd847af00bfa49
  resource: ../sources/shared-memory-4fcd847af00bfa49.md
---

# Agent Memory

<!-- BEGIN GENERATED -->
## Definition

Both notes discuss durable memory for assistants. One frames a small personal collection as local Markdown; the other frames a many-customer service as a governed server interface.[^local-memory-015a1edd3c08060e][^shared-memory-4fcd847af00bfa49]

## Key claims

- For a small personal collection, local Markdown and index-guided reading are the recommended pattern.[^local-memory-015a1edd3c08060e]
- For a service used by many customers, the server pattern centralizes access checks and shared business logic.[^shared-memory-4fcd847af00bfa49]
- Local files do not supply a shared access-control service, while servers introduce operating infrastructure.[^local-memory-015a1edd3c08060e][^shared-memory-4fcd847af00bfa49]

## Tensions

These recommendations differ in deployment context. The local-memory note addresses a personal assistant; the shared-memory note addresses many customers and explicitly concedes that a small personal collection may not justify a server. Neither supports a universal preference for one storage pattern.[^local-memory-015a1edd3c08060e][^shared-memory-4fcd847af00bfa49]

> Synthesis: Decide who shares the memory and what access checks are needed before selecting its storage interface.

[^local-memory-015a1edd3c08060e]: [Local agent memory](../sources/local-memory-015a1edd3c08060e.md)
[^shared-memory-4fcd847af00bfa49]: [Shared agent memory](../sources/shared-memory-4fcd847af00bfa49.md)
<!-- END GENERATED -->

## Human notes
