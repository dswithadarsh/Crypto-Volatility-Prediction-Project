"""
features.py
Feature engineering utilities.
"""
import pandas as pd
import numpy as np

def add_returns(df):
    df = df.sort_values(['symbol','date'])
    df['return'] = df.groupby('symbol')['close'].pct_change()
    return df

def add_rolling_volatility(df, window=14):
    df['rolling_vol'] = df.groupby('symbol')['return'].rolling(window).std().reset_index(0,drop=True)
    return df

def true_range(df):
    prev_close = df.groupby('symbol')['close'].shift(1)
    tr = pd.concat([
        (df['high'] - df['low']).abs(),
        (df['high'] - prev_close).abs(),
        (df['low'] - prev_close).abs()
    ], axis=1).max(axis=1)
    return tr

def add_ATR(df, window=14):
    df['TR'] = true_range(df)
    df['ATR'] = df.groupby('symbol')['TR'].rolling(window).mean().reset_index(0,drop=True)
    return df

def add_moving_averages(df, windows=[10,30,50]):
    for w in windows:
        df[f'ma_{w}'] = df.groupby('symbol')['close'].transform(lambda x: x.rolling(window=w).mean())
    return df

def add_bollinger(df, window=20, n_std=2):
    rolling_mean = df.groupby('symbol')['close'].transform(lambda x: x.rolling(window).mean())
    rolling_std  = df.groupby('symbol')['close'].transform(lambda x: x.rolling(window).std())
    df['bb_mid'] = rolling_mean
    df['bb_upper'] = rolling_mean + (rolling_std * n_std)
    df['bb_lower'] = rolling_mean - (rolling_std * n_std)
    return df

def add_liquidity(df):
    df['vol_mcap_ratio'] = df['volume'] / (df['market_cap'] + 1e-9)
    df['rolling_vol_mean'] = df.groupby('symbol')['volume'].transform(lambda x: x.rolling(14).mean())
    return df

if __name__ == "__main__":
    df = pd.read_csv("../data/raw/sample_crypto.csv", parse_dates=['date'])
    df = add_returns(df)
    df = add_rolling_volatility(df)
    df = add_ATR(df)
    df = add_moving_averages(df)
    df = add_bollinger(df)
    df = add_liquidity(df)
    print(df.tail().T.head(30))