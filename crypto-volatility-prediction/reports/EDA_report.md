EDA Report – Cryptocurrency Volatility Prediction

This report presents the Exploratory Data Analysis (EDA) performed on the cryptocurrency historical dataset used for volatility prediction. The analysis helps us understand trends, price behavior, volume movements, and volatility patterns.

1. Dataset Overview

The dataset contains daily historical price and volume data for multiple cryptocurrencies.

Columns included:

  * date – trading day

  * symbol – cryptocurrency name (BTC, ETH, etc.)

  * open – opening price

  * high – highest price of the day

  * low – lowest price of the day

  * close – closing price

  * volume – total traded volume

  * market_cap – total market value

Basic checks:

  * No missing values after preprocessing

  * Data sorted by symbol → date

  * Correct date format

  * No duplicate rows

2. Summary Statistics

Key summary results:

  * Close price varies significantly across symbols

  * Volume is highly inconsistent and shows heavy spikes

  * Returns (close_pct_change) mostly cluster near zero, indicating short-term stability

  * Volatility (rolling std) shows strong fluctuations

3. Price Trend Analysis

A line plot of closing prices for major cryptocurrencies (BTC, ETH) shows:

✔ Clear long-term price trends
✔ Sudden spikes and drops
✔ Highly volatile behavior, especially during major events/news

This indicates the crypto market is far more unstable compared to traditional markets.

4. Daily Returns Analysis

Daily returns were calculated using:

return = close.pct_change()


Observations:

  * Most returns stay near 0

  * Occasional extreme positive or negative spikes

  * Indicates unpredictable market movements

5. Volatility Analysis

Volatility was measured using 14-day rolling standard deviation of returns:

rolling_vol = returns.rolling(14).std()


Findings:

  * Volatility follows cycles (periods of calm followed by turbulence)

  * High volatility periods align with high-volume trading days

  * BTC and ETH show similar volatility patterns

6. Volume Trend Analysis

  * Trading volume shows sudden abnormal spikes

  * Volume surges often precede or follow large price movements

  * Volume has weak direct correlation with closing price but strong relation with volatility

7. Correlation Analysis

A heatmap between variables (open, high, low, close, volume, market_cap) shows:

✔ strong correlation among OHLC features

(open ↔ high ↔ low ↔ close)

✔ weak correlation between price and volume
✔ rolling volatility has moderate correlation with ATR and Bollinger Band width

(POST feature engineering)

This indicates engineered features are critical for better prediction.

8. Distribution of Returns

Histogram + KDE plot of returns reveals:

  * Heavy tails

  * Not normally distributed

  * Many small movements and few extreme events

  * Typical behavior of high-risk assets

9. Key Insights (Most Important Section)
🔥 Important Insights:

  * Crypto prices are highly volatile and unpredictable.

  * OHLC prices strongly depend on each other.

  * Trading volume acts as an indicator of upcoming volatility.

  * Rolling volatility captures market instability very well.

  * Returns distribution shows many small changes and rare major jumps.

  * Technical indicators (ATR, Bollinger Bands, moving averages) are essential for model improvement.

10. Conclusion

EDA shows that cryptocurrency markets behave non-linearly, with irregular volatility spikes. These findings justify the need for additional technical indicators and advanced ML models to improve volatility prediction accuracy.