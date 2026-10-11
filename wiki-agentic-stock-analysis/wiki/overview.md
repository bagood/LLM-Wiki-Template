---
type: overview
title: Agentic Stock Analysis — Overview
description: A dated IDX report collection with 5dd/10dd analysis, entry and hold
  methodology and results.
created: '2026-10-11T01:09:29.185071Z'
generated:
  by: llm-wiki-markdown/gpt-6
  at: '2026-10-11T01:09:29.185071Z'
total_sources: 28
total_pages: 52
corpus: agentic-stock-analysis
input_root: agenticStockAnalysis
sources:
- id: gpso-0e7ee5751fd4bce3
  resource: sources/gpso-0e7ee5751fd4bce3.md
  title: GPSO — Hold Strategy — 5dd
- id: stock-upside-analysis-5-instructions-7ddbeb4e49d6506f
  resource: sources/stock-upside-analysis-5-instructions-7ddbeb4e49d6506f.md
  title: Instructions for Analyzing a Stock’s 5 Trading Session Upside Potential
- id: stock-entry-strategy-5-instructions-51bfbec68204b2d3
  resource: sources/stock-entry-strategy-5-instructions-51bfbec68204b2d3.md
  title: Instructions for Generating a Stock Entry Strategy (5 Trading Sessions)
- id: stock-hold-strategy-10-instructions-d9a1481b76debebd
  resource: sources/stock-hold-strategy-10-instructions-d9a1481b76debebd.md
  title: Instructions for Generating a Stock Hold Strategy (10 Trading Sessions)
- id: bull-b65b7de46fe80d87
  resource: sources/bull-b65b7de46fe80d87.md
  title: BULL — Detailed Analysis — 5dd
- id: bull-270816fba3cce331
  resource: sources/bull-270816fba3cce331.md
  title: BULL — Detailed Analysis — 10dd
- id: icbp-c79c85e00a548f9d
  resource: sources/icbp-c79c85e00a548f9d.md
  title: ICBP — Detailed Analysis — 5dd
- id: epac-8a9e4ccf50586c57
  resource: sources/epac-8a9e4ccf50586c57.md
  title: EPAC — Detailed Analysis — 10dd
- id: bull-48a2a5c45588e51e
  resource: sources/bull-48a2a5c45588e51e.md
  title: BULL — Hold Strategy — 10dd
---

# Agentic Stock Analysis — Overview

<!-- BEGIN GENERATED -->
## Coverage

This collection contains 28 distinct local Markdown sources: six methodology specifications, ten detailed analyses, ten entry reports and two hold reports. Corpus key is `agentic-stock-analysis`; the stable input root is `agenticStockAnalysis/`. Source summaries cite immutable byte-identical originals in the companion `raw/` directory.

The analysis-result reports are dated September 25, 2026 and use a September 24 technical cut-off. The five-session window is September 28–October 2; the ten-session window adds October 5–9, with October 2 an intermediate checkpoint. Exact preparation times, provisional/verified calendar claims and missing close times remain report-specific; GPSO’s hold preparation clock is unavailable.[^gpso-0e7ee5751fd4bce3]

## Methodology and strategy relationships

Methodology documents describe intended upstream analysis, new-entry screening and existing-position management. Their embedded prompts were summarized, not executed. Detailed analyses accept supplied prior-session features and qualify terminal scenarios; entry reports require executable trigger/stop/target economics; hold reports evaluate remaining thesis and freshness. Provisional-calendar acceptance upstream differs from stricter downstream schedule requirements.[^stock-upside-analysis-5-instructions-7ddbeb4e49d6506f][^stock-entry-strategy-5-instructions-51bfbec68204b2d3][^stock-hold-strategy-10-instructions-d9a1481b76debebd]

Related ticker reports link directly to each other. BULL’s 5dd and 10dd price levels, forecasts and conclusions remain separate. Related reports reuse analysis context and are not presumed independent corroboration.[^bull-b65b7de46fe80d87][^bull-270816fba3cce331]

## Ticker coverage

| Ticker | 5dd reports | 10dd reports |
| --- | --- | --- |
| [BULL](entities/bull.md) | Detailed, entry | Detailed, entry, hold |
| [GPSO](entities/gpso.md) | Detailed, entry, hold | — |
| [HRTA](entities/hrta.md) | Detailed, entry | — |
| [ICBP](entities/icbp.md) | Detailed, entry | — |
| [MINA](entities/mina.md) | Detailed, entry | — |
| [BKSL](entities/bksl.md) | — | Detailed, entry |
| [BNBR](entities/bnbr.md) | — | Detailed, entry |
| [EPAC](entities/epac.md) | — | Detailed, entry |
| [HMSP](entities/hmsp.md) | — | Detailed, entry |

## Start here

- [Sources](sources/index.md) — Full-source extraction and original evidence.
- [Entities](entities/index.md) — Nine tickers, Bank Indonesia, Federal Reserve and VKTR.
- [Concepts](concepts/index.md) — Eleven methodology and report-comparison topics.
- [Fixed horizons](concepts/fixed-session-horizons.md), [reward-to-risk](concepts/risk-reward-screening.md), and [execution evidence](concepts/execution-state-evidence.md) — Context for reading the strategies.

## Health and gaps

- 28 acknowledged sources; 12 materialized entities; 11 materialized concepts; 52 content pages including this overview.
- Single-source candidates: BKSLDRCV6A, Freeport Indonesia and Tjokro Group. Their evidence remains in source summaries; no below-threshold page is materialized.
- Hold coverage exists only for GPSO 5dd and BULL 10dd. Cross-horizon coverage exists only for BULL.
- The reports describe one technical bar per analysis; independent JSON/history, current market observations, portfolio/execution inputs and realized outcomes are absent. Remote citations were not fetched or refreshed. Financial claims are dated source attributions; no new investment recommendation was generated.[^icbp-c79c85e00a548f9d][^epac-8a9e4ccf50586c57][^bull-48a2a5c45588e51e][^gpso-0e7ee5751fd4bce3]

> Synthesis: This wiki documents the collection’s reasoning and gaps, not a current market assessment or evidence of executed trades.

[^gpso-0e7ee5751fd4bce3]: [GPSO — Hold Strategy — 5dd](sources/gpso-0e7ee5751fd4bce3.md)
[^stock-upside-analysis-5-instructions-7ddbeb4e49d6506f]: [Instructions for Analyzing a Stock’s 5 Trading Session Upside Potential](sources/stock-upside-analysis-5-instructions-7ddbeb4e49d6506f.md)
[^stock-entry-strategy-5-instructions-51bfbec68204b2d3]: [Instructions for Generating a Stock Entry Strategy (5 Trading Sessions)](sources/stock-entry-strategy-5-instructions-51bfbec68204b2d3.md)
[^stock-hold-strategy-10-instructions-d9a1481b76debebd]: [Instructions for Generating a Stock Hold Strategy (10 Trading Sessions)](sources/stock-hold-strategy-10-instructions-d9a1481b76debebd.md)
[^bull-b65b7de46fe80d87]: [BULL — Detailed Analysis — 5dd](sources/bull-b65b7de46fe80d87.md)
[^bull-270816fba3cce331]: [BULL — Detailed Analysis — 10dd](sources/bull-270816fba3cce331.md)
[^icbp-c79c85e00a548f9d]: [ICBP — Detailed Analysis — 5dd](sources/icbp-c79c85e00a548f9d.md)
[^epac-8a9e4ccf50586c57]: [EPAC — Detailed Analysis — 10dd](sources/epac-8a9e4ccf50586c57.md)
[^bull-48a2a5c45588e51e]: [BULL — Hold Strategy — 10dd](sources/bull-48a2a5c45588e51e.md)

<!-- END GENERATED -->

## Human notes
