# Page contracts

The literal skeletons in [page-templates](../assets/page-templates/) are canonical. Replace every placeholder and use a YAML serializer where possible. Quote descriptions containing colons. Preserve unknown metadata and human-maintained content when updating.

| Type | Skeleton | Evidence and writing budget |
|---|---|---|
| `source` | [source.md](../assets/page-templates/source.md) | One full raw document; proportionate summary, normally 300–600 words, much less for a thin note |
| `entity` | [entity.md](../assets/page-templates/entity.md) | All source summaries that engage with a person, organization, tool, or concrete named thing; normally 200–500 words |
| `concept` | [concept.md](../assets/page-templates/concept.md) | All source summaries that engage with an idea/pattern; normally 200–500 words |
| `overview` | [overview.md](../assets/page-templates/overview.md) | Navigation and coverage; normally 200–400 words, no new substantive claims |

## Source extraction

Read the complete raw source, including its frontmatter and final sections. For a long document, read sequential chunks and keep concise section receipts; merge them into one faithful summary. Do not stop after an arbitrary line limit. If a read fails, leave the page incomplete and report the uncovered ranges; do not acknowledge it.

Use its H1 or filename for the title. Preserve the author's framing. Record known authors/dates only when present; absence is absence, not permission to infer them. Highlight concrete claims and meaningful limitations. Every factual claim or quote is attributed with a keyed footnote to the original. Exact quotations must match the raw text. Prefer paraphrases; do not add general background from model memory. Source pages should not contain cross-source inference unless it is separately labeled and grounded in an explicitly read summary.

The `entities` and `concepts` lists nominate only substantive engagements. Body connections use normal relative links to those candidates; existing canonical slugs and aliases take precedence. A thin source gets a thin page. For an empty source state that no knowledge was extractable, include its evidence link, and nominate no topics.

The page's `raw_file`, `content_sha256`, `source_id`, and `coverage` come from the adapter/actual reading. `limitations` is a list, possibly empty, and includes attachment warnings.

## Synthesis

Read all source pages listed for a qualifying topic in `count_mentions.py` output. Use their `source_id`s as stable provenance IDs. `source_count` must match the exact distinct-source set; list all qualifying source pages in provenance, even if one supports a conflicting framing.

Present disagreement with separate attributions. Do not blend opposing recommendations into consensus. Keep grounded claims distinct from labeled inference. Do not call related documents independent witnesses without evidence. Cite source summaries rather than opening all raw documents again; use a targeted raw check only if an extraction error is suspected, and repair its source page before continuing.

## Overview

Read source/topic metadata, counts, and a few representative summaries. Describe the actual collection and existing topic clusters. Link materialized pages, list single-source candidates, and report limitations. Avoid inventing themes that the corpus does not support. Readable navigation is the purpose; detailed claims belong on cited knowledge pages.
