# Agentic Stock Analysis — Ingestion report

Completed on October 11, 2026 (Asia/Jakarta).

- Output workspace: `wiki-agentic-stock-analysis/`
- Start: [Wiki index](wiki/index.md)
- Scope/methodology/horizons/coverage: [Overview](wiki/overview.md)
- Stable corpus key: `agentic-stock-analysis`
- Stable input root: `agenticStockAnalysis/`
- Discovery: all 28 Markdown files recursively accepted and read completely.
- New: 28; aliases: 0; skipped: 0; changed: 0; errors: 0; blocked: 0.
- Recovered pre-existing work: 0. All 28 source summaries acknowledged; no pending sources or ingestion tail.
- Immutable originals: 28; all byte-identical to input and SHA-256 checked.
- Composition: 6 methodology, 10 detailed-analysis, 10 entry-strategy, 2 hold-strategy sources.
- Materialized: 12 entities, 11 concepts, 1 overview, 28 source summaries = 52 content pages.
- Navigation: root and all three section indexes rebuilt.
- Completion: helper `--finish` succeeded; run ID `e07d32cc801141ac`.
- Validation: valid; 0 structural errors; 0 evidence errors; 6 candidate-link warnings representing 3 single-source entities, each warned once for its body link and once for its metadata path.

The methodology files were summarized as source content. Embedded prompts were not executed; report URLs were not fetched; market data was not refreshed; no new investment recommendation was generated. Report timestamps, technical cut-offs, 5dd/10dd windows and strategy relationships are preserved. Related reports qualify by distinct accepted source identity and substantive engagement, not presumed independence. Gaps and conflicting risk conventions remain visible with separate citations.

## Materialized entities

- [bank-indonesia](wiki/entities/bank-indonesia.md) — 10 distinct source IDs.
- [bksl](wiki/entities/bksl.md) — 2 distinct source IDs.
- [bnbr](wiki/entities/bnbr.md) — 2 distinct source IDs.
- [bull](wiki/entities/bull.md) — 5 distinct source IDs.
- [epac](wiki/entities/epac.md) — 2 distinct source IDs.
- [federal-reserve](wiki/entities/federal-reserve.md) — 10 distinct source IDs.
- [gpso](wiki/entities/gpso.md) — 3 distinct source IDs.
- [hmsp](wiki/entities/hmsp.md) — 2 distinct source IDs.
- [hrta](wiki/entities/hrta.md) — 2 distinct source IDs.
- [icbp](wiki/entities/icbp.md) — 2 distinct source IDs.
- [mina](wiki/entities/mina.md) — 2 distinct source IDs.
- [vktr](wiki/entities/vktr.md) — 2 distinct source IDs.

## Materialized concepts

- [catalyst-and-corporate-action-risk](wiki/concepts/catalyst-and-corporate-action-risk.md) — 18 distinct source IDs.
- [confirmation-and-participation](wiki/concepts/confirmation-and-participation.md) — 28 distinct source IDs.
- [entry-strategy-methodology](wiki/concepts/entry-strategy-methodology.md) — 12 distinct source IDs.
- [execution-state-evidence](wiki/concepts/execution-state-evidence.md) — 18 distinct source IDs.
- [fixed-session-horizons](wiki/concepts/fixed-session-horizons.md) — 28 distinct source IDs.
- [hold-strategy-methodology](wiki/concepts/hold-strategy-methodology.md) — 4 distinct source IDs.
- [risk-reward-screening](wiki/concepts/risk-reward-screening.md) — 18 distinct source IDs.
- [tactical-vs-structural-invalidation](wiki/concepts/tactical-vs-structural-invalidation.md) — 28 distinct source IDs.
- [terminal-scenario-returns](wiki/concepts/terminal-scenario-returns.md) — 26 distinct source IDs.
- [trusted-technical-data](wiki/concepts/trusted-technical-data.md) — 12 distinct source IDs.
- [upside-analysis-methodology](wiki/concepts/upside-analysis-methodology.md) — 12 distinct source IDs.

## Remaining candidates

- `bksldrcv6a` — 1 substantive accepted source ID; no entity page created. Evidence: [bksl-c2ef0f5604a2a67a](wiki/sources/bksl-c2ef0f5604a2a67a.md).
- `freeport-indonesia` — 1 substantive accepted source ID; no entity page created. Evidence: [hrta-30a4845bd9a6638a](wiki/sources/hrta-30a4845bd9a6638a.md).
- `tjokro-group` — 1 substantive accepted source ID; no entity page created. Evidence: [gpso-d737030d107af0ac](wiki/sources/gpso-d737030d107af0ac.md).

## Operational records

- [Discovery receipt](ingestion-reports/2026-10-11-discovery.json)
- [Topic evidence sets](ingestion-reports/2026-10-11-topic-evidence.json)
- [Validation result](ingestion-reports/2026-10-11-validation.json)
- [Completion result](ingestion-reports/2026-10-11-completion.json)
- [Stable collection identifiers](collection.json)

## Later runs

Reuse the same corpus key and input root (including when ingesting a subset):

```sh
uv run --script .agents/skills/llm-wiki-markdown/scripts/ingest_markdown.py \
  --wiki-dir wiki-agentic-stock-analysis \
  --corpus agentic-stock-analysis \
  --input-root agenticStockAnalysis \
  --inputs agenticStockAnalysis
```

Follow the skill recovery/acknowledgment/synthesis/navigation/finish tail only when work is pending. Changed bytes at an existing accepted identity retain the prior original; source revision is not automatic.
