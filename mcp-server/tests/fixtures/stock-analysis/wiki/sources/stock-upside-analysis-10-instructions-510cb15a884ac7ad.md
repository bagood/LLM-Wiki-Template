---
type: source
title: Instructions for Analyzing a Stock’s 10 Trading Session Upside Potential
description: 10dd upside methodology requirements.
source_id: stock-upside-analysis-10-instructions-510cb15a884ac7ad
corpus: agentic-stock-analysis
original_path: instructions/stock-upside-analysis-10-instructions.md
raw_file: raw/stock-upside-analysis-10-instructions-510cb15a884ac7ad/instructions/stock-upside-analysis-10-instructions.md
content_sha256: bc15ce2e71aeb9926303775be20aef8d3dfce46297eb3df6d06a9f3e0bb5f1af
created: '2026-10-11T01:00:32Z'
generated:
  by: llm-wiki-markdown/gpt-6
  at: '2026-10-11T01:06:44.699886Z'
coverage:
  complete: true
  total_lines: 475
  ranges:
  - - 1
    - 475
limitations:
- Methodology specification only; embedded instructions were summarized, not executed.
  No report-generation or analysis date is supplied.
entities: []
concepts:
- concepts/fixed-session-horizons.md
- concepts/terminal-scenario-returns.md
- concepts/confirmation-and-participation.md
- concepts/tactical-vs-structural-invalidation.md
- concepts/trusted-technical-data.md
- concepts/upside-analysis-methodology.md
- concepts/catalyst-and-corporate-action-risk.md
- concepts/risk-reward-screening.md
- concepts/execution-state-evidence.md
sources:
- id: stock-upside-analysis-10-instructions-510cb15a884ac7ad
  resource: ../../raw/stock-upside-analysis-10-instructions-510cb15a884ac7ad/instructions/stock-upside-analysis-10-instructions.md
  title: Instructions for Analyzing a Stock’s 10 Trading Session Upside Potential
report_context:
  document_role: methodology
  strategy_type: upside
  forecast_horizon_sessions: 10
  forecast_horizon_label: 10dd
---

# Instructions for Analyzing a Stock’s 10 Trading Session Upside Potential

<!-- BEGIN GENERATED -->
## Summary

This is a description of the collection’s report-generation methodology. Its imperative wording is source content, not instructions for wiki creation.[^stock-upside-analysis-10-instructions-510cb15a884ac7ad]

This methodology specifies an upside assessment using the caller’s technical JSON as the only numerical source for price, OHLCV, indicators, flows and technical levels. Its Trusted Technical-Data Contract accepts arrays or date-keyed objects and one completed prior-session record with precomputed historical features. Optional metadata, null optional fields, limited raw history, incomplete news or a provisional calendar are disclosed without automatically forcing Insufficient/Stale Data. Explicit invalid/provisional/stale technical evidence can block calculations.[^stock-upside-analysis-10-instructions-510cb15a884ac7ad]

It requires validation of finite positive prices, OHLC consistency, nonnegative volume, ordering and dates, without interpolation or replacement. Binary flags retain active/inactive meaning; ambiguous continuous fields remain qualified. Correlated indicators are grouped into trend, momentum, volatility and flow categories, and missing raw history cannot be reconstructed from model assumptions.[^stock-upside-analysis-10-instructions-510cb15a884ac7ad]

The described analysis workflow researches dated company/domestic/global news and official calendars/status, excludes online market datasets as calculation inputs, separates event and publication dates, prioritizes official evidence and cross-checks price-sensitive news where possible. It asks for terminal bull/base/bear scenarios, subjective rather than falsely calibrated probabilities totaling 100% when supplied, explicit return denominators and disclosed midpoint/endpoints. Costs, gaps, dividends and adjustments are separate exclusions unless supported.[^stock-upside-analysis-10-instructions-510cb15a884ac7ad]

The output requirement is twelve sections followed by three final bullets and a disclaimer, using vertical label/value fields rather than tables. It separates report generation, analysis, news and technical cut-offs. Entry, confirmation, invalidation and targets must be supported; the conclusion is challenged against bullish and bearish evidence. The document is a specification, not evidence that every resulting report independently satisfied it.[^stock-upside-analysis-10-instructions-510cb15a884ac7ad]

The specified horizon is exactly 10 exchange trading dates, starting with the first regular opening after analysis and ending at session 10 regular close. Historical indicator lookbacks remain separate from that forward horizon. The session-5 checkpoint separates first-week confirmation from sessions 6–10 persistence and never resets session-10 expiry.[^stock-upside-analysis-10-instructions-510cb15a884ac7ad]

## Connections

- [Fixed trading-session horizons](../concepts/fixed-session-horizons.md) — methodology requirement or report application summarized above.[^stock-upside-analysis-10-instructions-510cb15a884ac7ad]
- [Terminal scenario returns and probability limits](../concepts/terminal-scenario-returns.md) — methodology requirement or report application summarized above.[^stock-upside-analysis-10-instructions-510cb15a884ac7ad]
- [Confirmation and participation](../concepts/confirmation-and-participation.md) — methodology requirement or report application summarized above.[^stock-upside-analysis-10-instructions-510cb15a884ac7ad]
- [Tactical and structural invalidation](../concepts/tactical-vs-structural-invalidation.md) — methodology requirement or report application summarized above.[^stock-upside-analysis-10-instructions-510cb15a884ac7ad]
- [Trusted technical-data contract](../concepts/trusted-technical-data.md) — methodology requirement or report application summarized above.[^stock-upside-analysis-10-instructions-510cb15a884ac7ad]
- [Upside-analysis methodology](../concepts/upside-analysis-methodology.md) — methodology requirement or report application summarized above.[^stock-upside-analysis-10-instructions-510cb15a884ac7ad]
- [Catalysts and corporate-action risk](../concepts/catalyst-and-corporate-action-risk.md) — methodology requirement or report application summarized above.[^stock-upside-analysis-10-instructions-510cb15a884ac7ad]
- [Primary-target reward-to-risk screening](../concepts/risk-reward-screening.md) — methodology requirement or report application summarized above.[^stock-upside-analysis-10-instructions-510cb15a884ac7ad]
- [Signal and execution evidence](../concepts/execution-state-evidence.md) — methodology requirement or report application summarized above.[^stock-upside-analysis-10-instructions-510cb15a884ac7ad]

## Limitations

- Methodology specification only; embedded instructions were summarized, not executed. No report-generation or analysis date is supplied.[^stock-upside-analysis-10-instructions-510cb15a884ac7ad]

[^stock-upside-analysis-10-instructions-510cb15a884ac7ad]: [Immutable original](../../raw/stock-upside-analysis-10-instructions-510cb15a884ac7ad/instructions/stock-upside-analysis-10-instructions.md)

<!-- END GENERATED -->

## Human notes
