---
type: concept
title: Trusted technical-data contract
description: Collection methodology and dated report applications with separately
  attributed uncertainty.
aliases: []
created: '2026-10-11T01:09:29.185071Z'
generated:
  by: llm-wiki-markdown/gpt-6
  at: '2026-10-11T01:09:29.185071Z'
source_count: 12
sources:
- id: bksl-c2ef0f5604a2a67a
  resource: ../sources/bksl-c2ef0f5604a2a67a.md
  title: BKSL — Detailed Analysis — 10dd
- id: bnbr-a50512c7bd8186ed
  resource: ../sources/bnbr-a50512c7bd8186ed.md
  title: BNBR — Detailed Analysis — 10dd
- id: bull-270816fba3cce331
  resource: ../sources/bull-270816fba3cce331.md
  title: BULL — Detailed Analysis — 10dd
- id: bull-b65b7de46fe80d87
  resource: ../sources/bull-b65b7de46fe80d87.md
  title: BULL — Detailed Analysis — 5dd
- id: epac-8a9e4ccf50586c57
  resource: ../sources/epac-8a9e4ccf50586c57.md
  title: EPAC — Detailed Analysis — 10dd
- id: gpso-d737030d107af0ac
  resource: ../sources/gpso-d737030d107af0ac.md
  title: GPSO — Detailed Analysis — 5dd
- id: hmsp-6718bdc124e03030
  resource: ../sources/hmsp-6718bdc124e03030.md
  title: HMSP — Detailed Analysis — 10dd
- id: hrta-30a4845bd9a6638a
  resource: ../sources/hrta-30a4845bd9a6638a.md
  title: HRTA — Detailed Analysis — 5dd
- id: icbp-c79c85e00a548f9d
  resource: ../sources/icbp-c79c85e00a548f9d.md
  title: ICBP — Detailed Analysis — 5dd
- id: mina-b3a41fc7cf56b70d
  resource: ../sources/mina-b3a41fc7cf56b70d.md
  title: MINA — Detailed Analysis — 5dd
- id: stock-upside-analysis-10-instructions-510cb15a884ac7ad
  resource: ../sources/stock-upside-analysis-10-instructions-510cb15a884ac7ad.md
  title: Instructions for Analyzing a Stock’s 10 Trading Session Upside Potential
- id: stock-upside-analysis-5-instructions-7ddbeb4e49d6506f
  resource: ../sources/stock-upside-analysis-5-instructions-7ddbeb4e49d6506f.md
  title: Instructions for Analyzing a Stock’s 5 Trading Session Upside Potential
---

# Trusted technical-data contract

<!-- BEGIN GENERATED -->
## Definition

The upside-analysis methodology describes the caller-supplied JSON as authoritative previous-completed-session technical evidence. A date-keyed object or array and a single bar containing derived historical features are accepted. Missing optional definitions, adjustment basis, flow fields or history are limitations, rather than automatic Insufficient/Stale Data decisions.[^stock-upside-analysis-5-instructions-7ddbeb4e49d6506f][^stock-upside-analysis-10-instructions-510cb15a884ac7ad]

## What the reports claim

The September 25 detailed reports interpret September 24 completed bars and supplied trend, momentum, channel and flow features. ICBP and HMSP expressly discuss only one raw bar and unavailable foreign/non-regular flow. Their historical trend descriptions come from precomputed indicators rather than an independently reconstructed OHLCV series.[^icbp-c79c85e00a548f9d][^hmsp-6718bdc124e03030]

EPAC’s one-price IDR 50 bar and zero five-day realized volatility are treated as a participation/execution warning, despite acceptance of the technical payload. BULL separately qualifies the ambiguous ATR-stop feature and cannot establish a reliable executable 10dd stop from its name alone.[^epac-8a9e4ccf50586c57][^bull-270816fba3cce331]

## Boundaries

The methodology still requires finite prices, valid OHLC relationships, nonnegative volume and coherent dates; it prohibits interpolation, online replacement values and unsupported historical calculations. The two horizon variants share that input contract, but their forecast dates remain separate.[^stock-upside-analysis-5-instructions-7ddbeb4e49d6506f][^stock-upside-analysis-10-instructions-510cb15a884ac7ad]

> Synthesis: Acceptance of a technical input under the report methodology does not establish independent data verification, live freshness, liquidity or executable strategy economics. The wiki preserves what the reports accepted and the limitations they recorded.

## Evidence coverage

All 12 distinct accepted source summaries listed in provenance substantively discuss this topic. Methodology sources describe requirements; analysis-result sources describe dated applications and qualifications. Source count measures coverage, not independence.

- BKSL — Detailed Analysis — 10dd — analysis-result.[^bksl-c2ef0f5604a2a67a]
- BNBR — Detailed Analysis — 10dd — analysis-result.[^bnbr-a50512c7bd8186ed]
- BULL — Detailed Analysis — 10dd — analysis-result.[^bull-270816fba3cce331]
- BULL — Detailed Analysis — 5dd — analysis-result.[^bull-b65b7de46fe80d87]
- EPAC — Detailed Analysis — 10dd — analysis-result.[^epac-8a9e4ccf50586c57]
- GPSO — Detailed Analysis — 5dd — analysis-result.[^gpso-d737030d107af0ac]
- HMSP — Detailed Analysis — 10dd — analysis-result.[^hmsp-6718bdc124e03030]
- HRTA — Detailed Analysis — 5dd — analysis-result.[^hrta-30a4845bd9a6638a]
- ICBP — Detailed Analysis — 5dd — analysis-result.[^icbp-c79c85e00a548f9d]
- MINA — Detailed Analysis — 5dd — analysis-result.[^mina-b3a41fc7cf56b70d]
- Instructions for Analyzing a Stock’s 10 Trading Session Upside Potential — methodology.[^stock-upside-analysis-10-instructions-510cb15a884ac7ad]
- Instructions for Analyzing a Stock’s 5 Trading Session Upside Potential — methodology.[^stock-upside-analysis-5-instructions-7ddbeb4e49d6506f]

[^bksl-c2ef0f5604a2a67a]: [BKSL — Detailed Analysis — 10dd](../sources/bksl-c2ef0f5604a2a67a.md)
[^bnbr-a50512c7bd8186ed]: [BNBR — Detailed Analysis — 10dd](../sources/bnbr-a50512c7bd8186ed.md)
[^bull-270816fba3cce331]: [BULL — Detailed Analysis — 10dd](../sources/bull-270816fba3cce331.md)
[^bull-b65b7de46fe80d87]: [BULL — Detailed Analysis — 5dd](../sources/bull-b65b7de46fe80d87.md)
[^epac-8a9e4ccf50586c57]: [EPAC — Detailed Analysis — 10dd](../sources/epac-8a9e4ccf50586c57.md)
[^gpso-d737030d107af0ac]: [GPSO — Detailed Analysis — 5dd](../sources/gpso-d737030d107af0ac.md)
[^hmsp-6718bdc124e03030]: [HMSP — Detailed Analysis — 10dd](../sources/hmsp-6718bdc124e03030.md)
[^hrta-30a4845bd9a6638a]: [HRTA — Detailed Analysis — 5dd](../sources/hrta-30a4845bd9a6638a.md)
[^icbp-c79c85e00a548f9d]: [ICBP — Detailed Analysis — 5dd](../sources/icbp-c79c85e00a548f9d.md)
[^mina-b3a41fc7cf56b70d]: [MINA — Detailed Analysis — 5dd](../sources/mina-b3a41fc7cf56b70d.md)
[^stock-upside-analysis-10-instructions-510cb15a884ac7ad]: [Instructions for Analyzing a Stock’s 10 Trading Session Upside Potential](../sources/stock-upside-analysis-10-instructions-510cb15a884ac7ad.md)
[^stock-upside-analysis-5-instructions-7ddbeb4e49d6506f]: [Instructions for Analyzing a Stock’s 5 Trading Session Upside Potential](../sources/stock-upside-analysis-5-instructions-7ddbeb4e49d6506f.md)

<!-- END GENERATED -->

## Human notes
