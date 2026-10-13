---
type: concept
title: Terminal scenario returns and probability limits
description: Collection methodology and dated report applications with separately
  attributed uncertainty.
aliases: []
created: '2026-10-11T01:09:29.185071Z'
generated:
  by: llm-wiki-markdown/gpt-6
  at: '2026-10-11T01:09:29.185071Z'
source_count: 26
sources:
- id: bksl-7eacfc7741e851d3
  resource: ../sources/bksl-7eacfc7741e851d3.md
  title: BKSL — Entry Strategy — 10dd
- id: bksl-c2ef0f5604a2a67a
  resource: ../sources/bksl-c2ef0f5604a2a67a.md
  title: BKSL — Detailed Analysis — 10dd
- id: bnbr-694cd85cde8d5c1b
  resource: ../sources/bnbr-694cd85cde8d5c1b.md
  title: BNBR — Entry Strategy — 10dd
- id: bnbr-a50512c7bd8186ed
  resource: ../sources/bnbr-a50512c7bd8186ed.md
  title: BNBR — Detailed Analysis — 10dd
- id: bull-1b5fbb4a82ee07a0
  resource: ../sources/bull-1b5fbb4a82ee07a0.md
  title: BULL — Entry Strategy — 10dd
- id: bull-270816fba3cce331
  resource: ../sources/bull-270816fba3cce331.md
  title: BULL — Detailed Analysis — 10dd
- id: bull-a75efdaf022b83d5
  resource: ../sources/bull-a75efdaf022b83d5.md
  title: BULL — Entry Strategy — 5dd
- id: bull-b65b7de46fe80d87
  resource: ../sources/bull-b65b7de46fe80d87.md
  title: BULL — Detailed Analysis — 5dd
- id: epac-6e4659ee28ddf896
  resource: ../sources/epac-6e4659ee28ddf896.md
  title: EPAC — Entry Strategy — 10dd
- id: epac-8a9e4ccf50586c57
  resource: ../sources/epac-8a9e4ccf50586c57.md
  title: EPAC — Detailed Analysis — 10dd
- id: gpso-c8b53800c8dec568
  resource: ../sources/gpso-c8b53800c8dec568.md
  title: GPSO — Entry Strategy — 5dd
- id: gpso-d737030d107af0ac
  resource: ../sources/gpso-d737030d107af0ac.md
  title: GPSO — Detailed Analysis — 5dd
- id: hmsp-3b2ef84f3f7b15d1
  resource: ../sources/hmsp-3b2ef84f3f7b15d1.md
  title: HMSP — Entry Strategy — 10dd
- id: hmsp-6718bdc124e03030
  resource: ../sources/hmsp-6718bdc124e03030.md
  title: HMSP — Detailed Analysis — 10dd
- id: hrta-30a4845bd9a6638a
  resource: ../sources/hrta-30a4845bd9a6638a.md
  title: HRTA — Detailed Analysis — 5dd
- id: hrta-e2f2954f5612304b
  resource: ../sources/hrta-e2f2954f5612304b.md
  title: HRTA — Entry Strategy — 5dd
- id: icbp-be4bae821fb86c38
  resource: ../sources/icbp-be4bae821fb86c38.md
  title: ICBP — Entry Strategy — 5dd
- id: icbp-c79c85e00a548f9d
  resource: ../sources/icbp-c79c85e00a548f9d.md
  title: ICBP — Detailed Analysis — 5dd
- id: mina-37f439e72a0ebb94
  resource: ../sources/mina-37f439e72a0ebb94.md
  title: MINA — Entry Strategy — 5dd
- id: mina-b3a41fc7cf56b70d
  resource: ../sources/mina-b3a41fc7cf56b70d.md
  title: MINA — Detailed Analysis — 5dd
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

# Terminal scenario returns and probability limits

<!-- BEGIN GENERATED -->
## Definition

Upside methodology defines bull/base/bear scenarios at the final session close, not the maximum price touched. Numerical probabilities must total 100% when supported and subjective estimates must be labeled. Return denominators, midpoint choices or endpoint treatment, and cost/dividend/adjustment exclusions must remain visible.[^stock-upside-analysis-5-instructions-7ddbeb4e49d6506f][^stock-upside-analysis-10-instructions-510cb15a884ac7ad]

## Horizon-sensitive examples

The September 25 BULL 5dd analysis uses bull 398–404, base 378–396 and bear 356–376, with representative gross expected return +0.83%. The separately dated 10dd analysis uses bull 404–426, base 380–402 and bear 356–378, with +2.26%. Both are IDR terminal scenarios from the September 24 reference close 380, not realized returns.[^bull-b65b7de46fe80d87][^bull-270816fba3cce331]

EPAC’s 10dd subjective representative expectation is −2.3%, whereas GPSO’s 5dd figure is +3.15%. These source calculations retain different tickers, probability assumptions and execution limitations; neither is a current forecast made by the wiki.[^epac-8a9e4ccf50586c57][^gpso-d737030d107af0ac]

## Tensions and unavailable mappings

Entry methodology rejects automatic conversion of terminal-price probabilities into target-touch, stop-hit, fill or conditional-win probabilities. ICBP’s entry report therefore marks strategy expected value unavailable even though the detailed report provides +0.79% gross terminal expectation. BNBR likewise retains unavailable strategy EV alongside a conditional support-entry plan.[^stock-entry-strategy-5-instructions-51bfbec68204b2d3][^stock-entry-strategy-10-instructions-b62891c31dd14f64][^icbp-c79c85e00a548f9d][^icbp-be4bae821fb86c38][^bnbr-694cd85cde8d5c1b]

> Synthesis: A report’s numerical expected return and a managed strategy’s expected payoff answer different questions. Evidence of one cannot fill missing assumptions in the other.

## Evidence coverage

All 26 distinct accepted source summaries listed in provenance substantively discuss this topic. Methodology sources describe requirements; analysis-result sources describe dated applications and qualifications. Source count measures coverage, not independence.

- BKSL — Entry Strategy — 10dd — analysis-result.[^bksl-7eacfc7741e851d3]
- BKSL — Detailed Analysis — 10dd — analysis-result.[^bksl-c2ef0f5604a2a67a]
- BNBR — Entry Strategy — 10dd — analysis-result.[^bnbr-694cd85cde8d5c1b]
- BNBR — Detailed Analysis — 10dd — analysis-result.[^bnbr-a50512c7bd8186ed]
- BULL — Entry Strategy — 10dd — analysis-result.[^bull-1b5fbb4a82ee07a0]
- BULL — Detailed Analysis — 10dd — analysis-result.[^bull-270816fba3cce331]
- BULL — Entry Strategy — 5dd — analysis-result.[^bull-a75efdaf022b83d5]
- BULL — Detailed Analysis — 5dd — analysis-result.[^bull-b65b7de46fe80d87]
- EPAC — Entry Strategy — 10dd — analysis-result.[^epac-6e4659ee28ddf896]
- EPAC — Detailed Analysis — 10dd — analysis-result.[^epac-8a9e4ccf50586c57]
- GPSO — Entry Strategy — 5dd — analysis-result.[^gpso-c8b53800c8dec568]
- GPSO — Detailed Analysis — 5dd — analysis-result.[^gpso-d737030d107af0ac]
- HMSP — Entry Strategy — 10dd — analysis-result.[^hmsp-3b2ef84f3f7b15d1]
- HMSP — Detailed Analysis — 10dd — analysis-result.[^hmsp-6718bdc124e03030]
- HRTA — Detailed Analysis — 5dd — analysis-result.[^hrta-30a4845bd9a6638a]
- HRTA — Entry Strategy — 5dd — analysis-result.[^hrta-e2f2954f5612304b]
- ICBP — Entry Strategy — 5dd — analysis-result.[^icbp-be4bae821fb86c38]
- ICBP — Detailed Analysis — 5dd — analysis-result.[^icbp-c79c85e00a548f9d]
- MINA — Entry Strategy — 5dd — analysis-result.[^mina-37f439e72a0ebb94]
- MINA — Detailed Analysis — 5dd — analysis-result.[^mina-b3a41fc7cf56b70d]
- Instructions for Generating a Stock Entry Strategy (10 Trading Sessions) — methodology.[^stock-entry-strategy-10-instructions-b62891c31dd14f64]
- Instructions for Generating a Stock Entry Strategy (5 Trading Sessions) — methodology.[^stock-entry-strategy-5-instructions-51bfbec68204b2d3]
- Instructions for Generating a Stock Hold Strategy (10 Trading Sessions) — methodology.[^stock-hold-strategy-10-instructions-d9a1481b76debebd]
- Instructions for Generating a Stock Hold Strategy (5 Trading Sessions) — methodology.[^stock-hold-strategy-5-instructions-d8721315f9cdba99]
- Instructions for Analyzing a Stock’s 10 Trading Session Upside Potential — methodology.[^stock-upside-analysis-10-instructions-510cb15a884ac7ad]
- Instructions for Analyzing a Stock’s 5 Trading Session Upside Potential — methodology.[^stock-upside-analysis-5-instructions-7ddbeb4e49d6506f]

[^bksl-7eacfc7741e851d3]: [BKSL — Entry Strategy — 10dd](../sources/bksl-7eacfc7741e851d3.md)
[^bksl-c2ef0f5604a2a67a]: [BKSL — Detailed Analysis — 10dd](../sources/bksl-c2ef0f5604a2a67a.md)
[^bnbr-694cd85cde8d5c1b]: [BNBR — Entry Strategy — 10dd](../sources/bnbr-694cd85cde8d5c1b.md)
[^bnbr-a50512c7bd8186ed]: [BNBR — Detailed Analysis — 10dd](../sources/bnbr-a50512c7bd8186ed.md)
[^bull-1b5fbb4a82ee07a0]: [BULL — Entry Strategy — 10dd](../sources/bull-1b5fbb4a82ee07a0.md)
[^bull-270816fba3cce331]: [BULL — Detailed Analysis — 10dd](../sources/bull-270816fba3cce331.md)
[^bull-a75efdaf022b83d5]: [BULL — Entry Strategy — 5dd](../sources/bull-a75efdaf022b83d5.md)
[^bull-b65b7de46fe80d87]: [BULL — Detailed Analysis — 5dd](../sources/bull-b65b7de46fe80d87.md)
[^epac-6e4659ee28ddf896]: [EPAC — Entry Strategy — 10dd](../sources/epac-6e4659ee28ddf896.md)
[^epac-8a9e4ccf50586c57]: [EPAC — Detailed Analysis — 10dd](../sources/epac-8a9e4ccf50586c57.md)
[^gpso-c8b53800c8dec568]: [GPSO — Entry Strategy — 5dd](../sources/gpso-c8b53800c8dec568.md)
[^gpso-d737030d107af0ac]: [GPSO — Detailed Analysis — 5dd](../sources/gpso-d737030d107af0ac.md)
[^hmsp-3b2ef84f3f7b15d1]: [HMSP — Entry Strategy — 10dd](../sources/hmsp-3b2ef84f3f7b15d1.md)
[^hmsp-6718bdc124e03030]: [HMSP — Detailed Analysis — 10dd](../sources/hmsp-6718bdc124e03030.md)
[^hrta-30a4845bd9a6638a]: [HRTA — Detailed Analysis — 5dd](../sources/hrta-30a4845bd9a6638a.md)
[^hrta-e2f2954f5612304b]: [HRTA — Entry Strategy — 5dd](../sources/hrta-e2f2954f5612304b.md)
[^icbp-be4bae821fb86c38]: [ICBP — Entry Strategy — 5dd](../sources/icbp-be4bae821fb86c38.md)
[^icbp-c79c85e00a548f9d]: [ICBP — Detailed Analysis — 5dd](../sources/icbp-c79c85e00a548f9d.md)
[^mina-37f439e72a0ebb94]: [MINA — Entry Strategy — 5dd](../sources/mina-37f439e72a0ebb94.md)
[^mina-b3a41fc7cf56b70d]: [MINA — Detailed Analysis — 5dd](../sources/mina-b3a41fc7cf56b70d.md)
[^stock-entry-strategy-10-instructions-b62891c31dd14f64]: [Instructions for Generating a Stock Entry Strategy (10 Trading Sessions)](../sources/stock-entry-strategy-10-instructions-b62891c31dd14f64.md)
[^stock-entry-strategy-5-instructions-51bfbec68204b2d3]: [Instructions for Generating a Stock Entry Strategy (5 Trading Sessions)](../sources/stock-entry-strategy-5-instructions-51bfbec68204b2d3.md)
[^stock-hold-strategy-10-instructions-d9a1481b76debebd]: [Instructions for Generating a Stock Hold Strategy (10 Trading Sessions)](../sources/stock-hold-strategy-10-instructions-d9a1481b76debebd.md)
[^stock-hold-strategy-5-instructions-d8721315f9cdba99]: [Instructions for Generating a Stock Hold Strategy (5 Trading Sessions)](../sources/stock-hold-strategy-5-instructions-d8721315f9cdba99.md)
[^stock-upside-analysis-10-instructions-510cb15a884ac7ad]: [Instructions for Analyzing a Stock’s 10 Trading Session Upside Potential](../sources/stock-upside-analysis-10-instructions-510cb15a884ac7ad.md)
[^stock-upside-analysis-5-instructions-7ddbeb4e49d6506f]: [Instructions for Analyzing a Stock’s 5 Trading Session Upside Potential](../sources/stock-upside-analysis-5-instructions-7ddbeb4e49d6506f.md)

<!-- END GENERATED -->

## Human notes
