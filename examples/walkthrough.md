# Worked example: durable memory

Open [the finished wiki](wiki-memory/wiki/index.md) to inspect the result without running an agent. The two original documents are illustrative fixtures, not external research or performance evidence.

The [local-memory input](../tests/fixtures/notes/local-memory.md) discusses Markdown memory for a small personal assistant. The [shared-memory input](../tests/fixtures/notes/shared-memory.md) discusses a governed server for many customers. Their summaries preserve those contexts. The [Agent Memory concept](wiki-memory/wiki/concepts/agent-memory.md) presents the difference with separate citations rather than declaring one universal recommendation.

## Reproduce through an agent

Start your agent in the template directory and give it:

```text
Read .agents/skills/llm-wiki-markdown/SKILL.md and follow its linked contracts.
Create an LLM Wiki from tests/fixtures/notes/ in wiki-demo/.
Use corpus key memory-demo and input root tests/fixtures/notes/.
Read the complete sources, preserve their distinct contexts, and finish the
ingest tail, validation, indexes, and completion log.
```

Expect two source pages. If both engage with a common memory concept, it qualifies at two distinct source IDs. Narrower topics discussed by only one note stay candidates. Exact prose and topic choices may differ; verify faithfulness and evidence rather than wording.

## Check reruns and recovery

Give the same ingestion prompt again. Expect no duplicated evidence, unchanged pages, and no extra completion entry when nothing changed.

For a reversible recovery exercise, copy `wiki-demo/` to another temporary directory and remove only a generated section index there. Ask the agent to rebuild navigation. The helper should recreate the same bytes from page metadata. Keep the original workspace intact.

For source-page recovery, work in another temporary copy and remove a source summary while retaining its raw snapshot and manifest. Re-ingestion should return that record as pending rather than treating raw existence as completion. The writer must restore its summary and acknowledge a matching receipt before finishing.

## Query

```text
Using wiki-demo/, what do these notes say about when local files are appropriate
for agent memory? Follow the read-only query procedure and cite the pages used.
```

A grounded answer identifies the small personal-collection context, notes the access-control limitation, and contrasts the many-customer server context. It should not assert that files or servers always perform better. No workspace file should change.
