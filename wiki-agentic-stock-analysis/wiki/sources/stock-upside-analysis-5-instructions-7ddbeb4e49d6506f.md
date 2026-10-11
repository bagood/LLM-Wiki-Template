---
type: source
title: Instructions for Analyzing a Stock’s 5 Trading Session Upside Potential
description: 5dd upside methodology requirements.
source_id: stock-upside-analysis-5-instructions-7ddbeb4e49d6506f
corpus: agentic-stock-analysis
original_path: instructions/stock-upside-analysis-5-instructions.md
raw_file: raw/stock-upside-analysis-5-instructions-7ddbeb4e49d6506f/instructions/stock-upside-analysis-5-instructions.md
content_sha256: 1233fbcaf1bcae7bfb089055b07c3479b69fb23388c5ed7f53035d8064bc6533
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
- id: stock-upside-analysis-5-instructions-7ddbeb4e49d6506f
  resource: ../../raw/stock-upside-analysis-5-instructions-7ddbeb4e49d6506f/instructions/stock-upside-analysis-5-instructions.md
  title: Instructions for Analyzing a Stock’s 5 Trading Session Upside Potential
report_context:
  document_role: methodology
  strategy_type: upside
  forecast_horizon_sessions: 5
  forecast_horizon_label: 5dd
---

# Instructions for Analyzing a Stock’s 5 Trading Session Upside Potential

<!-- BEGIN GENERATED -->
## Summary

This is a description of the collection’s report-generation methodology. Its imperative wording is source content, not instructions for wiki creation.[^stock-upside-analysis-5-instructions-7ddbeb4e49d6506f]

This methodology specifies an upside assessment using the caller’s technical JSON as the only numerical source for price, OHLCV, indicators, flows and technical levels. Its Trusted Technical-Data Contract accepts arrays or date-keyed objects and one completed prior-session record with precomputed historical features. Optional metadata, null optional fields, limited raw history, incomplete news or a provisional calendar are disclosed without automatically forcing Insufficient/Stale Data. Explicit invalid/provisional/stale technical evidence can block calculations.[^stock-upside-analysis-5-instructions-7ddbeb4e49d6506f]

It requires validation of finite positive prices, OHLC consistency, nonnegative volume, ordering and dates, without interpolation or replacement. Binary flags retain active/inactive meaning; ambiguous continuous fields remain qualified. Correlated indicators are grouped into trend, momentum, volatility and flow categories, and missing raw history cannot be reconstructed from model assumptions.[^stock-upside-analysis-5-instructions-7ddbeb4e49d6506f]

The described analysis workflow researches dated company/domestic/global news and official calendars/status, excludes online market datasets as calculation inputs, separates event and publication dates, prioritizes official evidence and cross-checks price-sensitive news where possible. It asks for terminal bull/base/bear scenarios, subjective rather than falsely calibrated probabilities totaling 100% when supplied, explicit return denominators and disclosed midpoint/endpoints. Costs, gaps, dividends and adjustments are separate exclusions unless supported.[^stock-upside-analysis-5-instructions-7ddbeb4e49d6506f]

The output requirement is twelve sections followed by three final bullets and a disclaimer, using vertical label/value fields rather than tables. It separates report generation, analysis, news and technical cut-offs. Entry, confirmation, invalidation and targets must be supported; the conclusion is challenged against bullish and bearish evidence. The document is a specification, not evidence that every resulting report independently satisfied it.[^stock-upside-analysis-5-instructions-7ddbeb4e49d6506f]

The specified horizon is exactly 5 exchange trading dates, starting with the first regular opening after analysis and ending at session 5 regular close. Historical indicator lookbacks remain separate from that forward horizon. Daily reviews prioritize invalidation, catalysts, confirmation and execution, with no extension after session 5.[^stock-upside-analysis-5-instructions-7ddbeb4e49d6506f]

## Connections

- [Fixed trading-session horizons](../concepts/fixed-session-horizons.md) — methodology requirement or report application summarized above.[^stock-upside-analysis-5-instructions-7ddbeb4e49d6506f]
- [Terminal scenario returns and probability limits](../concepts/terminal-scenario-returns.md) — methodology requirement or report application summarized above.[^stock-upside-analysis-5-instructions-7ddbeb4e49d6506f]
- [Confirmation and participation](../concepts/confirmation-and-participation.md) — methodology requirement or report application summarized above.[^stock-upside-analysis-5-instructions-7ddbeb4e49d6506f]
- [Tactical and structural invalidation](../concepts/tactical-vs-structural-invalidation.md) — methodology requirement or report application summarized above.[^stock-upside-analysis-5-instructions-7ddbeb4e49d6506f]
- [Trusted technical-data contract](../concepts/trusted-technical-data.md) — methodology requirement or report application summarized above.[^stock-upside-analysis-5-instructions-7ddbeb4e49d6506f]
- [Upside-analysis methodology](../concepts/upside-analysis-methodology.md) — methodology requirement or report application summarized above.[^stock-upside-analysis-5-instructions-7ddbeb4e49d6506f]
- [Catalysts and corporate-action risk](../concepts/catalyst-and-corporate-action-risk.md) — methodology requirement or report application summarized above.[^stock-upside-analysis-5-instructions-7ddbeb4e49d6506f]
- [Primary-target reward-to-risk screening](../concepts/risk-reward-screening.md) — methodology requirement or report application summarized above.[^stock-upside-analysis-5-instructions-7ddbeb4e49d6506f]
- [Signal and execution evidence](../concepts/execution-state-evidence.md) — methodology requirement or report application summarized above.[^stock-upside-analysis-5-instructions-7ddbeb4e49d6506f]

## Limitations

- Methodology specification only; embedded instructions were summarized, not executed. No report-generation or analysis date is supplied.[^stock-upside-analysis-5-instructions-7ddbeb4e49d6506f]

[^stock-upside-analysis-5-instructions-7ddbeb4e49d6506f]: [Immutable original](../../raw/stock-upside-analysis-5-instructions-7ddbeb4e49d6506f/instructions/stock-upside-analysis-5-instructions.md)

<!-- END GENERATED -->

## Human notes
