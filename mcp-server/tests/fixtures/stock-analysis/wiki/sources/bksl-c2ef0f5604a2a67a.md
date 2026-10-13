---
type: source
title: BKSL — Detailed Analysis — 10dd
description: 10dd detailed-analysis BKSL report with dated conditions and limitations.
source_id: bksl-c2ef0f5604a2a67a
corpus: agentic-stock-analysis
original_path: detailedAnalysisResults/10dd/BKSL.md
raw_file: raw/bksl-c2ef0f5604a2a67a/detailedAnalysisResults/10dd/BKSL.md
content_sha256: 838bdab0471ad3bf32b86e93752e473da591130f912c7d70e7ab1a4db8c684fe
created: '2026-10-11T01:00:32Z'
generated:
  by: llm-wiki-markdown/gpt-6
  at: '2026-10-11T01:06:44.699886Z'
coverage:
  complete: true
  total_lines: 805
  ranges:
  - - 1
    - 805
limitations:
- Historical report claims and recommendations only; remote references were not fetched
  or independently verified during wiki creation. No later market observations or
  execution fills are established.
- Only one raw OHLCV bar is described; the separate original technical JSON is not
  present as an independently ingested artifact. Foreign/non-regular flow and adjustment
  metadata are unavailable.
entities:
- entities/bksl.md
- entities/bank-indonesia.md
- entities/federal-reserve.md
- entities/bksldrcv6a.md
concepts:
- concepts/fixed-session-horizons.md
- concepts/terminal-scenario-returns.md
- concepts/confirmation-and-participation.md
- concepts/tactical-vs-structural-invalidation.md
- concepts/trusted-technical-data.md
- concepts/upside-analysis-methodology.md
- concepts/catalyst-and-corporate-action-risk.md
sources:
- id: bksl-c2ef0f5604a2a67a
  resource: ../../raw/bksl-c2ef0f5604a2a67a/detailedAnalysisResults/10dd/BKSL.md
  title: BKSL — Detailed Analysis — 10dd
report_context:
  document_role: analysis-result
  strategy_type: detailed-analysis
  forecast_horizon_sessions: 10
  forecast_horizon_label: 10dd
  ticker: BKSL
  exchange: IDX
  report_generated_on: 25 September 2026, 13:24 WIB (UTC+7)
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
  - '**Analysis timestamp:** 25 September 2026, 13:24 WIB'
  - '**Forecast end:** 9 October 2026 regular close'
  - '**Calendar status:** Verified against the published IDX 2026 schedule; unexpected
    closures announced later would require rebuilding the schedule.'
  - '**News research cut-off:** 25 September 2026, approximately 13:24 WIB'
  - '**Forecast expiry:** Regular close on 9 October 2026; it must not be extended
    without a new analysis and updated completed-session data.'
---

# BKSL — Detailed Analysis — 10dd

<!-- BEGIN GENERATED -->
## Summary

Financial claims and recommendations below are attributed to this September 25, 2026 report and its supplied September 24 technical snapshot. They are preserved historical claims, forecasts and conditions, not current market facts.[^bksl-c2ef0f5604a2a67a]

The report rates BKSL Neutral/Wait with low-to-moderate confidence at IDR 66. Aroon oscillator −92, bearish SuperTrend/Vortex and negative 5/10/20-day momentum establish downside bias. Improving MACD/PVO histograms and modest OBV/ADL increases offer limited stabilization. Volume Ratio 20D 0.6271, CMF −0.1685, falling MFI and a 1.7234 short/medium volatility ratio weaken reversal reliability.[^bksl-c2ef0f5604a2a67a]

Session-10 scenarios are bull IDR 72–78 at 25%, base IDR 64–70 at 45%, and bear IDR 57–63 at 30%. Representative gross expected return is about +1.36%; weighted endpoints are −3.18% to +5.91%. Probabilities are subjective and scenarios use encoded lows/highs and supplied features rather than online targets.[^bksl-c2ef0f5604a2a67a]

The report identifies an August operational newsletter and a September substitution-repo ownership transaction, explicitly single-source and not necessarily bullish conviction. BKSLDRCV6A has a September 29 final trading date and October 2 exercise date; the report distinguishes this cash-settled securities-firm warrant from BKSL share issuance and dilution. No strong company catalyst overrides bearish technicals; restrictive BI/Fed conditions are property-financing headwinds.[^bksl-c2ef0f5604a2a67a]

The conditional entry area is IDR 64–66 after rejection of 63–64 and improving flow. Cleaner confirmation is a close above 69. A close below about 63 invalidates the thesis; 57 is a separate, wide deeper reference with ambiguous ATR-stop semantics. Profit zones are 69–72 and 75–78. Illustrative 65/63/72 economics are 3.5:1 before costs and gaps.[^bksl-c2ef0f5604a2a67a]

The report attributes a September 23 BI hold at 5.75% to currency stabilization, while restrictive rates constrain mortgages/developer funding. It attributes a September 16 Fed increase to tighter capital flows and property-sector risk appetite; the global connection is indirect.[^bksl-c2ef0f5604a2a67a]

## Report timing and horizon

- Ticker: BKSL; strategy: detailed-analysis; horizon: 10dd (10 sessions).[^bksl-c2ef0f5604a2a67a]
- Report generated on: 25 September 2026, 13:24 WIB (UTC+7).[^bksl-c2ef0f5604a2a67a]
- **Analysis timestamp:** 25 September 2026, 13:24 WIB[^bksl-c2ef0f5604a2a67a]
- **Forecast end:** 9 October 2026 regular close[^bksl-c2ef0f5604a2a67a]
- **Calendar status:** Verified against the published IDX 2026 schedule; unexpected closures announced later would require rebuilding the schedule.[^bksl-c2ef0f5604a2a67a]
- **News research cut-off:** 25 September 2026, approximately 13:24 WIB[^bksl-c2ef0f5604a2a67a]
- **Forecast expiry:** Regular close on 9 October 2026; it must not be extended without a new analysis and updated completed-session data.[^bksl-c2ef0f5604a2a67a]
- Forecast session dates (WIB): 2026-09-28, 2026-09-29, 2026-09-30, 2026-10-01, 2026-10-02, 2026-10-05, 2026-10-06, 2026-10-07, 2026-10-08, 2026-10-09.[^bksl-c2ef0f5604a2a67a]

## Connections

- [BKSL — PT Sentul City Tbk](../entities/bksl.md) — named subject discussed in this source.[^bksl-c2ef0f5604a2a67a]
- [Bank Indonesia in the dated reports](../entities/bank-indonesia.md) — named subject discussed in this source.[^bksl-c2ef0f5604a2a67a]
- [Federal Reserve in the dated reports](../entities/federal-reserve.md) — named subject discussed in this source.[^bksl-c2ef0f5604a2a67a]
- [BKSLDRCV6A structured warrant](../entities/bksldrcv6a.md) — named subject discussed in this source.[^bksl-c2ef0f5604a2a67a]
- [Fixed trading-session horizons](../concepts/fixed-session-horizons.md) — methodology requirement or report application summarized above.[^bksl-c2ef0f5604a2a67a]
- [Terminal scenario returns and probability limits](../concepts/terminal-scenario-returns.md) — methodology requirement or report application summarized above.[^bksl-c2ef0f5604a2a67a]
- [Confirmation and participation](../concepts/confirmation-and-participation.md) — methodology requirement or report application summarized above.[^bksl-c2ef0f5604a2a67a]
- [Tactical and structural invalidation](../concepts/tactical-vs-structural-invalidation.md) — methodology requirement or report application summarized above.[^bksl-c2ef0f5604a2a67a]
- [Trusted technical-data contract](../concepts/trusted-technical-data.md) — methodology requirement or report application summarized above.[^bksl-c2ef0f5604a2a67a]
- [Upside-analysis methodology](../concepts/upside-analysis-methodology.md) — methodology requirement or report application summarized above.[^bksl-c2ef0f5604a2a67a]
- [Catalysts and corporate-action risk](../concepts/catalyst-and-corporate-action-risk.md) — methodology requirement or report application summarized above.[^bksl-c2ef0f5604a2a67a]

## Related reports

- [BKSL — entryStrategyResults — 10dd](bksl-7eacfc7741e851d3.md)

> Synthesis: Related reports reuse the same ticker analysis context; distinct source IDs enable traceable comparison but do not establish independent market corroboration.

## Limitations

- Historical report claims and recommendations only; remote references were not fetched or independently verified during wiki creation. No later market observations or execution fills are established.
- Only one raw OHLCV bar is described; the separate original technical JSON is not present as an independently ingested artifact. Foreign/non-regular flow and adjustment metadata are unavailable.[^bksl-c2ef0f5604a2a67a]

[^bksl-c2ef0f5604a2a67a]: [Immutable original](../../raw/bksl-c2ef0f5604a2a67a/detailedAnalysisResults/10dd/BKSL.md)

<!-- END GENERATED -->

## Human notes
