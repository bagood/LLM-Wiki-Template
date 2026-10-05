# Data and ownership conventions

## Format boundary

`<workspace>/wiki/` is the OKF bundle. `<workspace>/raw/` and `manifest.json` are companion evidence and operational state, outside that bundle. Original inputs are allowed to have no frontmatter. Distribute the whole workspace to preserve local evidence; bundle-only distribution retains navigation and summaries but may lack their raw originals.

The format reference is [OKF SPEC v0.2](https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/main/SPEC.md), checked 2026-10-05. `okf-spec.json` alongside this file records the upstream revision. The following is our producer profile, not a replacement spec:

| Base format structure | Template quality rules |
|---|---|
| UTF-8 Markdown and YAML; non-reserved pages have `type` | Every content page has title, description, creation time, and generation actor/time |
| `index.md` and `log.md` are reserved | Rebuild indexes deterministically; record completed operations in the bundle log |
| Paths identify knowledge documents | Source IDs identify immutable evidence; display slugs identify canonical topics |

Use normal Markdown links. Relative links with `.md` work in text viewers and move with the workspace. URL-encode spaces, parentheses, Unicode, and `#` in filenames, leaving path separators intact. Resolve `/...` against the `wiki/` bundle root, not the filesystem root. YAML path fields `entities` and `concepts` use literal canonical bundle-relative paths such as `concepts/mcp.md`; they are custom extensions, not Markdown links. No Obsidian syntax is required in generated pages.

Each `sources` entry carries a stable `id` and page-relative `resource`. A source page links to its original at `../../raw/<id>/<relative-file>.md`; a synthesis page links to `../sources/<id>.md`. Body footnotes use the same IDs. Footnote text contains a normal link with a heading fragment when useful. Citation targets must exist; only topics declared in candidate lists may remain unresolved.

Times are timezone-aware ISO datetimes, normally UTC ending in `Z`. Preserve `created`. Change `generated.at` only when content meaningfully changes. Use an honest actor such as `llm-wiki-markdown/<actual-model-id>`; no invented human verification or authority. Unknown frontmatter and supported optional metadata survive updates. Do not add `verified` unless an actual verification event occurred.

## Evidence and identity

The helper computes source IDs from `(corpus key, normalized relative input path)`, with an ASCII display prefix and 16-character hash suffix. SHA-256 of source bytes detects content equality. Two identical files at different paths are aliases of one source. Two files with the same basename but different relative paths are separate identities when their content differs. Changed bytes at an existing identity are reported and skipped: revisions are outside this release. Renaming a changed input explicitly creates a new artifact; it is not automatic revision management.

Entity/concept pages require two distinct source IDs whose summaries substantively engage with the topic. Repeated mentions in one page still count once. Multiple documents from one author can qualify but do not establish independent corroboration. Synthesized pages, overview text, queries, attachments, and aliases never earn evidence votes.

Canonical topic slugs are nonempty ASCII kebab case. Reuse existing paths and aliases. For a new Unicode-only label use an explicit meaningful transliteration or a `topic-<hash>` fallback. Resolve synonymous candidate slugs before counting. Do not count a passing mention as substantive engagement.

## Write ownership

Raw evidence is immutable. The helper alone owns `manifest.json`, generated indexes, and completion log entries. All mutating helper invocations for one workspace are serial; do not run two orchestrators against it at once.

Knowledge pages contain one `<!-- BEGIN GENERATED -->` / `<!-- END GENERATED -->` region, plus a human notes section outside it. The agent updates the generated region and its generation-owned metadata. Preserve all unknown keys, existing aliases, and content outside that region byte-for-byte. An existing page without these markers needs explicit review before replacement.

Ingest receipts list `manual_changes` relative to hashes saved at the last completed run. Read those pages before writing. Preserve edits outside generated regions; if a person changed generated text or evidence lists, report the conflict and leave that page untouched until resolved. A failed run may also produce hash differences: compare them with the intended pending changes rather than assuming they are human edits.

The bundle log keeps previous entries while prepending a new date group. It is newest first, with plain date headings. Queries never mutate it.
