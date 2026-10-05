---
type: source
title: "<title>"
description: "<one-sentence source gist>"
source_id: "<source-id>"
corpus: "<corpus-key>"
original_path: "<relative-input-path>"
raw_file: "raw/<source-id>/<relative-input-path>"
content_sha256: "<sha256>"
created: "<created-ISO-datetime>"
generated: {by: "llm-wiki-markdown/<actual-model-id>", at: "<ISO-datetime>"}
coverage:
  complete: true
  total_lines: <integer>
  ranges: [[1, <integer>]]
limitations: []
entities: []
concepts: []
sources:
  - id: "<source-id>"
    resource: "../../raw/<source-id>/<URL-encoded-relative-input-path>"
    title: "<original title>"
---

# <title>

<!-- BEGIN GENERATED -->
## Summary

<Faithful summary attributed to the original>.[^<source-id>]

## Key claims

- <Specific grounded claim>.[^<source-id>]

## Connections

- [<Candidate topic>](../concepts/<canonical-slug>.md) — <substantive engagement>.

## Limitations

<Source limitations and any attachment warnings; omit this section if none.>

[^<source-id>]: [Original source](../../raw/<source-id>/<URL-encoded-relative-input-path>#<actual-heading-anchor>)
<!-- END GENERATED -->

## Human notes

