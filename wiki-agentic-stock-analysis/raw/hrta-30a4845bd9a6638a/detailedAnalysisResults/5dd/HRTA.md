**Report generated on:** 25 September 2026, 13:17:47 WIB (UTC+7)

## 1. Timing and forecast window

**Company name:** PT Hartadinata Abadi Tbk

**Ticker and exchange:** HRTA / Indonesia Stock Exchange

**Analysis timestamp:** 25 September 2026, 13:16 WIB

**Market status at analysis:** The 25 September session was already in progress. It is therefore excluded from the five full future sessions.

**Forecast horizon:** Exactly 5 trading sessions

**Forecast start:** Monday, 28 September 2026

**Forecast end:** Friday, 2 October 2026, at the regular IDX close

**Investor currency:** Indonesian rupiah

**Risk tolerance:** Moderate

**Entry price:** None supplied; no executed position is assumed

**News research cut-off:** 25 September 2026, 13:17 WIB

**Supplied technical-data cut-off:** Completed regular-session bar dated 24 September 2026

### Session schedule

**Session 1**

**Date:** Monday, 28 September 2026

**Exchange time zone:** WIB, UTC+7

**Session status:** Provisional regular IDX trading date

**Session 2**

**Date:** Tuesday, 29 September 2026

**Exchange time zone:** WIB, UTC+7

**Session status:** Provisional regular IDX trading date

**Session 3**

**Date:** Wednesday, 30 September 2026

**Exchange time zone:** WIB, UTC+7

**Session status:** Provisional regular IDX trading date

**Session 4**

**Date:** Thursday, 1 October 2026

**Exchange time zone:** WIB, UTC+7

**Session status:** Provisional regular IDX trading date

**Session 5**

**Date:** Friday, 2 October 2026

**Exchange time zone:** WIB, UTC+7

**Forecast expiry:** Regular close of session 5

**Excluded dates:** The partly elapsed 25 September session and the weekend of 26–27 September

**Calendar verification:** IDX-hosted event listings confirm activity on 28–30 September and 1 October, but I did not locate a definitive official 2026 exchange-holiday document covering the entire window. No closure or HRTA suspension notice was found. The schedule therefore remains provisional and follows normal IDX weekdays.

## 2. Input validation and freshness

**Payload shape:** Unambiguous date-keyed JSON object, conceptually normalized into one dated record

**Sorting:** The single record becomes the latest record after ascending date normalization

**Duplicate dates:** None

**Impossible or future dates:** None

**Required fields:** Present

**Price validation:** Passed

**OHLC relationship:** `High 2,320 ≥ Open 2,310 and Close 2,310`; `Low 2,260 ≤ Open and Close`; `High ≥ Low`

**Price positivity:** Passed

**Volume validation:** Non-negative finite value

**Optional nulls:** All foreign-flow and non-regular-market fields are null; no foreign or block-positioning conclusion is possible

**Provisional-bar flag:** None supplied

**Adjustment basis:** Not supplied

**Corporate-action comparability:** No adjustment conflict can be established from one row. Scenario returns exclude dividends and other corporate-action adjustments.

**Latest record currency:** IDR, based on the specified investor currency and IDX listing

**Freshness assessment:** Actionable under the Trusted Technical-Data Contract. The 24 September record is accepted as the immediately preceding completed session even though the analysis occurs during 25 September trading.

**Important limitation:** Only one raw daily bar was provided. Historical conclusions rely on the supplied derived features; no independent historical indicator calculation was attempted.

## 3. Supplied OHLCV and technical snapshot

### Latest bar

**Date:** 24 September 2026

**Open:** IDR 2,310

**High:** IDR 2,320

**Low:** IDR 2,260

**Close and market reference price:** IDR 2,310

**Volume:** 7,407,000, with units not specified

**Candle:** Open equaled close, producing a neutral body after a 2.60% intraday high-low range

**Close Location Value:** 0.6667, indicating a close in the upper third of the daily range

**Source:** Provided technical dataset

### Trend evidence

**Bullish conditions:** `ATR Bullish = 1`, `SuperTrend Bullish = 1`, `Positive Direction = 1`, `Plus Directional Index = 26.7535`, and `Minus Directional Index = 21.3015`

**Moving-average positioning:** `Close to EMA 5D = 3.1062%`, `Close to EMA 10D = 4.2378%`, `Close to EMA 20D = 4.7494%`, and `Close to EMA 50D = 6.7952%`

**Average alignment:** `EMA 5D to 20D Spread = 1.5936%` and `EMA 10D to 50D Spread = 2.4534%`

**Bearish contradiction:** `Aroon Up = 16`, `Aroon Down = 80`, `Aroon Oscillator = -64`, and `Aroon Down Trend = 1`

**Additional contradiction:** `Vortex Spread = -0.0278` and `Vortex Positive Direction = 0`

**Trend strength:** `ADX Value = 12.7005`, `ADX Strong Trend = 0`, and `ADX Change 5D = -1.2672`

**Interpretation:** Price is above all supplied EMAs and several binary trend conditions are bullish, but low and declining ADX indicates weak trend persistence. Aroon and Vortex warn that the recovery has not decisively displaced the preceding downswing.

### Momentum evidence

**Short-term momentum:** `Price Momentum 5D = 8.4507%` and `Price Momentum 10D = 4.0541%`

**Longer lookback:** `Price Momentum 20D = -2.1186%`

**MACD:** `MACD Near 0 = 1`, `MACD Percent = 0.8419%`, `MACD Signal Percent = 0.7879%`, and `MACD Histogram Percent = 0.0539%`

**MACD development:** `MACD Histogram Change 5D = 1.3914%`

**RSI:** `RSI Value = 58.9189`, with neither an up-trend nor down-trend flag

**RSI acceleration:** `RSI Rate of Change 5 = 13.0328` and `RSI 7 Minus 21 = 9.1583`

**Stochastic:** `Stochastic K Value = 71.2857`, `Stochastic D Value = 50.7460`, and `Stochastic K Minus D = 20.5397`

**Stochastic caution:** `Stochastic J = 112.3651`, indicating a stretched fast component even though the supplied overbought flag is zero

**Fisher:** `Fisher Spread = 0.6971` and `Fisher Change 5D = 2.5406`, but neither Fisher trend nor reversal flag is active

**Interpretation:** Momentum is improving strongly over five sessions, but the negative 20-day momentum and near-zero MACD show that this is still better characterized as a rebound than a confirmed durable uptrend.

### Volatility and channel evidence

**ATR Percent 14D:** 3.8047%

**ATR Stop Distance Percent:** 10.2437%

**Realized Volatility 5D:** 0.4776

**Realized Volatility 20D:** 0.4035

**Volatility 5D to 20D Ratio:** 1.1835

**Keltner position:** `Keltner Percent B = 0.8042`; not overbought or oversold

**Donchian position:** `Donchian Percent B = 0.7742`; not overbought or oversold

**Bollinger position:** `Bollinger Percent B = 0.8355`; not overbought or oversold

**Width signals:** Keltner and Donchian widths are increasing, while Bollinger width is decreasing

**Interpretation:** Price sits toward the upper part of all three supplied channels, while short-term realized volatility exceeds its 20-day measure. Upside continuation is possible, but risk of abrupt two-sided movement is elevated.

### Volume and money-flow evidence

**Volume Ratio 20D:** 0.9123

**Volume ZScore 20D:** -0.1868

**Volume ZScore 60D:** -0.6050

**Volume Change 1D:** -54.3305%

**Volume Change 5D:** 22.9827%

**OBV:** `On Balance Volume Increasing = 1`, `OBV to MA20 Ratio = 1.0037`, and `OBV Change 5D Normalized = 0.0087`

**MFI:** `MFI Value = 43.6204` and `MFI Increasing = 1`

**CMF:** `CMF Value = -0.0483`, `Negative CMF = 1`, but `CMF Change 5D = 0.0804`

**Accumulation/distribution:** `Accumulation Distribution Line Increasing = 1` and `ADL Change 5D Normalized = 0.0158`

**PVO:** `PVO Value = -13.2621`, `PVO Positive = 0`, but its histogram is positive and improving

**Price-volume divergence:** `Price Volume Divergence 20D = -0.0152`

**Interpretation:** OBV, ADL, MFI, and improving CMF suggest tentative accumulation. However, current volume remains below its 20-day norm, PVO is negative, and the latest daily volume fell sharply. Participation does not yet confirm the strength of the price rebound.

### Regime and positioning

**Price ZScore 20D:** 1.3419

**Price ZScore 60D:** 1.2395

**Choppiness Index 14D:** 55.4461

**Hurst Exponent 100D:** 0.4790

**Regime flags:** Trending, choppy, persistent, and mean-reverting flags are all zero

**Interpretation:** Price is relatively elevated versus its supplied historical distributions, while the Hurst value near 0.5 and weak ADX argue against assuming reliable trend continuation.

**Foreign positioning:** Not estimable because every supplied foreign-flow field is null

**Non-regular activity:** Not estimable because every corresponding field is null

## 4. Key company news and catalysts

### Freeport domestic-gold supply agreement

**Event date:** Initial 50-kilogram delivery occurred on 16 September 2026

**Publication date:** 24 September 2026

**Reported development:** HRTA entered a spot gold-bar purchase arrangement with PT Freeport Indonesia and received an initial 50 kilograms of 99.99%-pure cast bars. HRTA said delivery would proceed in stages according to requirements and agreements.

**Directional effect:** Bullish

**Transmission mechanism:** A domestic, documented raw-material source can improve supply reliability and operating flexibility for bullion and jewelry products.

**Near-term timing:** The announcement was published after the 24 September technical bar and after the regular close. Its first possible market reaction was the partly elapsed 25 September session, so by session 1 it may already be partly incorporated.

**Magnitude:** Moderate narrative catalyst; the disclosed initial shipment is not enough by itself to quantify earnings impact.

**Confirmation evidence:** Follow-on delivery volumes, measurable production or sales expansion, and price continuation with above-normal volume

**Invalidation evidence:** No meaningful follow-on volume, adverse commercial terms, or a failure of price and volume to confirm

**Sources:** [IDX Channel, published 24 September 2026](https://www.idxchannel.com/market-news/hartadinata-hrta-jalin-kerja-sama-pembelian-emas-murni-dengan-freeport/all); [HRTA-affiliated announcement, published 24 September 2026](https://gadaihartadinataabadi.com/2026/09/24/perkuat-ketersediaan-emas-murni-hartadinata-gandeng-freeport/)

### Private placement proposal

**Announcement date:** 9 September 2026

**Publication dates:** 10 September 2026

**Proposal:** Up to approximately 460.5 million new shares, described by reports as roughly 9.09%–10% of existing issued capital, principally for working capital

**Shareholder meeting:** 16 October 2026

**Forecast-window status:** Outside the five-session window

**Directional effect:** Mixed to bearish in the short term

**Positive channel:** Additional working capital could support expansion

**Negative channel:** Prospective dilution and uncertainty about issue price and investor participation can cap rerating

**Priced-in assessment:** Unknown. The technical dataset shows a strong five-day rebound but negative 20-day momentum, which is consistent with mixed digestion rather than conclusive pricing.

**Confirmation evidence:** Favorable issue terms, credible use-of-proceeds detail, and evidence that incremental returns exceed dilution

**Invalidation evidence:** Deeply discounted issuance, weak participation, or materially greater dilution than expected

**Sources:** [Bisnis Indonesia, published 10 September 2026](https://market.bisnis.com/read/20260910/192/2002973/gelar-private-placement-hartadinata-hrta-tambah-modal-kerja); [IDNFinancials, published 10 September 2026](https://www.idnfinancials.com/id/news/68642/hrta-jajaki-pendanaan-jumbo-lewat-private-placement-9-09-saham)

### First-half performance

**Event period:** Six months ended 30 June 2026

**Publication dates:** 4 and 14 August 2026

**Reported news:** First-half net sales were reported at approximately IDR33.81 trillion, up 124.61% year over year, while attributable profit was reported at IDR700.01 billion, up 100.86%.

**Directional effect:** Fundamentally bullish but largely established news rather than a fresh five-session catalyst

**Key exposure:** Reports said wholesale sales—including financial institutions and bullion banks—dominated the sales mix, creating concentration as well as growth potential.

**Verification:** The company investor-relations page lists its consolidated June 2026 report and first-half earnings materials.

**Sources:** [ANTARA, published 4 August 2026](https://www.antaranews.com/berita/5678611/hrta-kantongi-laba-rp70001-m-pada-semester-i-2026-naik-10086-persen); [Katadata, published 14 August 2026](https://databoks.katadata.co.id/pasar/statistik/6a7e7641799b3/laba-emiten-penjual-logam-mulia-hrta-melonjak-100-pada-semester-i-2026); [HRTA investor relations](https://hartadinataabadi.co.id/financial-information)

## 5. Indonesia market news

### Bank Indonesia decision

**Decision date:** 23 September 2026

**Publication date:** 23 September 2026, 14:30 WIB

**Decision:** BI retained its policy rate at 5.75%

**Policy rationale:** Rupiah stabilization amid strong external pressure, while supporting sustainable growth

**Effect on HRTA:** Mixed

**Positive channel:** Measures intended to stabilize the rupiah could reduce imported-cost volatility and domestic financial-market stress.

**Negative channel:** Relatively tight rates can constrain risk appetite and increase financing costs. A weaker rupiah can also increase local gold prices and investment demand, but may raise working-capital needs for a gold distributor.

**Source:** [Bank Indonesia press release, 23 September 2026](https://www.bi.go.id/id/publikasi/ruang-media/news-release/Pages/sp_2819326.aspx)

### Domestic gold backdrop

**Publication date:** Early September 2026

**Reported development:** The Ministry of Trade said the gold export reference price for the first half of September rose, attributing the move to strong global demand, constrained supply, lower international bond yields, and safe-haven demand.

**Effect on HRTA:** Generally positive for bullion interest and nominal sales values, but potentially negative for inventory funding requirements and consumer affordability.

**Window relevance:** Background rather than a newly scheduled catalyst.

**Source:** [Indonesia Ministry of Trade](https://www.kemendag.go.id/berita/pojok-media/harga-patokan-ekspor-emas-naik)

## 6. Global market news

### Gold and monetary-policy pressure

**Publication date:** 25 September 2026

**Reported condition:** Reuters reported that gold was heading toward a weekly loss as a stronger US dollar and expectations of sustained high Federal Reserve rates weighed on bullion.

**Direct connection to HRTA:** High. HRTA’s products and working capital are tied to gold demand and inventory economics.

**Positive channel:** Continuing geopolitical and inflation uncertainty preserves safe-haven demand.

**Negative channel:** A stronger dollar and higher-for-longer rates can pressure international gold sentiment. Rapid gold-price movements can also raise inventory, hedging, and affordability risks even when nominal sales remain strong.

**Source:** [Reuters report republished by MarketScreener, 25 September 2026](https://ca.marketscreener.com/news/gold-heads-for-weekly-loss-as-stronger-dollar-fed-rate-outlook-weighs-ce785adfdb8fff22)

## 7. Integrated technical-and-news assessment

**Technical direction:** Mildly bullish rebound

**Trend quality:** Weak

**Momentum quality:** Positive over 5–10 days, negative over 20 days

**Volume confirmation:** Incomplete

**News impulse:** Positive Freeport supply-chain news, counterbalanced by prospective dilution and a less supportive global gold-rate backdrop

**Most important bullish alignment:** Price is above all supplied EMAs, short-term momentum is positive, and the Freeport agreement strengthens the supply narrative.

**Most important contradiction:** Aroon remains bearish, ADX is only 12.7, CMF is negative, and trading volume is below its 20-day norm.

**Overall interpretation:** HRTA has credible upside potential, but the evidence does not support chasing the stock. The latest rally is not yet a strong, volume-confirmed trend, while prospective dilution and volatile gold conditions impair the risk-adjusted payoff.

## 8. Near-term catalyst calendar

### Supply-agreement digestion

**Expected timing:** Sessions 1–2, after any reaction already occurring on 25 September

**Confirmation status:** Agreement and initial delivery reported; financial impact unquantified

**Directional effect:** Bullish

**Likely magnitude:** Low to moderate unless accompanied by follow-on volume or commercial detail

**Already priced in:** Unknown and potentially partly priced by session 1

**Confirmation:** Close above the derived 20-day high with stronger volume participation

**Invalidation:** Failure to hold the latest low or continued subnormal volume

### Unscheduled gold, dollar, and geopolitical headlines

**Expected timing:** Any of sessions 1–5

**Confirmation status:** Event-dependent

**Directional effect:** Uncertain

**Likely magnitude:** Potentially high because short-term volatility is already elevated

**Confirmation:** Sustained favorable bullion news accompanied by HRTA price and volume confirmation

**Invalidation:** Stronger-dollar/higher-rate news combined with failure of HRTA momentum

### Private-placement meeting

**Expected event date:** 16 October 2026

**Forecast session:** Outside the window

**Directional effect:** Uncertain to bearish before terms are clarified

**Likely magnitude:** Moderate

**Monitoring relevance:** Headlines about issue price, investor, or revised size could emerge before the meeting

## 9. Bull, base, and bear scenarios

All scenarios describe the closing price at the end of session 5. Ranges are derived only from supplied technical distances and cited news—not online price targets.

### Bull case

**Required conditions:** The Freeport agreement attracts continued positive attention; gold-related sentiment stabilizes; HRTA clears the supplied 20-day high; and participation improves from `Volume Ratio 20D = 0.9123`

**Price target or range:** IDR2,410–2,470

**Derivation:** The upper boundary is the supplied implied 60-day high: `2,310 / (1 − 0.0647773) ≈ 2,470`. The lower boundary is an intermediate extension between the implied 20-day and 60-day highs.

**Gross price return at IDR2,410:** `(2,410 − 2,310) / 2,310 × 100 = 4.33%`

**Gross price return at IDR2,470:** `(2,470 − 2,310) / 2,310 × 100 = 6.93%`

**Representative price:** IDR2,440

**Representative gross return:** `(2,440 − 2,310) / 2,310 × 100 = 5.63%`

**Estimated probability:** 30%, subjective and not statistically calibrated

### Base case

**Most likely path:** Momentum remains constructive but weak ADX, bearish Aroon, subdued volume, dilution uncertainty, and global gold pressure prevent a decisive breakout

**Price target or range:** IDR2,300–2,370

**Derivation:** The upper boundary is the implied 20-day high: `2,310 / (1 − 0.0253165) ≈ 2,370`. The lower boundary represents consolidation close to the supplied market reference.

**Gross price return at IDR2,300:** `(2,300 − 2,310) / 2,310 × 100 = −0.43%`

**Gross price return at IDR2,370:** `(2,370 − 2,310) / 2,310 × 100 = 2.60%`

**Representative price:** IDR2,335

**Representative gross return:** `(2,335 − 2,310) / 2,310 × 100 = 1.08%`

**Estimated probability:** 45%, subjective and not statistically calibrated

### Bear case

**Failure conditions:** The 24 September low fails, volume-flow indicators deteriorate, dilution concerns intensify, or global gold sentiment weakens materially

**Downside target or range:** IDR2,070–2,180

**Derivation:** IDR2,070 is the supplied implied 20-day low: `2,310 / (1 + 0.1159420) ≈ 2,070`. IDR2,180 is an intermediate retracement within that supplied range.

**Gross price return at IDR2,070:** `(2,070 − 2,310) / 2,310 × 100 = −10.39%`

**Gross price return at IDR2,180:** `(2,180 − 2,310) / 2,310 × 100 = −5.63%`

**Representative price:** IDR2,125

**Representative gross return:** `(2,125 − 2,310) / 2,310 × 100 = −8.01%`

**Estimated probability:** 25%, subjective and not statistically calibrated

### Probability-weighted result

**Probability total:** 30% + 45% + 25% = 100%

**Representative expected return:** `(0.30 × 5.63%) + (0.45 × 1.08%) + (0.25 × −8.01%) = approximately +0.17%`

**Weighted range using scenario endpoints:** Approximately −1.49% to +1.84%

**Return type:** Gross price return from IDR2,310

**Excluded:** Brokerage, exchange fees, taxes, slippage, gap risk, dividends, and corporate-action adjustments

**Interpretation:** Expected upside is positive but marginal, and the downside distribution is materially wider than the base-case upside.

## 10. Risk assessment and controls

### Weak trend confirmation

**Probability:** High

**Potential impact:** Medium

**Warning indicator:** Failure to clear IDR2,370 while ADX remains weak and Aroon Down stays dominant

**Risk-control response:** Do not chase an unconfirmed breakout; require improved price and volume confirmation

### Dilution and financing uncertainty

**Probability:** Medium

**Potential impact:** High

**Warning indicator:** Discounted placement terms, an unexpectedly large issuance, or unclear return on working capital

**Risk-control response:** Reduce exposure before material placement-term announcements and reassess after definitive documentation

### Gold, dollar, and rate shock

**Probability:** Medium

**Potential impact:** High

**Warning indicator:** Further adverse bullion news, a stronger-dollar/higher-rate shift, or rising inventory-financing pressure

**Risk-control response:** Keep position size moderate and avoid holding through unquantifiable headline risk without a valid stop plan

### Incomplete volume and flow confirmation

**Probability:** High

**Potential impact:** Medium

**Warning indicator:** Volume remains below its 20-day norm, CMF stays negative, or OBV and ADL turn down

**Risk-control response:** Demand participation improvement before treating a price breakout as reliable

### Data and liquidity risk

**Probability:** Medium

**Potential impact:** Medium to high

**Warning indicator:** Large gaps, inability to transact near the intended price, suspension, or a divergence between price movement and supplied volume features

**Risk-control response:** Use limit orders where practical and recognize that a stop is not a guaranteed fill

### Trade-control levels

**Preferred entry zone:** IDR2,260–2,310, only if a newly completed bar shows that this area holds and volume/flow do not deteriorate

**Evidence:** IDR2,260 is the latest supplied low; IDR2,310 is the supplied close

**Bullish confirmation level:** A completed close above IDR2,370, the implied supplied 20-day high, preferably with volume ratio above its current 0.9123

**First profit-taking zone:** Around IDR2,370

**Second profit-taking zone:** IDR2,410–2,470

**Invalidation level:** A completed close below approximately IDR2,070

**Stop/risk-limit basis:** IDR2,070 aligns with both the implied supplied 20-day low and the ATR-derived risk distance. Applying `ATR Stop Distance Percent = 10.2437%` to IDR2,310 gives approximately IDR2,073.

**Execution warning:** A stop trigger does not guarantee execution at IDR2,070 during a gap, price-limit condition, or suspension.

**Risk–reward from IDR2,310:** `(2,470 − 2,310) / (2,310 − 2,070) = 0.67`

**Risk–reward from IDR2,260:** `(2,470 − 2,260) / (2,260 − 2,070) = 1.11`

**Assessment:** Neither ratio is compelling for moderate risk, especially before costs. This supports waiting for a better setup rather than immediate entry.

**Position sizing:** Keep exposure smaller than a normal moderate-risk position until volume confirms. A numerical size is unavailable because capital and per-trade risk budgets were not supplied.

### Review checkpoints

**After each completed session:** Check invalidation first, followed by catalyst changes, price confirmation, volume/flow confirmation, and execution feasibility.

**Session-5 close:** Expire this forecast. Do not extend the thesis without a new timestamp, schedule, and completed technical bar.

## 11. Final assessment

**Overall judgment:** Neutral/Wait

**Forecast confidence:** Low to moderate

**Why:** The short-term rebound, EMA positioning, improving momentum, and Freeport supply agreement create real upside optionality. But weak ADX, bearish Aroon, subnormal volume, negative CMF, rising short-term volatility, and prospective dilution leave the risk-adjusted return unattractive.

### Thesis challenge

**Strongest bullish item 1:** `Price Momentum 5D = 8.4507%` with price above every supplied EMA

**Strongest bullish item 2:** OBV and accumulation/distribution are increasing, while MFI and CMF direction have improved

**Strongest bullish item 3:** The reported Freeport agreement adds a domestic 99.99%-pure gold source and an initial documented delivery

**Strongest bearish item 1:** `Aroon Oscillator = −64`, `Aroon Down Trend = 1`, and negative Vortex spread

**Strongest bearish item 2:** `ADX Value = 12.7005` and below-normal volume show weak trend confirmation

**Strongest bearish item 3:** Private-placement dilution uncertainty and a stronger-dollar/higher-rate global backdrop

**Possibly priced in:** First-half earnings growth and at least part of the Freeport supply announcement; the extent is unknown

**Most important missing information:** Completed 25 September bar, updated volume/flow confirmation, definitive private-placement terms, and actual economics of the Freeport arrangement

**Single most likely invalidator:** A completed close below IDR2,070, especially alongside weakening OBV, ADL, or CMF

**Adverse-environment test:** The conclusion would become more bearish under simultaneous rupiah stress, higher global rates, weaker gold demand, or unfavorable placement terms. It would improve only after a confirmed breakout with stronger participation.

**Market-data compliance:** No internet-sourced share price, OHLCV, technical indicator, support/resistance level, target price, or flow statistic was used as a calculation input. All such inputs came exclusively from the Provided technical dataset.

## 12. News and official calendar sources

**Company sources:** [HRTA investor-relations materials](https://hartadinataabadi.co.id/company-update); [HRTA financial-information page](https://hartadinataabadi.co.id/financial-information)

**Freeport agreement:** [IDX Channel, 24 September 2026](https://www.idxchannel.com/market-news/hartadinata-hrta-jalin-kerja-sama-pembelian-emas-murni-dengan-freeport/all); [HRTA-affiliated announcement, 24 September 2026](https://gadaihartadinataabadi.com/2026/09/24/perkuat-ketersediaan-emas-murni-hartadinata-gandeng-freeport/)

**Private placement:** [Bisnis Indonesia, 10 September 2026](https://market.bisnis.com/read/20260910/192/2002973/gelar-private-placement-hartadinata-hrta-tambah-modal-kerja); [IDNFinancials, 10 September 2026](https://www.idnfinancials.com/id/news/68642/hrta-jajaki-pendanaan-jumbo-lewat-private-placement-9-09-saham)

**First-half performance:** [ANTARA, 4 August 2026](https://www.antaranews.com/berita/5678611/hrta-kantongi-laba-rp70001-m-pada-semester-i-2026-naik-10086-persen); [Katadata, 14 August 2026](https://databoks.katadata.co.id/pasar/statistik/6a7e7641799b3/laba-emiten-penjual-logam-mulia-hrta-melonjak-100-pada-semester-i-2026)

**Indonesia macroeconomic news:** [Bank Indonesia, 23 September 2026](https://www.bi.go.id/id/publikasi/ruang-media/news-release/Pages/sp_2819326.aspx); [Ministry of Trade gold-reference announcement](https://www.kemendag.go.id/berita/pojok-media/harga-patokan-ekspor-emas-naik)

**Global gold news:** [Reuters via MarketScreener, 25 September 2026](https://ca.marketscreener.com/news/gold-heads-for-weekly-loss-as-stronger-dollar-fed-rate-outlook-weighs-ce785adfdb8fff22)

**Calendar evidence:** [IDX-hosted RDIS events](https://rdis.idx.co.id/id/events?page=1)

- **Next 5 Trading Sessions Upside Potential:** The forecast runs from 28 September through 2 October 2026. The latest supplied Close is IDR2,310 on 24 September; no entry price was supplied. The base case is IDR2,300–2,370, equivalent to −0.43% to +2.60%, with a representative +1.08% return. The probability-weighted representative return is approximately +0.17%; the bull case offers +4.33% to +6.93%. Confidence is low to moderate. Upside requires a completed break above IDR2,370, improved volume from its current below-normal level, stable gold sentiment, and sustained positive interpretation of the Freeport agreement.

- **Risks Related to the Stock:** The major risks are prospective private-placement dilution, weak trend strength, bearish Aroon/Vortex signals, negative CMF, subnormal volume, elevated short-term volatility, adverse dollar/rate/gold news, and missing foreign-flow information. The defensible bear range is IDR2,070–2,180, while a completed close below approximately IDR2,070 invalidates the thesis. Failure at IDR2,370, deteriorating OBV/ADL/CMF, adverse placement terms, or large execution gaps should trigger reassessment or exit.

- **Summary of the Analysis:** **Neutral/Wait.** A conditional entry zone is IDR2,260–2,310 only after evidence that it holds; stronger bullish confirmation requires a completed close above IDR2,370 with better volume. Profit-taking zones are around IDR2,370 and IDR2,410–2,470, with an approximately IDR2,070 risk limit. The estimated reward-to-risk ratio is only 0.67 from IDR2,310 or 1.11 from IDR2,260, before costs. The decisive evidence is the strong five-day momentum and above-EMA positioning, the positive Freeport supply agreement, and—on the other side—the weak ADX, bearish Aroon, and incomplete volume confirmation.

> **Disclaimer:** This analysis is an evidence-based market assessment, not a guarantee of performance or personalized financial advice. Short-term stock prices can move unpredictably, and investors should perform their own due diligence and use position sizing appropriate to their financial situation.