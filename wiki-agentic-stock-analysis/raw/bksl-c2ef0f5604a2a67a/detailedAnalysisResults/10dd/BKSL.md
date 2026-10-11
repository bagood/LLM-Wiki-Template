**Report generated on:** 25 September 2026, 13:24 WIB (UTC+7)

## 1. Analysis timing and 10-session forecast window

**Company name:** PT Sentul City Tbk

**Ticker and exchange:** BKSL / Indonesia Stock Exchange

**Investor currency:** IDR

**Risk tolerance:** Moderate

**Entry price:** None supplied

**Analysis timestamp:** 25 September 2026, 13:24 WIB

**Market status at analysis:** Friday’s IDX regular session was already in progress. Consequently, 25 September is not counted as a full future session.

**Forecast horizon:** Exactly 10 future IDX trading sessions

**Forecast start:** 28 September 2026 regular open

**Forecast end:** 9 October 2026 regular close

**Exchange time zone:** Asia/Jakarta, WIB (UTC+7)

**Session 1**

**Date:** Monday, 28 September 2026

**Session 2**

**Date:** Tuesday, 29 September 2026

**Session 3**

**Date:** Wednesday, 30 September 2026

**Session 4**

**Date:** Thursday, 1 October 2026

**Session 5**

**Date:** Friday, 2 October 2026

**Session 6**

**Date:** Monday, 5 October 2026

**Session 7**

**Date:** Tuesday, 6 October 2026

**Session 8**

**Date:** Wednesday, 7 October 2026

**Session 9**

**Date:** Thursday, 8 October 2026

**Session 10**

**Date:** Friday, 9 October 2026

**Excluded dates:** 26–27 September and 3–4 October, all weekends

**Scheduled weekday closures:** None identified in September or October 2026

**Calendar status:** Verified against the published IDX 2026 schedule; unexpected closures announced later would require rebuilding the schedule.

**Stock suspension:** No BKSL suspension affecting the scheduled horizon was identified as of the research cut-off. A later trading-status announcement would not extend the 10-exchange-session horizon.

**News research cut-off:** 25 September 2026, approximately 13:24 WIB

**Supplied technical-data cut-off:** Completed IDX regular-session bar dated 24 September 2026

**Forecast expiry:** Regular close on 9 October 2026; it must not be extended without a new analysis and updated completed-session data.

## 2. Input validation and freshness

**Payload shape:** Unambiguous date-keyed JSON object, conceptually normalized to one dated record

**Records supplied:** One

**Sorting result:** 24 September 2026 is the latest and only record

**Required fields:** Present

**Numeric validation:** Open, High, Low, Close, and Volume are finite

**Price validation:** Prices are positive

**OHLC relationship:** Valid; High is at least Open and Close, Low is at most Open and Close, and High exceeds Low

**Volume validation:** Non-negative

**Duplicate dates:** None

**Impossible or future dates:** None

**Explicitly provisional records:** None

**Adjustment basis:** Not supplied

**Volume units:** Not explicitly defined; interpreted as the supplied exchange volume units without conversion

**Indicator definitions:** Not separately supplied; named continuous fields are interpreted by their ordinary directional meaning, and binary fields as `1 = active`, `0 = inactive`

**Null fields:** Foreign-flow and non-regular-market features are null. They are not treated as zero and cannot support a positioning conclusion.

**Corporate-action comparability:** No adjustment metadata was supplied. No cross-date raw-price comparison requiring an adjustment reconciliation was performed.

**Freshness assessment:** Actionable under the Trusted Technical-Data Contract because the record is treated as the immediately preceding completed session. The one-row limitation restricts independent trend reconstruction but does not invalidate the embedded historical indicators.

## 3. Supplied OHLCV and technical snapshot

### Latest completed bar

**Date:** 24 September 2026

**Open:** IDR 69

**High:** IDR 69

**Low:** IDR 64

**Close:** IDR 66

**Volume:** 88,339,700

**Source:** Provided technical dataset

**Candlestick interpretation:** Bearish session; the stock opened at its daily high and closed IDR 3 below the open.

**Open Gap Percent:** 0.0147058824, or approximately +1.47%

**Intraday Return Percent:** -0.0434782609, or approximately -4.35%

**High Low Range Percent:** 0.0757575758, or approximately 7.58%

**Close Location Value:** -0.2, indicating a close in the lower portion of the daily range

### Trend evidence

**ATR Bearish:** 1

**ATR Bullish:** 0

**Interpretation:** The supplied ATR regime flag is bearish. These are condition flags, not ATR price distances.

**Aroon Up:** 0.0

**Aroon Down:** 92.0

**Aroon Oscillator:** -92.0

**Aroon Down Trend:** 1

**Interpretation:** Strongly bearish trend recency; this is one of the clearest adverse signals.

**Plus Directional Index:** 12.0609

**Minus Directional Index:** 22.4888

**Directional Index Spread:** -10.4279

**ADX Value:** 24.3552

**ADX Strong Trend:** 0

**ADX Change 5D:** +4.5219

**Interpretation:** Sellers dominate directionally. ADX is not flagged as a strong trend, but its five-day rise suggests the directional move has been strengthening.

**SuperTrend Bearish:** 1

**SuperTrend Bullish:** 0

**Vortex Spread:** -0.3529

**Vortex Positive Direction:** 0

**Interpretation:** SuperTrend, Vortex, Aroon, and directional-index evidence agree on a bearish trend regime.

**Close to EMA 5D:** -1.44%

**Close to EMA 10D:** -3.27%

**Close to EMA 20D:** -5.70%

**Close to EMA 50D:** -8.01%

**EMA 5D to 20D Spread:** -4.32%

**EMA 10D to 50D Spread:** -4.90%

**Interpretation:** Price is below every supplied EMA reference, and shorter averages are below longer references. That materially weakens the case for buying without reversal confirmation.

### Momentum evidence

**Price Momentum 5D:** -2.94%

**Price Momentum 10D:** -8.33%

**Price Momentum 20D:** -12.00%

**Interpretation:** Momentum is negative across all supplied horizons.

**MACD Non-Near 0 Negative:** 1

**MACD Percent:** -2.52%

**MACD Signal Percent:** -1.47%

**MACD Histogram Percent:** -1.05%

**MACD Histogram Change 5D:** +0.36 percentage point

**Interpretation:** MACD remains bearish, although the improving histogram offers an early and unconfirmed sign that downside momentum may be decelerating.

**RSI Value:** 39.00

**RSI 7:** 36.31

**RSI 21:** 42.06

**RSI 7 Minus 21:** -5.75

**RSI Rate of Change 5:** +2.46

**RSI Rate of Change 10:** -6.51

**Interpretation:** Momentum is weak but not conventionally oversold. The five-day RSI improvement is insufficient to reverse the negative medium-term configuration.

**Stochastic K Value:** 21.43

**Stochastic D Value:** 19.52

**Stochastic K Minus D:** +1.91

**Stochastic Oscillator Oversold:** 0

**Interpretation:** Stochastic is near the lower end of its range with K slightly above D, creating rebound potential but not a supplied oversold signal.

**Fisher Transform:** -2.4285

**Fisher Transform Trigger:** -2.5280

**Fisher Down Trend:** 1

**Fisher Reversal:** 0

**Interpretation:** Fisher remains in a bearish state; the positive spread has not generated a supplied reversal flag.

### Volatility and channel position

**ATR Percent 14D:** 5.91%

**Realized Volatility 5D:** 0.6541

**Realized Volatility 20D:** 0.3796

**Volatility 5D to 20D Ratio:** 1.7234

**Interpretation:** Short-term volatility is elevated relative to the 20-day measure. Price gaps and slippage therefore matter materially.

**Keltner Percent B:** 0.2513

**Donchian Percent B:** 0.2

**Bollinger Percent B:** 0.1386

**Keltner Oversold:** 0

**Donchian Oversold:** 0

**Bollinger Oversold:** 0

**Channel-width condition:** Keltner, Donchian, and Bollinger width-increasing flags all equal 1

**Interpretation:** Price is near the lower portions of all three channels, but none identifies a formal oversold condition. Expanding widths confirm rising movement risk rather than guaranteeing a bounce.

**Distance From 20D High:** -15.38%

**Implied 20-day high:** Approximately IDR 78, calculated as `66 / (1 − 0.153846)`

**Distance From 20D Low:** +4.76%

**Implied 20-day low:** Approximately IDR 63, calculated as `66 / (1 + 0.047619)`

**Distance From 60D High:** -19.51%

**Implied 60-day high:** Approximately IDR 82

**Distance From 60D Low:** +15.79%

**Implied 60-day low:** Approximately IDR 57

**Price ZScore 20D:** -1.4457

**Interpretation:** Price is statistically depressed relative to its supplied 20-day context. That supports rebound potential, but trend confirmation remains absent.

### Volume and money-flow evidence

**Volume Ratio 20D:** 0.6271

**Volume ZScore 20D:** -0.8363

**Volume Change 1D:** -68.34%

**Up Volume Share 20D:** 0.3119

**Interpretation:** Trading participation is below its supplied 20-day norm, and only about 31% of volume is associated with up periods. This undermines the reliability of a bullish reversal.

**On Balance Volume Increasing:** 1

**OBV to MA20 Ratio:** 0.9816

**OBV Change 5D Normalized:** +0.0075

**Accumulation Distribution Line Increasing:** 1

**ADL Change 5D Normalized:** +0.0031

**Interpretation:** OBV and ADL supply modest accumulation evidence, although OBV remains slightly below its 20-day average.

**MFI Value:** 23.57

**MFI Decreasing:** 1

**CMF Value:** -0.1685

**Negative CMF:** 1

**CMF Change 5D:** +0.0677

**Interpretation:** Money flow remains negative and MFI is deteriorating, despite some CMF improvement. The flow group is therefore mixed-to-bearish.

**PVO Value:** -13.8553

**PVO Histogram:** +3.4382

**PVO Histogram Change 5D:** +8.5862

**Interpretation:** Absolute volume momentum is weak, but its rate of deterioration has improved.

**Foreign positioning:** Unavailable because every supplied foreign-flow field is null

**Non-regular/block activity:** Unavailable because the supplied fields are null

## 4. Key company news and catalysts

### Operational update

**Publication date:** 11 September 2026

**Reported period:** August 2026

**Confirmed facts:** Sentul City’s official site published its August newsletter covering community, wellness, and area-development activities.

**Short-term direction:** Mildly positive operational tone

**Likely magnitude:** Low unless accompanied by quantified sales, presales, cash-flow, or project-completion information

**Pricing assessment:** Unknown; one supplied row cannot establish whether these developments were priced in.

**Confirmation evidence needed:** A dated company disclosure containing material sales, handover, contract, financing, or project figures

### Shareholding transaction reported from an IDX disclosure

**Publication date:** 15 September 2026

**Transaction date:** 14 September 2026

**Reported development:** Pasardana reported that PT Samuel Sekuritas Indonesia acquired 2,873,442,600 BKSL shares at a reported IDR 72 for a substitution-repo purpose, increasing direct reported ownership to 5.36%.

**Confirmation status:** Single accessible news report attributing the information to an IDX disclosure; the underlying disclosure was not independently retrieved

**Directional effect:** Uncertain

**Reason:** A substitution-repo transaction is not necessarily an expression of fundamental bullish conviction and may represent financing/custody mechanics.

**Pricing assessment:** The supplied 24 September close of IDR 66 is below the news-reported transaction figure, but that reported price is not used as technical data or a return input.

### Company-news coverage assessment

**Recent material earnings announcement:** Not found in the completed search

**New material contract:** Not found

**Dividend schedule within the horizon:** Not found

**Rights issue, placement, split, or buyback within the horizon:** Not found

**Management change within the horizon:** Not found

**Coverage limitation:** Absence from search results is not proof that no filing exists. No strong company-level catalyst capable of overriding the bearish technical regime was confirmed.

## 5. Indonesia market news

### Bank Indonesia decision

**Decision date:** 23 September 2026

**Publication date:** 23 September 2026

**Confirmed fact:** Bank Indonesia held the BI-Rate at 5.75%, with the Deposit Facility at 4.75% and Lending Facility at 6.50%.

**Policy rationale:** Rupiah stabilization amid strong external headwinds, inflation control, and sustainable growth

**Transmission to BKSL:** Neutral-to-bearish. Stable policy avoids a fresh domestic tightening shock, but a 5.75% policy rate can constrain mortgage affordability, developer financing, and property-sector risk appetite.

### Inflation

**Reference period:** August 2026

**Publication date:** 1 September 2026

**Confirmed fact:** BPS reported headline inflation of 3.19% year over year and 0.21% month over month.

**Transmission to BKSL:** Moderate inflation inside BI’s cited target band is supportive of household stability, but it offers limited relief while financing rates remain elevated.

### Domestic risk conclusion

**Property sensitivity:** High because BKSL is exposed to housing demand, project execution, and financing conditions

**Net domestic effect:** Neutral-to-mildly bearish over ten sessions

**Reason:** The lack of a new rate increase is helpful, but there is no near-term monetary easing catalyst and BI explicitly cites external and currency headwinds.

## 6. Global market news

### US Federal Reserve

**Event date:** 16 September 2026

**Publication date:** 16 September 2026

**Confirmed fact:** The Federal Reserve raised its target range by 25 basis points to 3.75%–4.00%, citing elevated inflation.

**Transmission to BKSL:** Bearish through tighter global liquidity, potential pressure on emerging-market capital flows and IDR stabilization policy, and reduced appetite for speculative or rate-sensitive property equities.

**Directness:** Indirect but material

### Geopolitical and inflation risk

**Recent context:** The Fed and subsequent reporting cited persistent inflation and geopolitical energy pressure.

**Transmission to BKSL:** Higher global inflation or energy costs could sustain restrictive interest rates and raise construction or operating costs.

**Net global effect:** Bearish

**Commodity exposure:** BKSL is not primarily a commodity producer; the principal channel is financing conditions, currency stability, construction inputs, and general risk appetite.

## 7. Integrated technical-and-news assessment

**Technical conclusion:** Bearish trend with limited rebound potential

**News conclusion:** No confirmed company catalyst presently strong enough to negate the trend; macro conditions are not supportive of aggressive property-sector risk taking.

**Potential rebound basis:** Low channel position, 20-day price Z-score of -1.45, modest OBV/ADL improvement, positive Stochastic K-minus-D, and improving MACD/PVO histograms

**Obstacle to rebound:** Negative momentum over 5, 10, and 20 days; Aroon oscillator of -92; bearish SuperTrend and Vortex; negative CMF; below-average volume; and rising short-term volatility

**Regime Persistent:** 1

**Hurst Exponent 100D:** 0.7227

**Interpretation limitation:** These supplied fields suggest persistence, but they do not say that the next move must continue downward. Combined with the existing trend evidence, persistence currently favors caution.

**News/technical agreement:** Broadly bearish. Macro tightening aligns with the weak trend, while the modest operational news and accumulation indicators provide only secondary support.

**Overall bias:** Neutral/Wait rather than immediate long entry

## 8. Near-term catalyst calendar

### Structured-warrant final trading date

**Event:** Final trading date for cash-settled BKSLDRCV6A call warrants

**Expected date:** 29 September 2026, WIB

**Forecast session:** Session 2

**Confirmation status:** Confirmed by KSEI’s 12 June 2026 registration announcement

**Directional effect on BKSL shares:** Uncertain

**Likely magnitude:** Low to potentially moderate intraday, but no effect can be assumed

**Important distinction:** This is a cash-settled structured warrant issued by a securities firm, not a BKSL share issuance; it does not itself dilute BKSL shareholders.

**Confirmation:** Abnormal underlying volume or a decisive price break supported by new supplied data

**Invalidation:** Normal trading with no corresponding volume or price response

### Structured-warrant exercise/expiry

**Event:** BKSLDRCV6A exercise date

**Expected date:** 2 October 2026, WIB

**Forecast session:** Session 5

**Confirmation status:** Confirmed

**Directional effect:** Uncertain

**Likely magnitude:** Unknown and potentially negligible

**Priced-in assessment:** Unknown

### Session-5 review

**Review time:** After the regular close on 2 October 2026

**Review order:** Invalidation first, then catalyst changes, confirmation, liquidity, and execution feasibility

**Required new information:** Completed daily OHLCV and updated indicators supplied by the caller

**Deadline effect:** The review does not restart or extend the original 9 October expiry.

### Sessions 6–10

**Known company catalyst:** None confirmed

**Primary drivers:** Follow-through from the first-week technical response, domestic rates and currency news, global risk appetite, and any newly filed company disclosure

**Required bullish persistence:** Reclaim of IDR 69 followed by improvement in volume participation and money flow

## 9. Bull, base, and bear scenarios

The probabilities below are subjective judgmental estimates, not statistically calibrated probabilities. Targets are derived solely from supplied OHLCV-derived fields and cited catalyst conditions.

### Bull case

**Required conditions:** BKSL reclaims the supplied daily high of IDR 69, negative money flow improves, volume approaches or exceeds its supplied 20-day norm, and no adverse company or macro disclosure emerges

**Session-10 closing range:** IDR 72–78

**Range basis:** IDR 78 is the implied supplied 20-day high; IDR 72 represents a partial recovery toward that level without assuming a full breakout.

**Gross return at IDR 72:** `(72 − 66) / 66 × 100 = +9.09%`

**Gross return at IDR 78:** `(78 − 66) / 66 × 100 = +18.18%`

**Representative price:** IDR 75 midpoint

**Representative gross return:** `(75 − 66) / 66 × 100 = +13.64%`

**Estimated probability:** 25%

### Base case

**Most likely path:** Volatile consolidation or a limited rebound that fails to establish a confirmed trend reversal

**Session-10 closing range:** IDR 64–70

**Range basis:** The latest supplied low is IDR 64, while IDR 69–70 represents the first meaningful reclaim area around the latest high.

**Gross return at IDR 64:** `(64 − 66) / 66 × 100 = −3.03%`

**Gross return at IDR 70:** `(70 − 66) / 66 × 100 = +6.06%`

**Representative price:** IDR 67 midpoint

**Representative gross return:** `(67 − 66) / 66 × 100 = +1.52%`

**Estimated probability:** 45%

### Bear case

**Failure conditions:** A close below the implied 20-day low near IDR 63, persistent negative CMF/MFI, continued below-average participation, or adverse property, funding, legal, regulatory, or macro news

**Session-10 closing range:** IDR 57–63

**Range basis:** IDR 63 is the implied supplied 20-day low; IDR 57 is the implied supplied 60-day low and is also approximately consistent with the supplied negative ATR stop-distance field.

**Gross return at IDR 57:** `(57 − 66) / 66 × 100 = −13.64%`

**Gross return at IDR 63:** `(63 − 66) / 66 × 100 = −4.55%`

**Representative price:** IDR 60 midpoint

**Representative gross return:** `(60 − 66) / 66 × 100 = −9.09%`

**Estimated probability:** 30%

### Probability-weighted result

**Probability total:** 25% + 45% + 30% = 100%

**Expected-return calculation:** `(0.25 × 13.64%) + (0.45 × 1.52%) + (0.30 × −9.09%)`

**Probability-weighted gross expected return:** Approximately +1.36%

**Weighted range using scenario endpoints:** Approximately −3.18% to +5.91%

**Costs excluded:** Brokerage, exchange charges, taxes, slippage, gap losses, and any dividend or corporate-action adjustment

**Investor-currency conversion:** Not applicable; reference and investor currency are both IDR

## 10. Risks, controls, and review checkpoints

### Persistent downtrend

**Probability:** High

**Impact:** High

**Warning indicator:** Failure to reclaim IDR 69, Aroon Down remaining dominant, and continued negative MACD/SuperTrend/Vortex configuration

**Risk-control response:** Do not anticipate a reversal solely because price is near the lower channel.

### Breakdown below the recent range

**Probability:** Medium

**Impact:** High

**Warning indicator:** Completed-session close below the derived 20-day low near IDR 63

**Risk-control response:** Treat such a close as thesis invalidation and reassess rather than averaging down.

### Weak volume and money flow

**Probability:** High

**Impact:** Medium

**Warning indicator:** Volume Ratio 20D remaining below 1, negative CMF, decreasing MFI, or an attempted rally without volume confirmation

**Risk-control response:** Require stronger participation before treating a price rebound as durable.

### Macro financing pressure

**Probability:** Medium

**Impact:** Medium-to-high

**Warning indicator:** Further hawkish Fed news, renewed BI tightening risk, currency-stability stress, or worsening mortgage/credit news

**Risk-control response:** Reduce exposure or avoid new property-sector longs until conditions stabilize.

### Company disclosure and event risk

**Probability:** Medium

**Impact:** High

**Warning indicator:** Unexpected financing, dilution, litigation, land, governance, project-delay, or trading-status announcement

**Risk-control response:** Check official disclosures before every session and reassess immediately after material news.

### Volatility and execution risk

**Probability:** High

**Impact:** Medium-to-high

**Warning indicator:** Five-day volatility remaining well above 20-day volatility, expanding channel widths, gaps, or inability to trade near the intended level

**Risk-control response:** Use limit orders, avoid oversized positions, and recognize that a stop is not a guaranteed fill.

### Data-quality limitation

**Probability:** Certain

**Impact:** Medium

**Warning indicator:** Only one raw daily record, no bid–ask data, no trade-frequency data, null foreign-flow fields, and unspecified adjustment/volume basis

**Risk-control response:** Review again at session 5 with a newly supplied completed bar and updated indicators.

### Trade framework

**Preferred entry zone:** IDR 64–66 only after evidence of rejection of the IDR 63–64 area and improving volume/money flow

**Status:** Conditional, not an immediate recommendation

**Bullish confirmation:** Completed-session close above IDR 69, preferably with Volume Ratio 20D moving toward or above 1 and improving CMF/MFI

**Thesis invalidation:** Completed-session close below approximately IDR 63

**Deeper risk limit:** Approximately IDR 57, derived from the implied 60-day low and broadly consistent with the supplied `ATR Stop Distance Percent` of -13.6597%

**Stop limitation:** IDR 57 is wide for a moderate-risk short-horizon trade and could produce an unattractive loss. The exact semantics of the signed ATR-stop field are not supplied, so it should not be used mechanically.

**First profit-taking zone:** IDR 69–72

**Second profit-taking zone:** IDR 75–78

**Illustrative risk–reward calculation:** Using IDR 65 entry, IDR 63 risk limit, and IDR 72 first target: `(72 − 65) / (65 − 63) = 3.5`

**Risk–reward limitation:** This ratio assumes execution at IDR 65 and IDR 63, neither of which is guaranteed. A close-based invalidation may realize a larger loss after a gap.

**Position sizing:** Keep exposure below normal until confirmation. A numerical position size is unavailable because no capital amount or maximum IDR risk budget was supplied.

**Session 1–5 focus:** Test whether IDR 63–64 holds; watch the structured-warrant dates, volume participation, and any company disclosure.

**Session-5 checkpoint:** Invalidation first, then catalyst status, confirmation above IDR 69, and execution conditions.

**Session 6–10 focus:** Require continued closes above the reclaimed level; a one-day spike without money-flow improvement is insufficient.

**Session-10 action:** Expire this forecast at the 9 October close and conduct a fresh analysis before maintaining it as a new short-term thesis.

## 11. Final assessment

**Overall judgment:** Neutral/Wait

**Rationale:** BKSL has rebound potential because price is near its supplied 20-day low and lower channel region, with modest OBV/ADL and oscillator improvement. However, the dominant evidence remains bearish: Aroon oscillator -92, negative multi-horizon momentum, bearish SuperTrend and Vortex, negative CMF, below-average volume, and an adverse global rate backdrop.

### Strongest bullish evidence

- `Price ZScore 20D: -1.4457` and `Distance From 20D Low: +4.76%` show a depressed position with mean-reversion potential.
- `On Balance Volume Increasing: 1` and `Accumulation Distribution Line Increasing: 1` indicate modest accumulation.
- Improving MACD and PVO histograms suggest the rate of bearish deterioration may be easing.

### Strongest bearish evidence

- `Aroon Oscillator: -92`, `SuperTrend Bearish: 1`, and negative directional/Vortex spreads show broad trend agreement.
- `Price Momentum 5D: -2.94%`, `10D: -8.33%`, and `20D: -12.00%` remain uniformly negative.
- The Fed’s 16 September rate increase and BI’s continued 5.75% policy rate provide no clear financing-tailwind catalyst for a property developer.

**Possibly priced in:** The recent decline may already reflect part of the restrictive-rate environment and the absence of a strong near-term company catalyst. The supplied data cannot determine how completely.

**Most important missing information:** Updated completed bars after 24 September, current official BKSL disclosure coverage, order-book/liquidity depth, foreign flow, and quantified recent operating or sales results

**Single most likely invalidating development:** A completed-session close below the derived IDR 63 level with continued negative money flow

**Adverse-condition sensitivity:** A renewed domestic-rate or currency shock, further global tightening, or adverse company disclosure would shift the judgment toward Avoid.

**Data-source confirmation:** No internet-sourced share price, OHLCV, volume, technical indicator, support/resistance figure, target price, market-flow series, or consensus value was used as a calculation input.

## 12. News and official calendar sources

**Indonesia Stock Exchange**

**Source:** [IDX trading hours and mechanism](https://www.idx.id/en/products-services/trading-hours-and-mechanism/)

**Use:** Official session convention and regular trading hours

**Indonesia Stock Exchange calendar**

**Source:** [Official 2026 trading-holiday calendar listing](https://idxcarbon.co.id/news-announcement)

**Use:** September–October closure verification

**PT Sentul City Tbk**

**Source:** [Sentul City latest updates](https://sentulcity.co.id/latest_updates?newsData=1)

**Publication date:** 11 September 2026 for the August newsletter

**Use:** Recent company operational-news review

**KSEI**

**Source:** [Structured-warrant registration announcement](https://web.ksei.co.id/Announcement/Files/195733_ksei_4076_dir_0626_202606121623.pdf)

**Publication date:** 12 June 2026

**Use:** BKSLDRCV6A trading and exercise dates

**Pasardana**

**Source:** [Reported Samuel Sekuritas BKSL transaction](https://pasardana.id/news/2026/9/15/kembali-serok-bksl-samuel-sekuritas-kini-genggam-8-98-miliar-saham)

**Publication date:** 15 September 2026

**Use:** Single-source report of an ownership transaction attributed to an IDX disclosure

**Bank Indonesia**

**Source:** [BI-Rate held at 5.75%](https://www.bi.go.id/en/publikasi/ruang-media/news-release/Pages/sp_2819326.aspx)

**Event and publication date:** 23 September 2026

**Use:** Domestic monetary-policy context

**BPS-Statistics Indonesia**

**Source:** [August 2026 inflation release](https://www.bps.go.id/en/pressrelease/2026/09/01/2611/the-year-on-year--y-on-y--headline-inflation-in-august-2026-was-recorded-at-3-19-percent-.html)

**Publication date:** 1 September 2026

**Use:** Domestic inflation context

**US Federal Reserve**

**Source:** [16 September 2026 FOMC statement](https://www.federalreserve.gov/newsevents/pressreleases/monetary20260916a.htm)

**Event and publication date:** 16 September 2026

**Use:** Global rates and liquidity context

- **Next 10 Trading Sessions Upside Potential:** The forecast runs from 28 September through 9 October 2026. The latest supplied close is IDR 66 on 24 September 2026; no entry price was provided. The base-case session-10 range is IDR 64–70, equivalent to −3.03% to +6.06%, with a representative +1.52% return. The subjective probability-weighted expected gross return is +1.36%, while the bull case offers +9.09% to +18.18%. Confidence is low-to-moderate. Upside requires IDR 63–64 to hold, a completed-session reclaim above IDR 69, better volume and money flow, and no adverse company, rate, or currency news.

- **Risks Related to the Stock:** The principal risks are a persistent bearish trend, a close below the implied 20-day low near IDR 63, negative CMF and falling MFI, below-average volume, high short-term volatility, restrictive domestic/global rates, and incomplete flow/liquidity data. The bear range is IDR 57–63. A completed close below approximately IDR 63 should trigger reassessment; IDR 57 is the deeper supplied-data-derived risk boundary. Failed rallies below IDR 69, worsening volume/CMF, or adverse official disclosures are exit or no-entry warnings.

- **Summary of the Analysis:** **Neutral/Wait.** A conditional entry zone is IDR 64–66 only after reversal evidence; the cleaner confirmation is a completed close above IDR 69 with improving participation. Profit-taking zones are IDR 69–72 and IDR 75–78. The thesis invalidates below approximately IDR 63, with IDR 57 as a deeper risk boundary. An illustrative IDR 65 entry, IDR 63 risk limit, and IDR 72 target gives a 3.5 risk–reward ratio, excluding costs and gap risk. The most important evidence is the -92 Aroon oscillator, uniformly negative 5/10/20-day momentum, modest OBV/ADL improvement, and restrictive BI/Fed policy conditions.

> **Disclaimer:** This analysis is an evidence-based market assessment, not a guarantee of performance or personalized financial advice. Short-term stock prices can move unpredictably, and investors should perform their own due diligence and use position sizing appropriate to their financial situation.