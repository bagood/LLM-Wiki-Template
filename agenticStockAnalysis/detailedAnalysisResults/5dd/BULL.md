**Report generated on:** 25 September 2026, 06:24:34 UTC / 13:24:34 WIB

## 1. Report timing and exact forecast window

**Company name:** PT Buana Lintas Lautan Tbk

**Ticker and exchange:** BULL / Indonesia Stock Exchange

**Investor currency:** IDR

**Risk tolerance:** Moderate

**Entry price:** None supplied; no execution is assumed

**Analysis timestamp:** 25 September 2026, 13:24:34 WIB

**Market status at analysis:** The 25 September regular session was already underway. It is therefore excluded from the five full future sessions.

**News research cut-off:** 25 September 2026, approximately 13:24 WIB

**Supplied technical-data cut-off:** Completed IDX regular-session bar dated 24 September 2026

**Forecast horizon:** Exactly five future IDX trading sessions

**Forecast begins:** Regular open on 28 September 2026

**Forecast expires:** Regular close on 2 October 2026

### Session 1

**Date:** Monday, 28 September 2026

**Exchange time zone:** Asia/Jakarta, WIB, UTC+7

### Session 2

**Date:** Tuesday, 29 September 2026

**Exchange time zone:** Asia/Jakarta, WIB, UTC+7

### Session 3

**Date:** Wednesday, 30 September 2026

**Exchange time zone:** Asia/Jakarta, WIB, UTC+7

### Session 4

**Date:** Thursday, 1 October 2026

**Exchange time zone:** Asia/Jakarta, WIB, UTC+7

### Session 5

**Date:** Friday, 2 October 2026

**Exchange time zone:** Asia/Jakarta, WIB, UTC+7

**Excluded dates:** 26–27 September, which are Saturday and Sunday

**Holiday check:** The Indonesian government’s official 2026 holiday list contains no national holiday or collective-leave date from 28 September through 2 October. [Kemenko PMK, published 19 September 2025](https://kemenkopmk.go.id/pemerintah-tetapkan-17-hari-libur-nasional-dan-8-hari-cuti-bersama-tahun-2026)

**Calendar status:** Provisional. The government holiday calendar was verified, but a directly accessible IDX-specific 2026 exchange-closure calendar was not located. No unexpected exchange closure is presently identified.

**Stock suspension:** No current BULL suspension notice was found in the reviewed IDX/company sources. This is not an absolute guarantee of continued tradability.

---

## 2. Input validation and data-freshness assessment

**Payload shape:** Unambiguous date-keyed JSON object, conceptually normalized to one dated record

**Sorting result:** One record; latest and only date is 24 September 2026

**Required fields:** Date, Open, High, Low, Close, and Volume are present

**Finite-value validation:** All required values are finite

**Price validation:** All supplied OHLC prices are positive

**Range validation:** High 398 is at least Open 396 and Close 380; Low 380 is no greater than Open or Close; High exceeds Low

**Volume validation:** 162,183,400, non-negative

**Duplicate dates:** None

**Impossible or future dates:** None

**Explicit provisional bars:** None

**Optional null fields:** Foreign-flow and non-regular-market fields are null. This prevents conclusions about foreign positioning or block activity but does not invalidate the payload.

**Historical depth:** One raw OHLCV row. Derived historical indicators are accepted as authoritative features, but raw multi-day price reconstruction is unavailable.

**Adjustment basis:** Not supplied. No split or ex-dividend adjustment can be independently reconciled.

**Latest-row status:** Under the Trusted Technical-Data Contract, the 24 September row is the immediately preceding completed IDX session.

**Actionability:** Current enough for the requested forecast. The report is not classified as stale or insufficient.

**Technical source:** Provided technical dataset

---

## 3. Supplied OHLCV and technical snapshot

### Latest completed bar

**Date:** 24 September 2026

**Open:** IDR 396

**High:** IDR 398

**Low:** IDR 380

**Close:** IDR 380

**Volume:** 162,183,400, with units otherwise unspecified

**Intraday structure:** The share fell from 396 to 380 and closed exactly at the session low.

**Exact supplied field:** `Intraday Return Percent = -0.0404040404040404`

**Interpretation:** Approximately −4.04% from open to close, a materially bearish candle.

**Exact supplied field:** `Close Location Value = -1.0`

**Interpretation:** Maximum negative close location; sellers controlled the close.

**Exact supplied field:** `High Low Range Percent = 0.0473684210526315`

**Interpretation:** The session range was approximately 4.74% of the close, indicating meaningful short-term movement.

### Trend evidence

**Exact supplied field:** `ATR Bullish = 1`

**Exact supplied field:** `ATR Bearish = 0`

**Interpretation:** The supplied binary ATR regime flag remains bullish, but it conflicts with most directional indicators. It is not a numeric ATR distance.

**Exact supplied field:** `Aroon Down = 100.0`

**Exact supplied field:** `Aroon Up = 40.0`

**Exact supplied field:** `Aroon Oscillator = -60.0`

**Exact supplied field:** `Aroon Down Trend = 1`

**Interpretation:** Strong downside recency and bearish trend positioning.

**Exact supplied field:** `Plus Directional Index = 14.3561`

**Exact supplied field:** `Minus Directional Index = 22.4628`

**Exact supplied field:** `ADX Value = 16.6403`

**Interpretation:** Negative directional dominance, but ADX below 20 suggests the trend is not especially strong. This leaves room for whipsaw or a technical rebound.

**Exact supplied field:** `SuperTrend Bearish = 1`

**Exact supplied field:** `Vortex Spread = -0.4963`

**Interpretation:** Both confirm downside direction.

**Exact supplied field:** `Close to EMA 5D = -0.03390`

**Exact supplied field:** `Close to EMA 20D = -0.07996`

**Exact supplied field:** `Close to EMA 50D = -0.08435`

**Exact supplied field:** `EMA 5D to 20D Spread = -0.04768`

**Interpretation:** The close is below every supplied EMA reference, while short-term EMA positioning is below the 20-day reference. Trend alignment is bearish.

**Exact supplied field:** `Hurst Exponent 100D = 0.6500`

**Exact supplied field:** `Regime Persistent = 1`

**Interpretation:** Supplied regime features suggest movements may persist rather than immediately mean-revert. This makes buying solely because the stock is oversold riskier.

### Momentum evidence

**Exact supplied field:** `MACD Non-Near 0 Negative = 1`

**Exact supplied field:** `MACD Percent = -0.02470`

**Exact supplied field:** `MACD Histogram Percent = -0.01260`

**Interpretation:** MACD remains materially negative.

**Exact supplied field:** `MACD Histogram Change 5D = 0.00273`

**Interpretation:** The histogram has improved modestly over five days, an early stabilization hint, but it remains below zero.

**Exact supplied field:** `RSI Value = 36.8420`

**Exact supplied field:** `RSI 7 = 25.8791`

**Exact supplied field:** `RSI 21 = 42.2691`

**Interpretation:** Broad RSI is weak; short RSI is oversold. The large negative short-versus-long spread shows recent momentum deteriorated faster than the medium-term reading.

**Exact supplied field:** `Stochastic K Value = 11.1111`

**Exact supplied field:** `Stochastic D Value = 15.5093`

**Exact supplied field:** `Stochastic Oscillator Oversold = 1`

**Interpretation:** Rebound potential exists, but K remains below D, so a bullish turn is not yet confirmed.

**Exact supplied field:** `Fisher Transform = -2.2140`

**Exact supplied field:** `Fisher Down Trend = 1`

**Exact supplied field:** `Fisher Reversal = 1`

**Interpretation:** The Fisher signal is deeply negative but carries a supplied reversal marker. This is a possible early inflection, not confirmation.

**Exact supplied field:** `Price Momentum 5D = -0.02564`

**Exact supplied field:** `Price Momentum 10D = -0.09953`

**Exact supplied field:** `Price Momentum 20D = -0.13242`

**Interpretation:** Momentum is negative across all supplied horizons and worse over longer lookbacks.

### Channel and volatility evidence

**Exact supplied field:** `Donchian Percent B = -0.02083`

**Exact supplied field:** `Donchian Oversold = 1`

**Exact supplied field:** `Distance From 20D Low = 0.0`

**Interpretation:** The close is at the supplied 20-day low and fractionally below the Donchian lower reference. That supports bounce potential but also warns of breakdown risk.

**Exact supplied field:** `Bollinger Percent B = 0.03381`

**Exact supplied field:** `Keltner Percent B = 0.11576`

**Interpretation:** Price is close to the lower portions of both channel frameworks.

**Exact supplied field:** `Width Bollinger Increasing = 1`

**Exact supplied field:** `Width Donchian Increasing = 1`

**Interpretation:** Price weakness is occurring with expanding price ranges, which can amplify both a continuation decline and a rebound.

**Exact supplied field:** `ATR Percent 14D = 0.0594502`

**Interpretation:** The supplied ATR measure is approximately 5.95% of price. It supports wide scenario ranges but does not predict direction.

**Exact supplied field:** `ATR Stop Distance Percent = 0.0104465`

**Interpretation:** The supplied stop-distance feature equals approximately 1.04%. Its definition is not supplied, so it is used cautiously and not treated as interchangeable with `ATR Percent 14D`.

### Volume and money-flow evidence

**Exact supplied field:** `Volume Ratio 20D = 0.37440`

**Exact supplied field:** `Volume ZScore 20D = -0.8080`

**Exact supplied field:** `Volume Change 5D = -0.7141`

**Interpretation:** Trading activity is well below its encoded historical baseline. The selloff lacks strong volume confirmation, but low participation also weakens any rebound signal.

**Exact supplied field:** `PVO Histogram = -6.2907`

**Exact supplied field:** `PVO Histogram Change 5D = -2.4187`

**Interpretation:** Relative volume momentum is deteriorating.

**Exact supplied field:** `CMF Value = -0.36308`

**Exact supplied field:** `Strong Negative CMF = 1`

**Exact supplied field:** `MFI Value = 22.8867`

**Exact supplied field:** `MFI Decreasing = 1`

**Interpretation:** Strong net distribution and weakening money flow are among the most bearish observations.

**Exact supplied field:** `On Balance Volume Increasing = 1`

**Exact supplied field:** `Accumulation Distribution Line Increasing = 1`

**Interpretation:** OBV and ADL directional flags provide a limited bullish divergence.

**Contradiction:** Their normalized five-day changes are small or negative, and strong-negative CMF plus weak volume carry greater immediate caution.

### Positioning limitations

**Foreign positioning:** Not assessable; all supplied foreign-flow fields are null.

**Non-regular or block activity:** Not assessable; relevant supplied fields are null.

**Liquidity conclusion:** The latest absolute volume is known, but units, turnover history, bid–ask spreads, order-book depth, and tradable float behavior are unavailable. Execution liquidity cannot be fully assessed.

---

## 4. Key company news and catalysts

### First-half financial results

**Reported event:** BULL reported first-half 2026 revenue of approximately US$128.72 million and attributable profit of US$58.38 million, substantially above the corresponding 2025 period.

**Event period:** Six months ended 30 June 2026

**Publication date:** 4 September 2026

**Source status:** Reported independently by BCA Sekuritas/IQPlus and IDNFinancials, and consistent with BULL’s company financial-performance page. [BCA Sekuritas](https://www.bcasekuritas.co.id/en/latest-news/news/buana-lintas-lautan-raih-kenaikan-pendapatan-dan-laba-hingga-juni-2026), [IDNFinancials](https://www.idnfinancials.com/news/68354/bull-profit-owned-by-halim-jusuf-rises-8-4-fold-in-first-half), [BULL financial-performance page](https://www.bull.co.id/investor-relation/financial-performance)

**Directional effect:** Bullish fundamental background

**Five-session relevance:** Moderate. The results are about three weeks old and therefore may already be substantially reflected in expectations.

**Risk qualification:** Liabilities increased and the company continued investing in fleet expansion. Strong results do not ensure a five-session price rebound.

### Tanker rates and fleet expansion

**Reported event:** A dated UOB Kay Hian research report attributed BULL’s first-half growth to elevated spot charter rates and reported fleet expansion from 10 to 12 vessels, with additional vessels expected.

**Publication date:** 9 September 2026

**Directional effect:** Bullish if elevated charter rates persist; uncertain if geopolitical normalization sharply reduces rates.

**Priced-in assessment:** Unknown. The supplied 10-day and 20-day price momentum are sharply negative despite this favorable news, suggesting either substantial prior pricing, profit-taking, or concern about durability.

**Source:** [UOB Kay Hian research release](https://uobkh.com.hk/en/research/company-id-buana-lintas-lautan-09092026)

### Recent analyst optimism

**Reported event:** IDXChannel reported on 10 September that an RHB analyst upgraded 2026 profit expectations because of first-half performance and four new tankers.

**Publication date:** 10 September 2026

**Directional effect:** Bullish sentiment context

**Limitation:** Any internet-reported target price has been excluded from this report’s scenario calculations.

**Source:** [IDXChannel](https://www.idxchannel.com/amp/market-news/prospek-saham-bull-dinilai-masih-menarik-intip-target-terbaru)

### Corporate-disclosure check

**Recent finding:** BULL’s accessible announcements page shows no September corporate-action announcement; the latest displayed 2026 governance disclosure is the 30 June AGMS minutes.

**Five-session implication:** No confirmed earnings release, shareholder meeting, dividend date, placement, split, or other company-specific scheduled event was found for sessions 1–5.

**Source:** [BULL announcements and disclosures](https://bull.co.id/investor-relation/announcement-disclosure)

**Coverage limitation:** IDX disclosure indexing and company-page coverage may be incomplete, so an unindexed announcement remains possible.

---

## 5. Indonesia market news

### Bank Indonesia decision

**Reported event:** Bank Indonesia held the BI Rate at 5.75% after its 22–23 September meeting, citing persistent external pressure and the need to stabilize the rupiah.

**Publication date:** 23 September 2026

**Directional effect for BULL:** Mixed

**Transmission mechanism:** Currency stabilization is favorable for Indonesian risk appetite. Conversely, a relatively firm policy setting and external-pressure language signal constrained domestic liquidity. For BULL, rupiah weakness can complicate IDR investor sentiment and the domestic-currency effect of USD-denominated costs, debt, or revenue; the exact net exposure was not supplied.

**Source:** [Bank Indonesia press release](https://www.bi.go.id/en/publikasi/ruang-media/news-release/Pages/sp_2819326.aspx)

### Domestic financial-system backdrop

**Reported event:** OJK stated on 7 September that the financial-services sector remained stable but highlighted geopolitical uncertainty, global inflation pressure, and disruption to energy distribution.

**Directional effect:** Neutral to cautiously supportive domestically, with elevated external tail risk

**Transmission mechanism:** Stable domestic intermediation supports market functioning, while energy-market disruption is simultaneously positive for tanker demand and negative for broader inflation and risk appetite.

**Source:** [OJK press release, 7 September 2026](https://ojk.go.id/id/berita-dan-kegiatan/siaran-pers/Pages/RDKB-Agustus-2026.aspx)

---

## 6. Global market news

### Tanker-market disruption

**Reported event:** Shipping reports dated 23–25 September described severe Middle East transport disruption, constrained vessel availability, and exceptionally strong tanker earnings.

**Directional effect for BULL:** Directly bullish for spot-charter revenue potential

**Timing:** Active immediately before the forecast window

**Magnitude:** Potentially high for sentiment because BULL’s recent earnings were reported as heavily exposed to spot vessel charters.

**Invalidation:** Credible reopening and normalization of Strait of Hormuz traffic, rapid easing of war-risk premiums, or a sharp fall in tanker utilization.

**Sources:** [The National, 23 September 2026](https://www.thenationalnews.com/business/energy/2026/09/23/oil-tanker-earnings-near-650000-per-day-as-middle-east-disruption-deepens/), [Reuters report published 25 September 2026](https://www.devdiscourse.com/article/international/3982191-gulf-of-oman-ship-to-ship-oil-transfers-reach-limit-as-saudi-exports-surge)

### Oil-supply volatility

**Reported event:** Oil rose sharply on 24 September after a Houthi missile attack revived supply fears, although prices retreated from intraday extremes following reports of discussions about reopening the Strait of Hormuz.

**Directional effect for BULL:** Mixed but initially bullish for tanker-rate expectations

**Transmission mechanism:** Disrupted routes and longer voyages can lift tanker demand and rates. Resolution can reverse that premium quickly, while very high fuel costs can also increase operating expenses.

**Source:** [Reuters report, 24 September 2026](https://www.marketscreener.com/news/oil-prices-jump-4-as-houthis-fire-missiles-at-saudi-arabia-ce785aded08df725)

### Federal Reserve and global yields

**Reported event:** The Federal Reserve raised its policy range by 25 basis points on 16 September. On 24 September, global bond markets remained under pressure amid inflation and further-tightening concerns.

**Directional effect for BULL:** Bearish for broad emerging-market risk appetite

**Transmission mechanism:** Higher US rates and yields can strengthen the dollar, pressure emerging-market capital flows, and raise financing costs. This can offset company-specific tanker optimism.

**Sources:** [Federal Reserve statement, 16 September 2026](https://www.federalreserve.gov/newsevents/pressreleases/monetary20260916a.htm), [Reuters, 24 September 2026](https://www.investing.com/news/economy-news/bond-market-selloff-rumbles-on-ahead-of-trump-and-xi-talks-4915616)

---

## 7. Integrated technical-and-news assessment

**Technical direction:** Bearish but oversold

**News direction:** Company and tanker-industry news is bullish; macro liquidity news is bearish

**Agreement:** Negative price momentum, bearish trend flags, strong-negative CMF, and a close at the daily low agree that sellers retain control.

**Divergence:** Oversold stochastic, RSI 7, Donchian position, Fisher reversal, rising OBV, and rising ADL create a credible rebound setup.

**Key conflict:** Very favorable earnings and tanker-rate news have not produced positive 10-day or 20-day momentum in the supplied features. That is a warning that good news may already be priced in or is being sold.

**Short-term interpretation:** BULL has asymmetric rebound potential from an oversold condition, but the evidence does not yet support chasing. A close back through IDR 398 would provide better confirmation than the current close at IDR 380.

**Confidence:** Low-to-moderate because only one raw bar is supplied, flow fields are absent, and global geopolitical news is exceptionally unstable.

---

## 8. Near-term catalyst calendar

### Catalyst 1

**Event:** Continuing Middle East shipping disruption and tanker-rate news

**Expected timing:** Every forecast session; unscheduled

**Forecast session:** Sessions 1–5

**Confirmation status:** Ongoing and confirmed by multiple recent reports

**Direction:** Bullish for tanker economics, but volatile

**Likely effect:** Potentially immediate and material

**Already priced in:** Unknown; negative supplied momentum suggests the market is not responding cleanly to the favorable backdrop.

**Bullish confirmation:** New evidence of sustained route disruption accompanied by a BULL close above IDR 398 and improving volume participation

**Invalidation:** Credible normalization of routes or tanker capacity

### Catalyst 2

**Event:** Reaction to Bank Indonesia’s rate hold and rupiah-stability stance

**Expected timing:** Sessions 1–2

**Forecast session:** Primarily sessions 1–2

**Confirmation status:** Confirmed policy decision

**Direction:** Mixed

**Likely effect:** Low-to-moderate unless currency or capital-flow pressure intensifies

**Confirmation:** Improved Indonesian risk appetite without renewed currency stress

**Invalidation:** Further external-pressure headlines or capital outflow concerns

### Catalyst 3

**Event:** Continued global reaction to the Fed increase and bond-market selloff

**Expected timing:** Sessions 1–5

**Forecast session:** All sessions

**Confirmation status:** Confirmed policy action; ongoing market reaction

**Direction:** Bearish for broad risk appetite

**Likely effect:** Moderate and capable of overwhelming stock-specific news

**Warning evidence:** Further hawkish communications, higher yields, or a stronger dollar

### Catalyst 4

**Event:** Company-specific scheduled disclosure

**Expected date:** None confirmed within the window

**Forecast session:** Not applicable

**Direction:** Unknown

**Coverage warning:** Investors should recheck IDX and company disclosures before every session.

---

## 9. Bull, base, and bear scenarios

The scenarios classify terminal session-5 outcomes using the technical reference points supplied in the JSON. Their probabilities are subjective judgmental estimates, not statistically calibrated probabilities.

### Bull case

**Required conditions:** IDR 380 holds, oversold momentum reverses, the share closes above the supplied 24 September high of IDR 398, volume participation improves, and tanker-market disruption remains supportive.

**Terminal session-5 price range:** IDR 398–404

**Method:** Lower bound uses the supplied daily high as confirmation. Upper bound approximates one supplied 14-day ATR percentage above the IDR 380 reference: `380 × (1 + 0.0594502) = 402.59`, rounded to a practical range around IDR 404.

**Gross price return at lower bound:** `(398 − 380) / 380 × 100 = 4.74%`

**Gross price return at upper bound:** `(404 − 380) / 380 × 100 = 6.32%`

**Representative price:** IDR 401 midpoint

**Representative return:** `(401 − 380) / 380 × 100 = 5.53%`

**Estimated probability:** 25%

### Base case

**Most likely path:** An oversold bounce or stabilization occurs, but bearish trend and money-flow readings prevent a decisive breakout. The stock finishes between its recent low area and the 24 September high.

**Terminal session-5 price range:** IDR 378–396

**Method:** Range brackets consolidation around the IDR 380 completed-session close while remaining below the IDR 398 confirmation point.

**Gross price return at lower bound:** `(378 − 380) / 380 × 100 = −0.53%`

**Gross price return at upper bound:** `(396 − 380) / 380 × 100 = 4.21%`

**Representative price:** IDR 387 midpoint

**Representative return:** `(387 − 380) / 380 × 100 = 1.84%`

**Estimated probability:** 40%

### Bear case

**Failure conditions:** IDR 380 fails to hold, strong-negative CMF persists, oversold signals do not reverse, or macro/geopolitical news turns against Indonesian risk assets or tanker rates.

**Terminal session-5 price range:** IDR 356–376

**Method:** Upper area is just below the current low and approximately consistent with the supplied `ATR Stop Distance Percent`. The lower boundary approximates one supplied `ATR Percent 14D` below IDR 380: `380 × (1 − 0.0594502) = 357.41`, rounded to IDR 356–358.

**Gross price return at upper bound:** `(376 − 380) / 380 × 100 = −1.05%`

**Gross price return at lower bound:** `(356 − 380) / 380 × 100 = −6.32%`

**Representative price:** IDR 366 midpoint

**Representative return:** `(366 − 380) / 380 × 100 = −3.68%`

**Estimated probability:** 35%

### Probability-weighted expected return

**Probabilities:** 25% bull + 40% base + 35% bear = 100%

**Representative-price calculation:** `(0.25 × 5.53%) + (0.40 × 1.84%) + (0.35 × −3.68%)`

**Probability-weighted expected gross price return:** Approximately +0.83%

**Weighted range caveat:** The expected return uses disclosed scenario midpoints. It is not a forecast of the intrawindow high and does not account for gaps, trading costs, taxes, slippage, dividends, or corporate-action adjustments.

**Investor-currency conversion:** Unnecessary because both security price and investor currency are IDR.

---

## 10. Risk assessment, controls, and review checkpoints

### Risk 1: Downtrend continuation

**Probability:** High

**Potential impact:** High

**Evidence:** Bearish Aroon, SuperTrend, Vortex, MACD, EMA positioning, and negative multi-horizon momentum

**Warning indicator:** Failure to hold IDR 380 or another close at the session low

**Risk-control response:** Do not initiate solely on an oversold reading. Reassess or exit if a confirmed entry subsequently closes below IDR 376.

### Risk 2: Distribution and weak participation

**Probability:** High

**Potential impact:** Medium-to-high

**Evidence:** `CMF Value = -0.3631`, `Strong Negative CMF = 1`, `Volume Ratio 20D = 0.3744`, and negative PVO histogram

**Warning indicator:** Price bounce without improving volume or money flow

**Risk-control response:** Reduce conviction; avoid adding to an unconfirmed rebound.

### Risk 3: “Good news already priced” behavior

**Probability:** Medium

**Potential impact:** High

**Evidence:** Strong earnings and tanker-rate news coexist with negative 10-day and 20-day momentum.

**Warning indicator:** Failure to recover IDR 398 despite further favorable tanker headlines

**Risk-control response:** Treat repeated rejection below 398 as evidence that favorable news is already discounted.

### Risk 4: Geopolitical reversal

**Probability:** Medium

**Potential impact:** High

**Warning indicator:** Confirmed reopening or normalization of Middle East routes and rapid easing in tanker-rate reports

**Risk-control response:** Reassess the bullish catalyst immediately; do not extend the trade beyond session 5.

### Risk 5: Global rates and currency pressure

**Probability:** Medium-to-high

**Potential impact:** Medium-to-high

**Warning indicator:** Additional hawkish Fed news, global bond selling, or signs of renewed rupiah pressure

**Risk-control response:** Require stronger stock-specific confirmation and use smaller-than-normal exposure.

### Risk 6: Execution and data limitations

**Probability:** Medium

**Potential impact:** Medium-to-high

**Warning indicator:** Wide spreads, poor order-book depth, gaps, suspension, or new corporate-action disclosure

**Risk-control response:** Use limit orders and verify live tradability independently. A stop is a risk limit, not a guaranteed fill.

### Trade-control framework

**Preferred entry zone:** IDR 380–384 only after evidence that IDR 380 is holding; otherwise wait

**Alternative confirmation entry:** A completed-session close above IDR 398 with improved volume participation

**Bullish confirmation level:** IDR 398, derived from the latest supplied daily high

**Thesis invalidation level:** IDR 376 on a completed-session closing basis

**Basis for invalidation:** `380 × (1 − 0.0104465) = 376.03`, using the supplied `ATR Stop Distance Percent`; definition ambiguity requires caution.

**Stop-loss or risk limit:** Around IDR 376 after entry near 380–384, subject to live tick rules and execution conditions

**First profit-taking zone:** IDR 398–400

**Second profit-taking zone:** IDR 402–404

**Risk–reward example:** Using entry IDR 382, stop IDR 376, and target IDR 402

**Calculation:** `(402 − 382) / (382 − 376) = 20 / 6 = 3.33`

**Estimated upside-to-downside ratio:** Approximately 3.3:1 before costs

**Qualification:** This ratio applies only if execution near IDR 382 is available and the IDR 376 risk limit is accepted. A gap can produce a worse exit.

**Position sizing:** Moderate-risk investors should use a smaller-than-normal position until IDR 398 is reclaimed. A numerical position size is unavailable because capital and per-trade risk budget were not supplied.

### Horizon review checkpoints

**After session 1:** Check invalidation first, then whether IDR 380 held and whether the rebound attracted better participation.

**After session 2:** Require momentum stabilization; continued closes near session lows weaken the rebound thesis.

**After session 3:** Reassess tanker and geopolitical news. A failure to approach IDR 398 by this point lowers bull-case credibility.

**After session 4:** Protect gains if price has entered IDR 398–404; do not assume the catalyst persists.

**At session 5 close:** Expire this forecast. Do not extend the trade without a new timestamp, schedule, disclosures, and completed-session technical payload.

---

## 11. Final assessment

**Overall judgment:** Neutral/Wait

**Reason:** The oversold setup and favorable tanker news create real upside potential, but trend and flow confirmation are missing. The small positive probability-weighted expected return does not justify an unconditional entry.

### Strongest bullish items

**Bullish item 1:** `Stochastic Oscillator Oversold = 1`, `RSI 7 = 25.8791`, and `Donchian Oversold = 1`

**Bullish item 2:** `Fisher Reversal = 1`, `On Balance Volume Increasing = 1`, and `Accumulation Distribution Line Increasing = 1`

**Bullish item 3:** Recent first-half earnings growth and ongoing Middle East tanker-capacity disruption

### Strongest bearish items

**Bearish item 1:** The share closed at IDR 380, exactly the session low and supplied 20-day low.

**Bearish item 2:** `Strong Negative CMF = 1`, declining MFI, negative PVO, and very low volume ratio

**Bearish item 3:** Negative MACD, Aroon, SuperTrend, Vortex, EMA positioning, and 5/10/20-day momentum

**What may already be priced in:** Strong first-half earnings, fleet expansion, elevated charter rates, and analyst optimism were public before the supplied 24 September bar. The subsequent negative momentum indicates that these positives cannot be treated as undiscovered catalysts.

**Most important uncertainty:** Whether the tanker-rate windfall persists long enough to change BULL’s price trend rather than merely support already-known earnings expectations.

**Single most likely thesis invalidator:** A completed-session close below approximately IDR 376, especially if accompanied by continued negative money flow.

**Adverse-news sensitivity:** A combination of Middle East route normalization, further global rate increases, and rupiah pressure would change the conclusion from Neutral/Wait to Avoid unless BULL had already confirmed above IDR 398.

**Data-source confirmation:** No internet-sourced share price, OHLCV, volume, technical indicator, support/resistance level, market-flow statistic, or analyst target was used as a calculation input. All such calculations use the Provided technical dataset.

---

## 12. News and official calendar sources

**Company source:** [BULL announcements and disclosures](https://bull.co.id/investor-relation/announcement-disclosure)

**Company financial-source page:** [BULL financial performance](https://www.bull.co.id/investor-relation/financial-performance)

**Cross-check of first-half results:** [BCA Sekuritas/IQPlus, 4 September 2026](https://www.bcasekuritas.co.id/en/latest-news/news/buana-lintas-lautan-raih-kenaikan-pendapatan-dan-laba-hingga-juni-2026)

**Independent company-results coverage:** [IDNFinancials, 4 September 2026](https://www.idnfinancials.com/news/68354/bull-profit-owned-by-halim-jusuf-rises-8-4-fold-in-first-half)

**Attributed analyst research:** [UOB Kay Hian, 9 September 2026](https://uobkh.com.hk/en/research/company-id-buana-lintas-lautan-09092026)

**Indonesian macro source:** [Bank Indonesia, 23 September 2026](https://www.bi.go.id/en/publikasi/ruang-media/news-release/Pages/sp_2819326.aspx)

**Indonesian financial-sector source:** [OJK, 7 September 2026](https://ojk.go.id/id/berita-dan-kegiatan/siaran-pers/Pages/RDKB-Agustus-2026.aspx)

**Official holiday source:** [Kemenko PMK 2026 holiday calendar](https://kemenkopmk.go.id/pemerintah-tetapkan-17-hari-libur-nasional-dan-8-hari-cuti-bersama-tahun-2026)

**Global monetary-policy source:** [Federal Reserve, 16 September 2026](https://www.federalreserve.gov/newsevents/pressreleases/monetary20260916a.htm)

**Global risk source:** [Reuters, 24 September 2026](https://www.investing.com/news/economy-news/bond-market-selloff-rumbles-on-ahead-of-trump-and-xi-talks-4915616)

**Tanker-market sources:** [The National, 23 September 2026](https://www.thenationalnews.com/business/energy/2026/09/23/oil-tanker-earnings-near-650000-per-day-as-middle-east-disruption-deepens/), [Reuters coverage, 25 September 2026](https://www.devdiscourse.com/article/international/3982191-gulf-of-oman-ship-to-ship-oil-transfers-reach-limit-as-saudi-exports-surge)

- **Next 5 Trading Sessions Upside Potential:** The forecast runs from 28 September through 2 October 2026. The latest supplied Close is IDR 380 from 24 September 2026; no entry price was supplied. The base-case session-5 range is IDR 378–396, equivalent to −0.53% to +4.21%, with a representative midpoint return of +1.84%. The midpoint-based probability-weighted expected gross return is approximately +0.83%. Bull-case upside is approximately +4.74% to +6.32% toward IDR 398–404. Confidence is low-to-moderate. Upside requires IDR 380 to hold, oversold momentum to reverse, volume and money flow to improve, IDR 398 to be reclaimed, and tanker-market news to remain favorable.

- **Risks Related to the Stock:** The principal risks are persistent bearish trend and MACD signals, strong-negative CMF, falling MFI and volume momentum, a close at the 20-day low, low relative participation, potentially priced-in earnings news, geopolitical normalization, global rate pressure, absent foreign-flow data, and uncertain execution liquidity. The representative bear range is IDR 356–376. A completed-session close below approximately IDR 376 invalidates the rebound thesis. Continued closes at session lows, failure to respond to favorable tanker news, or route-normalization headlines should trigger reassessment or exit.

- **Summary of the Analysis:** **Neutral/Wait.** A conditional entry at IDR 380–384 is reasonable only after the IDR 380 area visibly holds; the safer confirmation is a completed-session close above IDR 398 with better participation. Profit-taking zones are IDR 398–400 and IDR 402–404, with an indicative risk limit near IDR 376. An example using entry IDR 382, stop IDR 376, and target IDR 402 gives an estimated 3.3:1 gross risk–reward ratio. The decisive evidence is the oversold RSI/stochastic/Donchian setup, exceptionally favorable tanker-market news, and—on the other side—the strongly bearish trend alignment and negative money flow.

> **Disclaimer:** This analysis is an evidence-based market assessment, not a guarantee of performance or personalized financial advice. Short-term stock prices can move unpredictably, and investors should perform their own due diligence and use position sizing appropriate to their financial situation.