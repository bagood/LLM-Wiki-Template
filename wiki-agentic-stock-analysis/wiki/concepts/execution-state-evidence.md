---
type: concept
title: Signal and execution evidence
description: Collection methodology and dated report applications with separately
  attributed uncertainty.
aliases: []
created: '2026-10-11T01:09:29.185071Z'
generated:
  by: llm-wiki-markdown/gpt-6
  at: '2026-10-11T01:09:29.185071Z'
source_count: 18
sources:
- id: bksl-7eacfc7741e851d3
  resource: ../sources/bksl-7eacfc7741e851d3.md
  title: BKSL — Entry Strategy — 10dd
- id: bnbr-694cd85cde8d5c1b
  resource: ../sources/bnbr-694cd85cde8d5c1b.md
  title: BNBR — Entry Strategy — 10dd
- id: bull-1b5fbb4a82ee07a0
  resource: ../sources/bull-1b5fbb4a82ee07a0.md
  title: BULL — Entry Strategy — 10dd
- id: bull-48a2a5c45588e51e
  resource: ../sources/bull-48a2a5c45588e51e.md
  title: BULL — Hold Strategy — 10dd
- id: bull-a75efdaf022b83d5
  resource: ../sources/bull-a75efdaf022b83d5.md
  title: BULL — Entry Strategy — 5dd
- id: epac-6e4659ee28ddf896
  resource: ../sources/epac-6e4659ee28ddf896.md
  title: EPAC — Entry Strategy — 10dd
- id: gpso-0e7ee5751fd4bce3
  resource: ../sources/gpso-0e7ee5751fd4bce3.md
  title: GPSO — Hold Strategy — 5dd
- id: gpso-c8b53800c8dec568
  resource: ../sources/gpso-c8b53800c8dec568.md
  title: GPSO — Entry Strategy — 5dd
- id: hmsp-3b2ef84f3f7b15d1
  resource: ../sources/hmsp-3b2ef84f3f7b15d1.md
  title: HMSP — Entry Strategy — 10dd
- id: hrta-e2f2954f5612304b
  resource: ../sources/hrta-e2f2954f5612304b.md
  title: HRTA — Entry Strategy — 5dd
- id: icbp-be4bae821fb86c38
  resource: ../sources/icbp-be4bae821fb86c38.md
  title: ICBP — Entry Strategy — 5dd
- id: mina-37f439e72a0ebb94
  resource: ../sources/mina-37f439e72a0ebb94.md
  title: MINA — Entry Strategy — 5dd
- id: stock-entry-strategy-10-instructions-b62891c31dd14f64
  resource: ../sources/stock-entry-strategy-10-instructions-b62891c31dd14f64.md
  title: Instructions for Generating a Stock Entry Strategy (10 Trading Sessions)
- id: stock-entry-strategy-5-instructions-51bfbec68204b2d3
  resource: ../sources/stock-entry-strategy-5-instructions-51bfbec68204b2d3.md
  title: Instructions for Generating a Stock Entry Strategy (5 Trading Sessions)
- id: stock-hold-strategy-10-instructions-d9a1481b76debebd
  resource: ../sources/stock-hold-strategy-10-instructions-d9a1481b76debebd.md
  title: Instructions for Generating a Stock Hold Strategy (10 Trading Sessions)
- id: stock-hold-strategy-5-instructions-d8721315f9cdba99
  resource: ../sources/stock-hold-strategy-5-instructions-d8721315f9cdba99.md
  title: Instructions for Generating a Stock Hold Strategy (5 Trading Sessions)
- id: stock-upside-analysis-10-instructions-510cb15a884ac7ad
  resource: ../sources/stock-upside-analysis-10-instructions-510cb15a884ac7ad.md
  title: Instructions for Analyzing a Stock’s 10 Trading Session Upside Potential
- id: stock-upside-analysis-5-instructions-7ddbeb4e49d6506f
  resource: ../sources/stock-upside-analysis-5-instructions-7ddbeb4e49d6506f.md
  title: Instructions for Analyzing a Stock’s 5 Trading Session Upside Potential
---

# Signal and execution evidence

<!-- BEGIN GENERATED -->
## Definition

The entry specification distinguishes Waiting, Armed, Triggered, Active—healthy/warning, Invalidated and Completed. Armed/Triggered require dated observations; Active requires confirmed entry fills; Completed requires full closing fills. A completed closing signal is known only after the bar ends, so an order must be considered in a later eligible session.[^stock-entry-strategy-5-instructions-51bfbec68204b2d3][^stock-entry-strategy-10-instructions-b62891c31dd14f64]

## Evidence limits

For the September 25 report context, BNBR’s conditional support card remains Waiting despite a numerical trigger framework. GPSO’s candidate is rejected and has no dated confirmation. Their described future state transitions are rules for a possible plan, not evidence that trading occurred.[^bnbr-694cd85cde8d5c1b][^gpso-c8b53800c8dec568]

Target touches, invalidation conditions or time deadlines without exit fills mean Exit due / execution unconfirmed. A partial profit fill would leave the remaining position active. Disqualified candidates remain watch-only even if a price threshold later occurs; absent observations cannot establish that later event.[^stock-entry-strategy-5-instructions-51bfbec68204b2d3][^stock-entry-strategy-10-instructions-b62891c31dd14f64][^bull-1b5fbb4a82ee07a0]

Hold methodology similarly separates future Exit on trigger and profit-objective conditions from confirmed reduction, realized P/L or closure. BULL’s hold report finds no immediate-sale condition in its dated evidence: the close equals 380 rather than breaching the below-380 rule. GPSO’s current trigger and execution state are unknown because preparation-time freshness is unavailable.[^stock-hold-strategy-5-instructions-d8721315f9cdba99][^stock-hold-strategy-10-instructions-d9a1481b76debebd][^bull-48a2a5c45588e51e][^gpso-0e7ee5751fd4bce3]

## Time and orders

Final-session closing entry signals cannot be filled within an already-ending horizon. Limits may remain unfilled; market/stop orders can slip through gaps, halts, price limits and illiquidity. The documents do not claim automatic monitoring or execution.[^stock-entry-strategy-5-instructions-51bfbec68204b2d3][^stock-entry-strategy-10-instructions-b62891c31dd14f64]

> Synthesis: The collection is a record of analyses and conditional decision logic. Its strategy-state vocabulary must not be read as an execution ledger.

## Evidence coverage

All 18 distinct accepted source summaries listed in provenance substantively discuss this topic. Methodology sources describe requirements; analysis-result sources describe dated applications and qualifications. Source count measures coverage, not independence.

- BKSL — Entry Strategy — 10dd — analysis-result.[^bksl-7eacfc7741e851d3]
- BNBR — Entry Strategy — 10dd — analysis-result.[^bnbr-694cd85cde8d5c1b]
- BULL — Entry Strategy — 10dd — analysis-result.[^bull-1b5fbb4a82ee07a0]
- BULL — Hold Strategy — 10dd — analysis-result.[^bull-48a2a5c45588e51e]
- BULL — Entry Strategy — 5dd — analysis-result.[^bull-a75efdaf022b83d5]
- EPAC — Entry Strategy — 10dd — analysis-result.[^epac-6e4659ee28ddf896]
- GPSO — Hold Strategy — 5dd — analysis-result.[^gpso-0e7ee5751fd4bce3]
- GPSO — Entry Strategy — 5dd — analysis-result.[^gpso-c8b53800c8dec568]
- HMSP — Entry Strategy — 10dd — analysis-result.[^hmsp-3b2ef84f3f7b15d1]
- HRTA — Entry Strategy — 5dd — analysis-result.[^hrta-e2f2954f5612304b]
- ICBP — Entry Strategy — 5dd — analysis-result.[^icbp-be4bae821fb86c38]
- MINA — Entry Strategy — 5dd — analysis-result.[^mina-37f439e72a0ebb94]
- Instructions for Generating a Stock Entry Strategy (10 Trading Sessions) — methodology.[^stock-entry-strategy-10-instructions-b62891c31dd14f64]
- Instructions for Generating a Stock Entry Strategy (5 Trading Sessions) — methodology.[^stock-entry-strategy-5-instructions-51bfbec68204b2d3]
- Instructions for Generating a Stock Hold Strategy (10 Trading Sessions) — methodology.[^stock-hold-strategy-10-instructions-d9a1481b76debebd]
- Instructions for Generating a Stock Hold Strategy (5 Trading Sessions) — methodology.[^stock-hold-strategy-5-instructions-d8721315f9cdba99]
- Instructions for Analyzing a Stock’s 10 Trading Session Upside Potential — methodology.[^stock-upside-analysis-10-instructions-510cb15a884ac7ad]
- Instructions for Analyzing a Stock’s 5 Trading Session Upside Potential — methodology.[^stock-upside-analysis-5-instructions-7ddbeb4e49d6506f]

[^bksl-7eacfc7741e851d3]: [BKSL — Entry Strategy — 10dd](../sources/bksl-7eacfc7741e851d3.md)
[^bnbr-694cd85cde8d5c1b]: [BNBR — Entry Strategy — 10dd](../sources/bnbr-694cd85cde8d5c1b.md)
[^bull-1b5fbb4a82ee07a0]: [BULL — Entry Strategy — 10dd](../sources/bull-1b5fbb4a82ee07a0.md)
[^bull-48a2a5c45588e51e]: [BULL — Hold Strategy — 10dd](../sources/bull-48a2a5c45588e51e.md)
[^bull-a75efdaf022b83d5]: [BULL — Entry Strategy — 5dd](../sources/bull-a75efdaf022b83d5.md)
[^epac-6e4659ee28ddf896]: [EPAC — Entry Strategy — 10dd](../sources/epac-6e4659ee28ddf896.md)
[^gpso-0e7ee5751fd4bce3]: [GPSO — Hold Strategy — 5dd](../sources/gpso-0e7ee5751fd4bce3.md)
[^gpso-c8b53800c8dec568]: [GPSO — Entry Strategy — 5dd](../sources/gpso-c8b53800c8dec568.md)
[^hmsp-3b2ef84f3f7b15d1]: [HMSP — Entry Strategy — 10dd](../sources/hmsp-3b2ef84f3f7b15d1.md)
[^hrta-e2f2954f5612304b]: [HRTA — Entry Strategy — 5dd](../sources/hrta-e2f2954f5612304b.md)
[^icbp-be4bae821fb86c38]: [ICBP — Entry Strategy — 5dd](../sources/icbp-be4bae821fb86c38.md)
[^mina-37f439e72a0ebb94]: [MINA — Entry Strategy — 5dd](../sources/mina-37f439e72a0ebb94.md)
[^stock-entry-strategy-10-instructions-b62891c31dd14f64]: [Instructions for Generating a Stock Entry Strategy (10 Trading Sessions)](../sources/stock-entry-strategy-10-instructions-b62891c31dd14f64.md)
[^stock-entry-strategy-5-instructions-51bfbec68204b2d3]: [Instructions for Generating a Stock Entry Strategy (5 Trading Sessions)](../sources/stock-entry-strategy-5-instructions-51bfbec68204b2d3.md)
[^stock-hold-strategy-10-instructions-d9a1481b76debebd]: [Instructions for Generating a Stock Hold Strategy (10 Trading Sessions)](../sources/stock-hold-strategy-10-instructions-d9a1481b76debebd.md)
[^stock-hold-strategy-5-instructions-d8721315f9cdba99]: [Instructions for Generating a Stock Hold Strategy (5 Trading Sessions)](../sources/stock-hold-strategy-5-instructions-d8721315f9cdba99.md)
[^stock-upside-analysis-10-instructions-510cb15a884ac7ad]: [Instructions for Analyzing a Stock’s 10 Trading Session Upside Potential](../sources/stock-upside-analysis-10-instructions-510cb15a884ac7ad.md)
[^stock-upside-analysis-5-instructions-7ddbeb4e49d6506f]: [Instructions for Analyzing a Stock’s 5 Trading Session Upside Potential](../sources/stock-upside-analysis-5-instructions-7ddbeb4e49d6506f.md)

<!-- END GENERATED -->

## Human notes
