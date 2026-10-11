---
type: source
title: BULL — Entry Strategy — 10dd
description: 10dd entry-strategy BULL report with dated conditions and limitations.
source_id: bull-1b5fbb4a82ee07a0
corpus: agentic-stock-analysis
original_path: entryStrategyResults/10dd/BULL.md
raw_file: raw/bull-1b5fbb4a82ee07a0/entryStrategyResults/10dd/BULL.md
content_sha256: e30894569bfca52c1123e385f0ff6f9eb79d620276860f84a51d37aa4248cdb7
created: '2026-10-11T01:00:32Z'
generated:
  by: llm-wiki-markdown/gpt-6
  at: '2026-10-11T01:06:44.699886Z'
coverage:
  complete: true
  total_lines: 35
  ranges:
  - - 1
    - 35
limitations:
- Historical report claims and recommendations only; remote references were not fetched
  or independently verified during wiki creation. No later market observations or
  execution fills are established.
- Net economics and executable sizing are unavailable without supplied costs, capital,
  currency risk, tick/lot sizes and effective execution assumptions.
entities:
- entities/bull.md
concepts:
- concepts/fixed-session-horizons.md
- concepts/terminal-scenario-returns.md
- concepts/confirmation-and-participation.md
- concepts/tactical-vs-structural-invalidation.md
- concepts/entry-strategy-methodology.md
- concepts/risk-reward-screening.md
- concepts/execution-state-evidence.md
sources:
- id: bull-1b5fbb4a82ee07a0
  resource: ../../raw/bull-1b5fbb4a82ee07a0/entryStrategyResults/10dd/BULL.md
  title: BULL — Entry Strategy — 10dd
report_context:
  document_role: analysis-result
  strategy_type: entry-strategy
  forecast_horizon_sessions: 10
  forecast_horizon_label: 10dd
  ticker: BULL
  exchange: IDX
  report_generated_on: 25 September 2026, 13:33:30 WIB (UTC+7)
  technical_data_cutoff: '2026-09-24'
  forecast_session_dates:
  - '2026-09-28'
  - '2026-09-29'
  - '2026-09-30'
  - '2026-10-01'
  - '2026-10-02'
  - '2026-10-05'
  - '2026-10-06'
  - '2026-10-07'
  - '2026-10-08'
  - '2026-10-09'
  forecast_timezone: WIB (UTC+7)
  timing_as_stated:
  - '- **Source and fixed window:** BULL/IDX; analysis and news cut-off 25 September
    2026, 13:28 WIB; technical cut-off 24 September 2026. Original window is sessions
    1–10 from 28 September through 9 October 2026, with 10 sessions remaining. Expiry
    is the regular close on 9 October 2026; its exact closing time is not supplied.
    The schedule remains provisional because a definitive IDX trading calendar was
    not obtained.'
  - '- **Source and fixed window:** BULL/IDX; analysis and news cut-off 25 September
    2026, 13:28 WIB; technical cut-off 24 September 2026. Sessions 1–10 run provisionally
    from 28 September through 9 October 2026, with 10 sessions remaining. The plan
    cannot extend beyond the regular close on 9 October; the exact close time is not
    supplied.'
  - '- **Maximum holding point:** Regular close on 9 October 2026, exact time not
    supplied. Any exit condition without a confirmed fill is **Exit due / execution
    unconfirmed**.'
---

# BULL — Entry Strategy — 10dd

<!-- BEGIN GENERATED -->
## Summary

Financial claims and recommendations below are attributed to this September 25, 2026 report and its supplied September 24 technical snapshot. They are preserved historical claims, forecasts and conditions, not current market facts.[^bull-1b5fbb4a82ee07a0]

Rank 1 is No actionable strategy because a closing invalidation below IDR 380 is not an executable tactical stop, confirmation is absent and primary-target economics fail. The schedule is provisional and exact expiry time is missing. Rank 2 watches/rejects a close above 398 with improved volume, momentum and flow, then a later-session provisional limit in 398–402 capped at 402. At 402 against 380, rewards to 404 and 415 yield only 0.09:1 and 0.59:1 gross, with binary break-even rates 91.67% and 62.86%. Conditional 426 cannot justify a deficient first target. If a refreshed plan later qualifies, lack of follow-through by holding-session 3 requires exit within the original window. Tanker benefits are paired with operating/geopolitical and global-rate risks.[^bull-1b5fbb4a82ee07a0]

The report keeps signals separate from fills: Waiting is the stated cut-off condition; Armed/Triggered need fresh dated observations, Active needs explicit entry execution, and Completed needs fills closing the full position. Target touches or exit deadlines alone do not prove execution. Terminal scenario probabilities cannot establish conditional target/stop/fill probabilities, so strategy expected value is not reliably estimable. Unknown costs are not zero and capital, currency-risk, lot and execution inputs do not support a share quantity.[^bull-1b5fbb4a82ee07a0]

## Report timing and horizon

- Ticker: BULL; strategy: entry-strategy; horizon: 10dd (10 sessions).[^bull-1b5fbb4a82ee07a0]
- Report generated on: 25 September 2026, 13:33:30 WIB (UTC+7).[^bull-1b5fbb4a82ee07a0]
- **Source and fixed window:** BULL/IDX; analysis and news cut-off 25 September 2026, 13:28 WIB; technical cut-off 24 September 2026. Original window is sessions 1–10 from 28 September through 9 October 2026, with 10 sessions remaining. Expiry is the regular close on 9 October 2026; its exact closing time is not supplied. The schedule remains provisional because a definitive IDX trading calendar was not obtained.[^bull-1b5fbb4a82ee07a0]
- **Source and fixed window:** BULL/IDX; analysis and news cut-off 25 September 2026, 13:28 WIB; technical cut-off 24 September 2026. Sessions 1–10 run provisionally from 28 September through 9 October 2026, with 10 sessions remaining. The plan cannot extend beyond the regular close on 9 October; the exact close time is not supplied.[^bull-1b5fbb4a82ee07a0]
- **Maximum holding point:** Regular close on 9 October 2026, exact time not supplied. Any exit condition without a confirmed fill is **Exit due / execution unconfirmed**.[^bull-1b5fbb4a82ee07a0]
- Forecast session dates (WIB): 2026-09-28, 2026-09-29, 2026-09-30, 2026-10-01, 2026-10-02, 2026-10-05, 2026-10-06, 2026-10-07, 2026-10-08, 2026-10-09.[^bull-1b5fbb4a82ee07a0]

## Connections

- [BULL](../entities/bull.md) — named subject discussed in this source.[^bull-1b5fbb4a82ee07a0]
- [Fixed trading-session horizons](../concepts/fixed-session-horizons.md) — methodology requirement or report application summarized above.[^bull-1b5fbb4a82ee07a0]
- [Terminal scenario returns and probability limits](../concepts/terminal-scenario-returns.md) — methodology requirement or report application summarized above.[^bull-1b5fbb4a82ee07a0]
- [Confirmation and participation](../concepts/confirmation-and-participation.md) — methodology requirement or report application summarized above.[^bull-1b5fbb4a82ee07a0]
- [Tactical and structural invalidation](../concepts/tactical-vs-structural-invalidation.md) — methodology requirement or report application summarized above.[^bull-1b5fbb4a82ee07a0]
- [Entry-strategy methodology](../concepts/entry-strategy-methodology.md) — methodology requirement or report application summarized above.[^bull-1b5fbb4a82ee07a0]
- [Primary-target reward-to-risk screening](../concepts/risk-reward-screening.md) — methodology requirement or report application summarized above.[^bull-1b5fbb4a82ee07a0]
- [Signal and execution evidence](../concepts/execution-state-evidence.md) — methodology requirement or report application summarized above.[^bull-1b5fbb4a82ee07a0]

## Related reports

- [BULL — detailedAnalysisResults — 10dd](bull-270816fba3cce331.md)
- [BULL — detailedAnalysisResults — 5dd](bull-b65b7de46fe80d87.md)
- [BULL — entryStrategyResults — 5dd](bull-a75efdaf022b83d5.md)
- [BULL — holdStrategyResults — 10dd](bull-48a2a5c45588e51e.md)

> Synthesis: Related reports reuse the same ticker analysis context; distinct source IDs enable traceable comparison but do not establish independent market corroboration.

## Limitations

- Historical report claims and recommendations only; remote references were not fetched or independently verified during wiki creation. No later market observations or execution fills are established.
- Net economics and executable sizing are unavailable without supplied costs, capital, currency risk, tick/lot sizes and effective execution assumptions.[^bull-1b5fbb4a82ee07a0]

[^bull-1b5fbb4a82ee07a0]: [Immutable original](../../raw/bull-1b5fbb4a82ee07a0/entryStrategyResults/10dd/BULL.md)

<!-- END GENERATED -->

## Human notes
