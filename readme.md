# Markdown LLM Wiki template

This template gives an LLM agent ready-to-use instructions for turning local Markdown into a persistent, cited knowledge wiki. Copy the template, point the agent at your notes, and let it follow the ingestion workflow. The resulting files are readable in a text editor and can be versioned with Git.

The agent writes source summaries and synthesizes knowledge. Python helpers preserve evidence, track completion, count sources, generate navigation, and validate the result. Running a helper alone does not produce LLM-written knowledge.

## Start here

You need an agent that can read/write local files and run commands. Use `uv` for the helper scripts; their metadata specifies Python 3.12+ and pinned PyYAML. The first run may download the runtime/dependency. There is no model API key configuration in this template: generation uses your chosen agent harness. Subagents and Obsidian are optional.

From this repository:

```sh
cd llm-wiki-markdown-template
```

Start your agent in that directory and paste:

```text
Read .agents/skills/llm-wiki-markdown/SKILL.md and its linked contracts.
Create an LLM Wiki from tests/fixtures/notes/ in wiki-demo/.
Use corpus key memory-demo and input root tests/fixtures/notes/.
Read every source completely. Create cited source summaries, synthesize
qualifying entities/concepts, rebuild navigation, validate, and finish the run.
```

For your collection, replace the input directory, input root, corpus key, and output path. A corpus key is a stable name such as `research-notes`; keep it and the relative input root consistent on later runs. Moving the collection to another directory does not require a new key.

The prompt works without slash-command support. A harness that discovers `.agents/skills/` can load the skill directly. You can also copy `.agents/skills/llm-wiki-markdown/` into an existing project, or have the agent read its `SKILL.md` at an explicit path. Keep the whole skill directory, including scripts, references, and assets.

To inspect a finished result first, open [the example wiki](examples/wiki-memory/wiki/index.md). [The walkthrough](examples/walkthrough.md) explains its evidence, rerun checks, and queries.

## How knowledge develops

1. **Snapshot inputs.** The adapter discovers Markdown recursively and copies accepted files byte-for-byte to `raw/`. It copies supported local attachments while preserving their relative layout. Missing attachments and invalid input encoding are reported.
2. **Extract each source.** The agent reads the whole original, writes a faithful source summary, records actual line coverage, and attributes claims to the original. A completion receipt is validated before that page is acknowledged.
3. **Count substantive evidence.** Source summaries nominate canonical entities and concepts. Two distinct source IDs must engage with a topic before it earns a synthesized page. A repeated mention or identical-content alias adds no vote.
4. **Synthesize.** The agent reads the qualifying source summaries, merges supported knowledge, and retains disagreements with separate citations. Inference is labeled `Synthesis`.
5. **Build navigation and finish.** The agent updates the overview; helpers validate pages and regenerate indexes. The completion step checks evidence sets and navigation before recording a log entry and clearing pending work.

Thin notes get thin summaries. Topics discussed by only one source remain candidates; their intentionally unresolved links are warnings. Agreement among related documents is not automatically independent corroboration.

## Generated workspace

```text
wiki-demo/
  manifest.json             # portable identity, hashes, aliases, completion
  raw/<source-id>/           # immutable originals and copied attachments
    <relative-input-path>.md
  wiki/                     # Open Knowledge Format bundle root
    index.md                # generated map
    log.md                  # newest-first completed-operation history
    overview.md              # scope, navigation, gaps
    sources/
      index.md
      <source-id>.md         # individual source summaries
    entities/
      <slug>.md              # concrete people/tools/organizations
    concepts/
      <slug>.md              # synthesized ideas and patterns
```

Section indexes appear when that section contains pages. Original Markdown stays outside the bundle because it may lack OKF frontmatter. To share the summaries **with their local evidence**, copy the whole workspace. Copying only `wiki/` keeps the bundle but leaves companion raw evidence behind.

## Open Knowledge Format alignment

The template targets [OKF v0.2](https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/0b87c52c6ef999286c745e19998fdfcd03d5dbee/SPEC.md). The checked revision and fingerprint are recorded in [okf-spec.json](.agents/skills/llm-wiki-markdown/references/okf-spec.json).

Generated content is Markdown with YAML frontmatter and a nonempty `type`. Standard Markdown links identify related pages. Provenance uses `sources` entries with stable IDs; claim footnotes use those IDs. Generation metadata uses `generated.by` and `generated.at`. Root navigation declares `okf_version: "0.2"`; section indexes have no frontmatter. Logs use newest-first date groups.

This template additionally requires titles, descriptions, creation metadata, full-source coverage declarations, traceable citations, and a two-source synthesis threshold. These are producer quality rules, beyond basic OKF structure. Optional metadata and unknown fields are preserved. Generated content is not labeled human-reviewed merely because an agent wrote it. See [conventions](.agents/skills/llm-wiki-markdown/references/conventions.md) for the detailed profile.

## Identity, updates, and recovery

Source identity combines a corpus key and relative path with a safe filename hash. Different folders can contain the same basename without colliding. Exact duplicate content is recorded as an alias of one canonical source.

An unchanged completed run leaves knowledge pages, timestamps, and log unchanged. If an input changes at an already accepted identity, this release reports it and retains the previous snapshot. Automatic revisions and retirement are deferred; it never silently overwrites raw evidence.

Snapshotting and source-page completion are separate. If ingestion stops after copying a file, re-ingestion returns its source page as pending. If extraction completed but synthesis did not, `pending_tail` causes the agent to revisit qualifying pages and finish navigation. Missing or modified accepted raw evidence is blocked until its exact bytes are restored.

The manifest records page fingerprints so the agent can detect manual edits. Knowledge pages provide generated-region markers and a separate human notes section. The agent preserves unknown metadata, aliases, and notes outside the generated region; conflicting edits inside generated content need a deliberate merge. Run only one mutating workflow against a workspace at a time.

## Query your wiki

```text
Read .agents/skills/llm-wiki-markdown/SKILL.md.
Using wiki-demo/, what do my sources say about when local Markdown is
appropriate for agent memory? Follow the read-only query workflow and cite
the pages used.
```

The agent starts with indexes, then relevant synthesized pages, then source summaries. It reads a specific original only when needed. Answers distinguish source claims, inference, and missing coverage. Queries do not change the workspace or count as evidence.

## Helper commands

These commands run from the template directory. They are primarily called by the agent; absolute script paths also work from another working directory.

Snapshot inputs only:

```sh
uv run --script .agents/skills/llm-wiki-markdown/scripts/ingest_markdown.py \
  --wiki-dir wiki-demo --corpus memory-demo \
  --input-root tests/fixtures/notes --inputs tests/fixtures/notes
```

After the agent writes source pages, it acknowledges each with `--complete <source-id> --receipt <receipt.json>`. The exact JSON contract is in [sources.md](.agents/skills/llm-wiki-markdown/references/sources.md). Receipts belong outside the bundle, preferably in temporary files.

Count evidence:

```sh
uv run --script .agents/skills/llm-wiki-markdown/scripts/count_mentions.py --wiki-dir wiki-demo
```

After synthesis and overview generation, validate content before rebuilding navigation:

```sh
uv run --script .agents/skills/llm-wiki-markdown/scripts/validate_wiki.py --wiki-dir wiki-demo --no-indexes
uv run --script .agents/skills/llm-wiki-markdown/scripts/build_index_md.py --wiki-dir wiki-demo
uv run --script .agents/skills/llm-wiki-markdown/scripts/validate_wiki.py --wiki-dir wiki-demo
uv run --script .agents/skills/llm-wiki-markdown/scripts/ingest_markdown.py --wiki-dir wiki-demo --finish
```

Validate the provided example's base bundle structure:

```sh
uv run --script .agents/skills/llm-wiki-markdown/scripts/validate_wiki.py \
  --wiki-dir examples/wiki-memory/wiki --scope bundle
```

Default `workspace` validation checks structure plus template evidence, raw hashes, coverage, candidate links, topic counts, and citation identities. `bundle` scope checks base format structure and tolerates missing optional metadata or cross-link targets. Errors produce a nonzero exit; warnings are listed separately. Index generation validates first and refuses to replace handwritten indexes.

## Verification and limits

Run the 30 behavioral tests:

```sh
uv run --python 3.12 --with PyYAML==6.0.3 python -m unittest discover -s tests -v
```

The included two-source example passed end-to-end acknowledgment, synthesis, indexes, validation, and completion, with manual claim checks against its short originals. A copied template ran the standalone commands from another directory without changing the completed example. Actual workshop notes were also tested through the adapter: 5 easy snapshots, then 5 new medium snapshots, 4 unchanged identities, and 1 changed identity; unresolved image paths were surfaced. That workshop check covered snapshots, not full synthesis of all ten documents.

Validation cannot prove semantic fidelity, that every factual sentence is cited, or that declared coverage reflects an actual complete reading. The agent must read and review the sources. Supported local-link parsing covers common Markdown links, reference definitions, images, and Obsidian image embeds; arbitrary HTML embeds or Markdown extensions may require manual handling. Remote URLs are not fetched. Source revisions, external adapters, embeddings, publishing, and learning automatically from queries are outside this release.
