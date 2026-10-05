# Workflows and recovery

## Ingest

1. Resolve input root, corpus key, skill directory, and output workspace. Read the data/page contracts. Use explicit user choices where supplied; otherwise choose deterministic defaults and report them.
2. Run `ingest_markdown.py --wiki-dir ... --corpus ... --input-root ... --inputs ...`. Review errors, changes, aliases, manual edits, pending records, and `pending_tail`. Report changed-input retention. Do not write over a conflicting manually edited page.
3. If no work is pending and the run was previously complete, validate the workspace. If it is valid, report an unchanged run and stop without rewriting timestamps, indexes, or log. If it is invalid, repair only the affected generated artifacts within the authorized task.
4. For every `pending` source, read its raw snapshot completely, use the source skeleton, write its source summary, verify claims against raw passages, and acknowledge the exact receipt with `--complete`. Even a valid page from a crashed run needs acknowledgment if `page_complete` is false. Do not rewrite it unnecessarily. Before writing, gather canonical topics and aliases from existing entity/concept pages and candidate lists from existing source frontmatter. Do not process `blocked` evidence as if it were a new source.
5. Reconcile candidate aliases across source pages. If any acknowledged source page changes, re-acknowledge it with a matching new receipt. Then run `count_mentions.py --wiki-dir ...`. Invalid/missing source pages must be repaired before counting succeeds.
6. For every qualifying topic, compare the evidence set and source hashes with its existing page. Create missing pages and update affected pages using the entity/concept skeleton. When recovering a pending tail, inspect **all** qualifying topics, not just the latest batch. Preserve existing creation metadata, unknown fields, aliases, and human notes. Leave unaffected pages byte-identical. Do not materialize below-threshold candidates.
7. Create/update overview only when its coverage or navigation changes. Run `validate_wiki.py --wiki-dir ... --no-indexes`. Resolve structural/evidence errors. Candidate links and draft statuses are warnings, not evidence failures.
8. Run `build_index_md.py --wiki-dir ...`, then `validate_wiki.py --wiki-dir ...`. Index rebuilding validates first and protects handwritten indexes. It does not generate knowledge prose.
9. Run `ingest_markdown.py --wiki-dir ... --finish`. It checks source acknowledgments, synthesis evidence sets, overview, and index freshness; it records an idempotent completion entry and clears `pending_tail`.
10. Report counts, paths, qualifying topic changes, candidates, unresolved input errors, and validation. A partial success must explicitly name what is still pending.

All helper calls for a workspace are serial. Optional parallel extraction may write distinct source pages, after canonical slug agreement, and return receipts; acknowledge them serially. Aggregation must wait until extraction succeeds. No helper depends on subagents or a particular model.

## Query: read-only

1. Select an existing workspace and read `wiki/index.md`, then relevant section indexes.
2. Prefer a few relevant entity/concept pages. Follow their citations to source summaries when needed.
3. Read a specific raw passage only if the summaries cannot establish the answer. Do not bulk scan raw evidence.
4. Answer with normal links to used pages, separating source claims from inference. State missing coverage or unresolved disagreement. Include a short `Pages used` list.
5. Do not update pages, manifest, indexes, or log. Questions and model answers are not new source evidence.

## Recovery cases

| Interrupted or changed state | Response |
|---|---|
| Raw exists, source page missing/invalid | Discovery returns it as pending; write/repair and acknowledge |
| Page was written, acknowledgment never ran | Validate the existing page and acknowledge it without unnecessary rewriting |
| Sources complete, synthesis/index run unfinished | `pending_tail` remains true; recount and inspect all qualifying pages, then finish |
| Generated index deleted | Rebuild from page metadata; indexes are a cache |
| Completed source file changes at original identity | Keep previous raw; report changed input; no automatic source revision |
| Raw or attachment hash changes inside workspace | Stop using affected evidence; restore exact accepted bytes from a trustworthy copy before proceeding |
| Human edited generated text | Report the conflicting page and preserve it until the intended merge is clear |
| Raw directory was renamed before manifest write crashed | Helper accepts the orphan only if all expected source/asset bytes match; otherwise reports conflict |

Do not delete a workspace as a recovery step. Automatic source retirement, evidence removal, and revision-aware resynthesis are future extensions.
