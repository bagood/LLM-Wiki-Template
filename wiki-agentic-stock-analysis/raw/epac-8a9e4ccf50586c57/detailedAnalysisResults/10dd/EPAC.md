**Report generated on:** 25 September 2026, 13:17 WIB (UTC+7)

## 1. Report timing and forecast window

**Company name:** PT Megalestari Epack Sentosaraya Tbk

**Ticker and exchange:** EPAC / Indonesia Stock Exchange

**Investor currency:** IDR

**Risk tolerance:** Moderate

**Entry price:** None supplied

**Analysis timestamp:** 25 September 2026, 13:17 WIB

**Market status at analysis:** The 25 September IDX session was partially elapsed. It is therefore excluded from the forward horizon.

**News research cut-off:** 25 September 2026, 13:17 WIB

**Supplied technical-data cut-off:** Completed IDX regular-session bar dated 24 September 2026

**Forecast horizon:** Exactly 10 future IDX trading sessions

**Forecast start:** 28 September 2026

**Forecast expiry:** Regular close on 9 October 2026

**Calendar status:** Provisional but well supported. No Indonesian national or collective holiday falls inside the window. The government’s official 2026 holiday list contains no September or October closure affecting these dates. No separate unexpected IDX closure was located by the research cut-off. [Indonesian State Secretariat, published 19 September 2025](https://www.setneg.go.id/baca/index/inilah_skb_3_menteri_libur_nasional_dan_cuti_bersama_2026)

**Excluded dates:** 26–27 September and 3–4 October 2026, because they are weekends

**Stock suspension:** No current EPAC suspension announcement was found. This is not a guarantee against a later trading halt.

### Exact 10-session schedule

**Session 1**

**Date:** Monday, 28 September 2026

**Exchange time zone:** WIB, UTC+7

**Session 2**

**Date:** Tuesday, 29 September 2026

**Exchange time zone:** WIB, UTC+7

**Session 3**

**Date:** Wednesday, 30 September 2026

**Exchange time zone:** WIB, UTC+7

**Session 4**

**Date:** Thursday, 1 October 2026

**Exchange time zone:** WIB, UTC+7

**Session 5**

**Date:** Friday, 2 October 2026

**Exchange time zone:** WIB, UTC+7

**Session 6**

**Date:** Monday, 5 October 2026

**Exchange time zone:** WIB, UTC+7

**Session 7**

**Date:** Tuesday, 6 October 2026

**Exchange time zone:** WIB, UTC+7

**Session 8**

**Date:** Wednesday, 7 October 2026

**Exchange time zone:** WIB, UTC+7

**Session 9**

**Date:** Thursday, 8 October 2026

**Exchange time zone:** WIB, UTC+7

**Session 10**

**Date:** Friday, 9 October 2026

**Exchange time zone:** WIB, UTC+7

---

## 2. Input validation and data freshness

**Payload shape:** Unambiguous date-keyed JSON object, conceptually normalized into one dated record

**Sorting result:** One record; latest and only date is 24 September 2026

**Required fields:** Present

**Finite required values:** Yes

**Price positivity:** Valid

**Volume:** Non-negative and valid

**OHLC consistency:** Valid; High equals Open and Close, while Low equals Open and Close

**Duplicate dates:** None

**Impossible or future dates:** None

**Explicit provisional bar:** None

**Missing values:** Foreign-flow, non-regular-market, and `Close Location Value` fields are null. These omissions limit positioning analysis but do not invalidate the payload.

**Raw-history limitation:** Only one raw daily bar is supplied. Historical changes can therefore be discussed only through the derived features already contained in that record.

**Corporate-action adjustment basis:** Not supplied. No cross-period raw-price calculation requiring adjustment reconciliation is performed.

**Latest bar relationship:** Under the Trusted Technical-Data Contract, the 24 September record is accepted as the immediately preceding completed session.

**Actionability:** Current enough for this forecast. However, today’s partially completed 25 September session may incorporate the newly published buyback and operating news; its closing bar is deliberately not substituted or estimated.

**Source:** Provided technical dataset

---

## 3. Supplied OHLCV and technical snapshot

### Latest supplied bar

**Date:** 24 September 2026

**Open:** IDR 50

**High:** IDR 50

**Low:** IDR 50

**Close:** IDR 50

**Volume:** 85,100 shares, assuming the payload’s volume unit is shares

**Intraday return:** `Intraday Return Percent = 0.0`

**Range:** `High Low Range Percent = 0.0`

**Interpretation:** The session printed at one price throughout. That shows no observable intraday price discovery in this bar and materially weakens the reliability of conventional breakout and stop execution assumptions.

### Trend evidence

**Signal:** `ATR Bullish = 0`; `ATR Bearish = 1`

**Implication:** The supplied binary ATR regime is bearish. These are condition flags, not ATR distances.

**Signal:** `SuperTrend Bullish = 0`; `SuperTrend Bearish = 1`

**Implication:** Confirms the bearish trend regime.

**Signal:** `Aroon Up = 28.0`; `Aroon Down = 72.0`; `Aroon Oscillator = -44.0`; `Aroon Down Trend = 1`

**Implication:** Recent downside timing dominates upside timing.

**Signal:** `Plus Directional Index = 12.515`; `Minus Directional Index = 19.407`; `Directional Index Spread = -6.892`

**Implication:** Sellers have directional advantage.

**Signal:** `ADX Value = 15.778`; `ADX Strong Trend = 0`

**Implication:** The bearish direction is not accompanied by a conventionally strong trend. This leaves room for consolidation or a news-driven reversal, but does not establish one.

**Signal:** `Vortex Positive = 0.84`; `Vortex Negative = 1.24`; `Vortex Spread = -0.4`

**Implication:** Confirms negative directional positioning.

**Signal:** `Close to EMA 5D = -0.0051`; `Close to EMA 20D = -0.0585`; `Close to EMA 50D = -0.1248`

**Implication:** The close is below every supplied EMA-relative reference, with progressively larger deficits at longer lookbacks.

**Signal:** `EMA 5D to 20D Spread = -0.0537`; `EMA 10D to 50D Spread = -0.1031`

**Implication:** Shorter averages remain below longer averages; this is structurally bearish.

### Momentum evidence

**Signal:** `Price Momentum 5D = 0.0`

**Implication:** The latest price is unchanged over the encoded five-day lookback.

**Signal:** `Price Momentum 10D = -0.0909`; `Price Momentum 20D = -0.0741`

**Implication:** Medium-short momentum remains negative despite recent price stagnation.

**Signal:** `RSI Value = 33.582`; `RSI Down Trend = 1`

**Implication:** Weak momentum, approaching but not reaching the conventional 30 oversold threshold.

**Signal:** `RSI 7 = 24.586`; `RSI 21 = 37.661`; `RSI 7 Minus 21 = -13.075`

**Implication:** Short-horizon momentum is oversold and substantially weaker than the longer RSI. This creates rebound potential, but an oversold reading can persist.

**Signal:** `Stochastic K Value = 0.0`; `Stochastic D Value = 0.0`; `Stochastic Oscillator Oversold = 1.0`

**Implication:** Extreme supplied oversold condition. It supports rebound optionality but is not a bullish crossover because K minus D is zero.

**Signal:** `Fisher Transform = -4.178`; `Fisher Transform Trigger = -3.768`; `Fisher Down Trend = 1`; `Fisher Reversal = 0.0`

**Implication:** Strong negative momentum remains active, with no supplied reversal signal.

**Signal:** `MACD Near 0 = 1`; `MACD Histogram Percent = -0.00307`

**Implication:** MACD is only slightly negative and near zero. This is less bearish than Fisher, RSI, and trend evidence, but is not positive.

### Volatility and channel evidence

**Signal:** `ATR Percent 14D = 0.04464`

**Implication:** The supplied ATR feature corresponds to approximately 4.46% of the reference price, or about IDR 2.23 at a close of IDR 50.

**Signal:** `Donchian Percent B = 0.0`; `Donchian Oversold = 1`

**Implication:** Price is at the supplied Donchian lower boundary.

**Signal:** `Distance From 20D Low = 0.0`; `Distance From 60D Low = 0.0`

**Implication:** The close equals the encoded 20- and 60-day lows.

**Signal:** `Distance From 20D High = -0.18033`

**Derived historical reference:** Approximately IDR 61, calculated as `50 / (1 − 0.1803279)`.

**Signal:** `Distance From 60D High = -0.38272`

**Derived historical reference:** Approximately IDR 81, calculated as `50 / (1 − 0.3827160)`.

**Caution:** These are reconstructed historical high references, not forecast targets or verified resistance levels.

**Signal:** `Bollinger Percent B = 0.1865`; `Bollinger Width = 0.2142`; `Width Bollinger Increasing = 1`

**Implication:** Price is in the lower part of the supplied band while band width is increasing, consistent with downside volatility risk.

**Signal:** `Keltner Percent B = 0.05675`; `Width Keltner Decreasing = 1`

**Implication:** Price is near the lower Keltner region, but Keltner contraction conflicts with Bollinger expansion.

**Signal:** `Realized Volatility 5D = 0.0`

**Implication:** The encoded five-day price series was static. This does not mean execution risk is zero; in an illiquid stock, observed volatility can understate gap and fill risk.

### Volume and flow evidence

**Signal:** `Volume Ratio 20D = 0.001603`

**Implication:** On its apparent ratio scale, the latest volume is only about 0.16% of the encoded 20-day norm—exceptionally weak participation. Because the exact definition was not provided, the magnitude should be treated cautiously, but it plainly indicates very low relative activity.

**Signal:** `Volume Change 1D = -0.8755`; `Volume Change 5D = -0.9794`

**Implication:** Participation has collapsed relative to the encoded comparison periods.

**Signal:** `PVO Value = -58.825`; `PVO Histogram = -11.577`; `PVO Positive = 0`

**Implication:** Confirms severe volume contraction.

**Signal:** `MFI Value = 38.477`; `MFI Decreasing = 1`

**Implication:** Money flow is weak but not at the supplied oversold threshold.

**Signal:** `CMF Value = -0.01099`; `Negative CMF = 1`; `Strong Negative CMF = 0`; `CMF Change 5D = 0.05418`

**Implication:** Capital flow remains slightly negative, although its recent change has improved.

**Signal:** `OBV to MA20 Ratio = 1.2695`; `OBV Change 5D Normalized = 0.0`

**Implication:** The OBV level relative to its moving average is potentially constructive, but no five-day OBV advance confirms accumulation.

**Foreign and domestic positioning:** Not estimable; all supplied foreign-flow fields are null.

**Non-regular/block activity:** Not estimable; all relevant supplied fields are null.

### Technical balance

**Bullish or rebound-supportive evidence:** Oversold short RSI, zero stochastic at the lower channel boundary, price at supplied 20- and 60-day lows, and improving CMF change.

**Bearish evidence:** Bearish ATR and SuperTrend states, negative Aroon/DMI/Vortex structures, price below all supplied EMA references, negative 10- and 20-day momentum, and Fisher downtrend without reversal.

**Decisive weakness:** Any rebound thesis lacks volume confirmation. The supplied volume indicators show exceptionally weak participation.

---

## 4. Key company news and catalysts

### Proposed buyback and extraordinary meeting

**Publication date:** 25 September 2026

**Event date:** Announcement published 25 September 2026; proposed RUPSLB scheduled for 3 November 2026

**Reported development:** EPAC proposes buying back up to 10% of issued shares using up to IDR 20 billion, funded from internal cash. Shareholder approval is required before implementation. [BCA Sekuritas/IQPlus, 25 September 2026](https://bcasekuritas.co.id/latest-news/news/epac-siapkan-dana-rp20-miliar-untuk-buyback-saham)

**Official corroboration:** IDX posted EPAC’s notice of a planned extraordinary shareholders’ meeting on 25 September. [IDX announcements, 25 September 2026](https://www.idx.co.id/id/berita/pengumuman)

**Direction:** Short-term sentiment bullish; financing and opportunity-cost implications uncertain

**Window relevance:** The announcement can affect sessions 1–10, but the 3 November vote and any actual buyback lie outside this forecast window.

**Potential magnitude:** Potentially high for sentiment because the proposed maximum repurchase is large in percentage terms. Actual price impact is unknown because approval, execution price, execution volume, and timing remain unresolved.

**Priced-in assessment:** Unknown. The announcement occurred during the partially elapsed 25 September session, for which no authorized completed technical bar was supplied.

**Confirmation:** Stronger post-announcement closing prices accompanied by a meaningful recovery in supplied relative-volume indicators.

**Invalidation:** Weak or absent buying response, adverse clarification about funding, or withdrawal/delay of the proposal.

### Sales objective and current losses

**Publication date:** 25 September 2026, 07:10 WIB

**Reported development:** Management continues to target 15% sales growth in 2026, but EPAC reportedly recorded an approximately IDR 5.54 billion first-half net loss. Higher oil-linked raw-material costs, freight, and operating expenses pressured profitability. [Kontan, 25 September 2026](https://insight.kontan.co.id/news/megalestari-epack-epac-kejar-pertumbuhan-penjualan-15)

**Direction:** Mixed—growth target is bullish, but continuing losses and input-cost pressure are bearish.

**Window relevance:** Immediate narrative driver throughout the forecast.

**Priced-in assessment:** Partly possible given the supplied negative trend, but not demonstrable from one record.

**Confirmation:** Evidence of improving profitability, cost pass-through, or operating leverage.

**Invalidation:** Further oil/freight pressure or evidence that sales growth is being achieved without adequate margin.

### Shift to digital printing and proposed financing

**Publication date:** 15 September 2026

**Event date:** Company response dated 15 September following an IDX request dated 11 September

**Reported development:** The company said discontinuing conventional flexible packaging would not threaten continuity and that it would focus on digital printing through its subsidiary. Expansion was expected to use leasing and a proposed rights issue requiring an RUPSLB. The Surabaya facility is planned for operation in 2027. [IndoPremier summary, 15 September 2026](https://www.indopremier.com/module/newsDetail.php?group_news=IPOTNEWS&halaman=1&jdl=AI_Report___Tanggapan_atas_Permintaan_Penjelasan_Bursa_%28EPAC%29&name=&news_id=241744&q=EPAC%2C+AI%2C+AI+Report%2C+AI-Report&search=y_general&taging_subtype=EPAC)

**Direction:** Strategically constructive, but near-term uncertain and potentially dilutive.

**Window relevance:** Narrative catalyst only; facility completion is outside the window.

**Key risk:** Buyback and possible rights-issue narratives can conflict—one reduces shares while the other may issue new equity. Terms and sequencing are unknown.

### Control change

**Publication date:** 23 July 2026

**Reported development:** PT Triple Berkah Bersama reportedly completed an acquisition of 34.56% of outstanding shares from two holders, becoming the new controller and triggering a mandatory-tender process. The source itself warns that its synopsis is AI-generated, so it is treated as secondary context. [IndoPremier, 23 July 2026](https://www.indopremier.com/ipotnews/newsDetail.php?group_news=IPOTNEWS&halaman=1&jdl=AI_Report___Keterbukaan_Informasi_Tentang_Pengambilalihan_Penawaran_Tender_Wajib_Refloat_%28EPAC%29&name=&news_date=&news_id=227296&q=EPAC,+Megalestari+Epack+Sentosaraya,+AI,+AI+Report,+AI-Report&search=y_general&taging_subtype=STOCK)

**Direction:** Uncertain; new control may support restructuring, but execution and governance risks remain.

**Window relevance:** Continuing background, not a newly scheduled 10-session event.

---

## 5. Indonesia market news

### Bank Indonesia policy

**Publication and event date:** 23 September 2026

**Development:** Bank Indonesia held the BI Rate at 5.75%, citing rupiah stabilization amid strong external pressures while maintaining support for growth. Credit growth remained positive, but BI emphasized currency stability and capital inflows. [Bank Indonesia, 23 September 2026](https://www.bi.go.id/en/publikasi/ruang-media/news-release/Pages/sp_2819326.aspx)

**Transmission to EPAC:** A stable domestic policy rate avoids a fresh local tightening shock, but currency pressure remains important. A weaker IDR could raise the local cost of imported films, resins, machinery, or dollar-linked freight if EPAC lacks natural hedges or pricing power.

**Direction:** Neutral to mildly supportive for domestic liquidity; currency risk remains bearish.

### Domestic financial-system conditions

**Publication date:** 7 September 2026

**Development:** OJK described the financial-services sector as stable but acknowledged high geopolitical uncertainty and global inflation pressure. [OJK, 7 September 2026](https://ojk.go.id/id/berita-dan-kegiatan/siaran-pers/Pages/RDKB-Agustus-2026.aspx)

**Transmission to EPAC:** System stability supports access to leasing and working capital, but elevated geopolitical and inflation risk can raise input costs and make investors less tolerant of loss-making small-cap companies.

**Direction:** Mixed.

---

## 6. Global market news

### Federal Reserve tightening

**Publication and event date:** 16 September 2026

**Development:** The Federal Reserve raised its target range by 25 basis points to 3.75%–4.00%, stating that inflation remained elevated. [Federal Reserve, 16 September 2026](https://www.federalreserve.gov/newsevents/pressreleases/monetary20260916a.htm)

**Transmission to EPAC:** Higher US rates can support the dollar, pressure emerging-market currencies and capital flows, and indirectly raise imported-input or financing costs. This is a bearish external factor for a small Indonesian manufacturer with current profitability pressure.

**Direction:** Bearish through liquidity and currency channels.

### Oil and shipping disruption

**Publication date:** 18 September 2026

**Development:** The IEA said renewed Middle East hostilities had again created upward oil-price pressure and constrained exports, even after earlier offsets from emergency stocks and alternative routes. [IEA, 18 September 2026](https://www.iea.org/commentaries/oil-markets-strain-to-plug-the-gap-left-by-middle-east-supply-shortfall)

**Transmission to EPAC:** Packaging films and resins are linked to petrochemical feedstocks; higher oil and freight costs can compress margins unless passed through to customers. This directly corroborates the cost pressures reported by Kontan.

**Direction:** Bearish and directly relevant.

**Counterpoint:** Reuters reported on 25 September that oil eased slightly on possible US-Iran truce expectations, although attacks and supply risks remained. [Reuters via MarketScreener, 25 September 2026](https://uk.marketscreener.com/news/oil-prices-fall-as-markets-look-to-iran-truce-but-remain-wary-of-attacks-on-oil-facilities-ce785adfdb8cf525)

**Net assessment:** Oil-cost risk remains elevated but headline-sensitive. A durable de-escalation would improve EPAC’s margin outlook; renewed disruption would worsen it.

---

## 7. Integrated technical-and-news assessment

**Technical state:** Bearish and oversold

**News state:** Mixed, with a fresh sentiment-positive buyback proposal offset by first-half losses, rising input costs, a potential future rights issue, and execution risk around restructuring.

**Agreement:** The reported profitability pressure agrees with negative medium-term momentum, price below all supplied EMA references, bearish trend flags, and weak money flow.

**Divergence:** The new proposed buyback is more constructive than the 24 September technical state. Because it was announced after the supplied cut-off, the dataset cannot show whether buyers accepted or rejected the catalyst.

**Upside mechanism:** A short-covering or speculative rebound could occur if the buyback proposal attracts genuine participation, oil-cost fears ease, and EPAC breaks out of the five-day price freeze with higher volume.

**Capital-preservation issue:** The one-price bar and extremely depressed relative volume create material execution risk. Apparent low volatility may reflect inactivity rather than stability.

**Overall integrated bias:** Neutral-to-bearish until post-announcement price and volume confirmation appears.

---

## 8. Near-term catalyst calendar

### Catalyst 1

**Event:** Market digestion of proposed buyback and 15% sales-growth narrative

**Expected timing:** Session 1, 28 September 2026, from the open

**Confirmation status:** Announcement confirmed; shareholder approval and execution remain pending

**Directional effect:** Bullish sentiment, uncertain fundamentals

**Likely magnitude:** Potentially high but difficult to execute reliably in weak liquidity

**Already priced in:** Unknown because the 25 September completed bar is unavailable by design

**Confirmation evidence:** A completed close above approximately IDR 52.23, the supplied one-ATR reference, with material volume recovery

**Invalidation evidence:** Continued closing at IDR 50 on negligible volume or adverse buyback clarification

### Catalyst 2

**Event:** Month- and quarter-end positioning

**Expected timing:** Sessions 1–3

**Confirmation status:** Calendar-based, not company-specific

**Directional effect:** Uncertain

**Likely magnitude:** Low to medium unless it coincides with buyback speculation

**Already priced in:** Unknown

**Confirmation evidence:** Expanding volume with a directional close

**Invalidation evidence:** Continued zero-range sessions

### Catalyst 3

**Event:** Oil, freight, and Middle East developments

**Expected timing:** Continuous across sessions 1–10

**Confirmation status:** Ongoing external risk

**Directional effect:** Lower oil/freight costs bullish; renewed disruption bearish

**Likely magnitude:** Medium through margin expectations

**Already priced in:** Partly possible but not measurable

**Confirmation evidence:** Durable de-escalation and company evidence of cost relief

**Invalidation evidence:** Renewed supply disruptions or further management warning on raw materials

### Catalyst 4

**Event:** RUPSLB concerning buyback and potentially other capital actions

**Expected date:** 3 November 2026

**Forecast session:** Outside the 10-session window

**Directional effect:** Contextually bullish for buyback approval, but uncertain given possible future rights-issue financing

**Near-window role:** Anticipation only; no approval should be assumed during this forecast.

---

## 9. Bull, base, and bear scenarios

The ranges below concern the closing price at the end of session 10. Probabilities are subjective judgment estimates, not statistically calibrated forecasts.

### Bull case

**Required conditions:** Buyback news attracts genuine demand; price escapes the five-day static regime; volume recovers materially; oil/freight news improves; no adverse rights-issue or liquidity clarification emerges.

**Price target or range:** IDR 52–54

**Target method:** Approximately one to two supplied 14-day ATR percentages above IDR 50: `50 × (1 + 0.04464) ≈ 52.23` and `50 × (1 + 2 × 0.04464) ≈ 54.46`, rounded to avoid false precision.

**Representative price for probability weighting:** IDR 53

**Range return calculation:** `(52 − 50) / 50 × 100 = 4.0%` to `(54 − 50) / 50 × 100 = 8.0%`

**Representative return:** `(53 − 50) / 50 × 100 = 6.0%`

**Estimated probability:** 20%

**Timing:** A catalyst reaction would most plausibly begin in sessions 1–3. Failure to gain volume by session 5 would materially reduce this probability.

### Base case

**Most likely path:** Buyback optimism is offset by losses, input-cost pressure, weak technical structure, and poor liquidity. Price remains near the supplied reference without a durable breakout.

**Price target or range:** IDR 49–51

**Target method:** Consolidation around the IDR 50 reference, consistent with zero five-day momentum and zero five-day realized volatility. The range is judgmental because only one raw bar is available and tick/execution constraints were not supplied.

**Representative price for probability weighting:** IDR 50

**Range return calculation:** `(49 − 50) / 50 × 100 = −2.0%` to `(51 − 50) / 50 × 100 = 2.0%`

**Representative return:** `(50 − 50) / 50 × 100 = 0.0%`

**Estimated probability:** 45%

### Bear case

**Failure conditions:** Buyback enthusiasm fades; no volume returns; oil/freight pressure worsens; rights-issue dilution concerns dominate; or price loses the current low regime if such lower trading is executable.

**Downside target or range:** IDR 41–48

**Target method:** Upper portion represents a modest loss of the current reference. Lower portion is anchored to `ATR Stop Distance Percent = −0.171728`, implying `50 × (1 − 0.171728) ≈ 41.41`. The field’s exact construction is unspecified, so this is an analytical boundary, not a guaranteed executable stop.

**Representative price for probability weighting:** IDR 45

**Range return calculation:** `(41 − 50) / 50 × 100 = −18.0%` to `(48 − 50) / 50 × 100 = −4.0%`

**Representative return:** `(45 − 50) / 50 × 100 = −10.0%`

**Estimated probability:** 35%

### Probability-weighted return

**Probability total:** 20% + 45% + 35% = 100%

**Calculation:** `(0.20 × 6.0%) + (0.45 × 0.0%) + (0.35 × −10.0%)`

**Probability-weighted expected gross price return:** `1.2% + 0.0% − 3.5% = −2.3%`

**Return denominator:** Latest supplied close of IDR 50

**Dividends:** Excluded

**Brokerage, taxes, bid–ask spread, and slippage:** Excluded

**Currency conversion:** Not applicable; reference and scenarios are in IDR

**Important limitation:** The expected return is highly sensitive to subjective scenario probabilities and uncertain execution. It should not be treated as a calibrated statistical expectation.

---

## 10. Risk assessment, controls, and review checkpoints

### Risk 1: Illiquidity and failed execution

**Probability:** High

**Potential impact:** High

**Evidence:** `Volume Ratio 20D = 0.001603`, sharply negative volume changes, negative PVO, and a zero-range bar

**Warning indicator:** Continued one-price sessions, negligible trading, wide or absent executable quotes, or inability to transact near the analytical price

**Risk-control response:** Do not use a market order. Require confirmed executable liquidity and use a limit order. Keep position size below normal moderate-risk allocation.

### Risk 2: Persistent unprofitability

**Probability:** High

**Potential impact:** High

**Evidence:** News-reported first-half net loss and higher raw-material, freight, and operating costs

**Warning indicator:** Further loss guidance, weak margin commentary, or sales growth without profit improvement

**Risk-control response:** Avoid treating the 15% sales objective as equivalent to earnings growth.

### Risk 3: Oil and freight escalation

**Probability:** Medium

**Potential impact:** High

**Warning indicator:** Renewed Middle East supply disruption or company comments indicating further resin/freight cost increases

**Risk-control response:** Reassess immediately; do not average down solely because momentum appears oversold.

### Risk 4: Dilution and capital-allocation conflict

**Probability:** Medium

**Potential impact:** High

**Evidence:** Proposed buyback alongside reported plans to finance expansion partly through a rights issue

**Warning indicator:** Rights-issue terms, a large discount, significant new-share count, or evidence that buyback and expansion strain internal cash

**Risk-control response:** Wait for formal terms and evaluate net share-count and cash effects together.

### Risk 5: Buy-the-rumor/sell-the-news behavior

**Probability:** Medium

**Potential impact:** Medium to high

**Warning indicator:** Initial price strength without volume persistence, followed by reversal toward IDR 50

**Risk-control response:** Require a completed-session confirmation rather than chasing the opening reaction.

### Risk 6: Missing positioning and execution data

**Probability:** Certain limitation

**Potential impact:** Medium to high

**Warning indicator:** None; the data are currently absent

**Risk-control response:** Do not infer foreign accumulation, order-book depth, bid–ask spread, or block activity.

### Trade controls

**Preferred entry zone:** No immediate entry recommended. A defensible pullback entry cannot be established from a one-price bar.

**Conditional confirmation level:** A completed close above approximately IDR 52.23, derived as one supplied ATR percentage above IDR 50, accompanied by material volume recovery.

**Stronger confirmation:** A completed close above approximately IDR 54.46, or two ATR percentages above the reference.

**Analytical invalidation level:** Approximately IDR 41.41, derived from `ATR Stop Distance Percent = −0.171728`.

**Executable stop-loss:** Not estimable responsibly from supplied data. The analytical IDR 41.41 boundary is not necessarily executable, and stop orders can fail through gaps, price limits, suspension, or lack of bids.

**First profit-taking zone:** IDR 52–54

**Second profit-taking reference:** Approximately IDR 61, the reconstructed supplied 20-day high—not a guaranteed 10-session target.

**Illustrative risk–reward setup:** Entry IDR 53 after confirmation; analytical stop IDR 41.41; target IDR 61

**Risk–reward calculation:** `(61 − 53) / (53 − 41.41) = 8 / 11.59 ≈ 0.69`

**Assessment:** Unattractive because estimated upside is smaller than analytical downside, before costs and slippage.

**Position sizing:** Qualitative only. Capital and per-trade risk budgets were not provided, and no reliable executable stop distance exists. For moderate risk tolerance, any exploratory position should be materially smaller than a normal liquid-stock position.

### Sessions 1–5 review

**Priority 1:** Check invalidation and actual tradability first.

**Priority 2:** Determine whether buyback news produces sustained closing strength rather than an opening-only reaction.

**Priority 3:** Require recovery in volume and money-flow features.

**Session-5 checkpoint:** At the close on 2 October 2026, obtain a new completed technical payload. Failure to close above the one-ATR confirmation area with materially improved volume favors the base or bear case.

### Sessions 6–10 review

**Priority 1:** Check whether any early gain is being retained.

**Priority 2:** Monitor oil/freight developments and rights-issue disclosures.

**Priority 3:** Avoid converting a failed 10-session trade into an indefinite holding based only on the November meeting.

**Forecast expiry:** Regular close on 9 October 2026. The forecast must then expire. Any continued exposure requires a fresh timestamp, schedule, news search, and supplied completed-session data.

---

## 11. Final assessment

**Overall judgment:** Neutral/Wait

**Reason:** The buyback proposal offers a credible sentiment catalyst, and the stock is technically oversold. Nevertheless, the dominant supplied trend structure is bearish, profitability is under pressure, and the latest bar shows exceptionally weak participation. The subjective expected return is negative and the illustrative risk–reward ratio is below 1.

### Strongest bullish items

- The proposed buyback covers up to 10% of issued shares, subject to November approval.

- `RSI 7 = 24.586`, `Stochastic Oscillator Oversold = 1`, and the price is at the supplied 20- and 60-day lows, creating rebound potential.

- Management retains a reported 15% sales-growth objective and is shifting toward digital printing.

### Strongest bearish items

- `ATR Bearish = 1`, `SuperTrend Bearish = 1`, negative Aroon/DMI/Vortex structures, and the close below every supplied EMA-relative reference.

- First-half losses and direct oil/freight/raw-material cost pressure.

- Exceptionally weak volume evidence, including `Volume Ratio 20D = 0.001603`, which undermines reliable entry and exit execution.

**Possibly already priced in:** Historical profitability problems, conventional-business closure, and the control change may be partly reflected in the negative trend. The degree to which the 25 September buyback news is priced in is unknown.

**Most important missing information:** Completed 25 September OHLCV and indicators, executable order-book liquidity, foreign/domestic flows, corporate-action adjustment basis, definitive rights-issue terms, and detailed buyback/RUPSLB documents.

**Single most likely thesis invalidator:** Failure of the buyback announcement to produce sustained price and volume confirmation.

**Adverse-environment test:** Renewed oil disruption, further IDR pressure, or a risk-off reaction to higher US rates would strengthen the Neutral/Wait conclusion and could shift it to Avoid.

**Data-source confirmation:** No internet-sourced price, OHLCV, volume, technical indicator, support/resistance, market-flow figure, target price, or consensus target was used as a calculation input. All price calculations use the Provided technical dataset.

---

## 12. News and official calendar sources

**Official calendar source:** [Indonesian State Secretariat—2026 national and collective holidays, published 19 September 2025](https://www.setneg.go.id/baca/index/inilah_skb_3_menteri_libur_nasional_dan_cuti_bersama_2026)

**Official exchange source:** [IDX announcements, accessed 25 September 2026](https://www.idx.co.id/id/berita/pengumuman)

**Company news source:** [Kontan—sales objective and first-half loss, published 25 September 2026](https://insight.kontan.co.id/news/megalestari-epack-epac-kejar-pertumbuhan-penjualan-15)

**Buyback source:** [BCA Sekuritas/IQPlus—proposed buyback, published 25 September 2026](https://bcasekuritas.co.id/latest-news/news/epac-siapkan-dana-rp20-miliar-untuk-buyback-saham)

**Domestic policy source:** [Bank Indonesia—September policy decision, published 23 September 2026](https://www.bi.go.id/en/publikasi/ruang-media/news-release/Pages/sp_2819326.aspx)

**Domestic regulatory source:** [OJK—financial-sector conditions, published 7 September 2026](https://ojk.go.id/id/berita-dan-kegiatan/siaran-pers/Pages/RDKB-Agustus-2026.aspx)

**Global monetary-policy source:** [Federal Reserve—FOMC decision, published 16 September 2026](https://www.federalreserve.gov/newsevents/pressreleases/monetary20260916a.htm)

**Commodity source:** [IEA—Middle East oil-supply pressure, published 18 September 2026](https://www.iea.org/commentaries/oil-markets-strain-to-plug-the-gap-left-by-middle-east-supply-shortfall)

**Latest oil-news counterpoint:** [Reuters via MarketScreener, published 25 September 2026](https://uk.marketscreener.com/news/oil-prices-fall-as-markets-look-to-iran-truce-but-remain-wary-of-attacks-on-oil-facilities-ce785adfdb8cf525)

- **Next 10 Trading Sessions Upside Potential:** The forecast runs from 28 September through 9 October 2026. The latest supplied close is IDR 50 on 24 September; no entry price was supplied. The base case is IDR 49–51, equal to −2.0% to +2.0%, while the subjective probability-weighted expected gross return is −2.3%. The bull case is IDR 52–54, or +4.0% to +8.0%. Confidence is low because only one raw bar is supplied and liquidity is extremely weak. Upside requires sustained reaction to the buyback proposal, easing oil/freight pressure, a close above approximately IDR 52.23, and material volume recovery.

- **Risks Related to the Stock:** Principal risks are first-half losses, oil-linked raw-material and freight inflation, possible rights-issue dilution, conflicting capital-allocation signals, weak technical trend, absent foreign-flow data, and severe apparent illiquidity. The analytical bear range is IDR 41–48. Approximately IDR 41.41 is an indicator-derived invalidation boundary, not a guaranteed stop fill. Failure to move above IDR 52.23 with improved volume, renewed one-price sessions, adverse capital-action terms, or worsening input-cost news should trigger reassessment or exit.

- **Summary of the Analysis:** **Neutral/Wait.** Do not enter solely because the stock is oversold. Prefer confirmation through a completed close above approximately IDR 52.23 with substantially better participation. The first potential profit zone is IDR 52–54; the reconstructed IDR 61 historical reference is a secondary, lower-probability objective. A reliable executable stop is not estimable. The illustrative risk–reward ratio to IDR 61 from IDR 53 against the IDR 41.41 analytical boundary is only about 0.69, excluding costs. The decisive evidence is the proposed 10% buyback, bearish SuperTrend/ATR and EMA positioning, and exceptionally weak relative volume.

> **Disclaimer:** This analysis is an evidence-based market assessment, not a guarantee of performance or personalized financial advice. Short-term stock prices can move unpredictably, and investors should perform their own due diligence and use position sizing appropriate to their financial situation.