"""
models.py
Baseline RandomForest model training template.
"""
import joblib
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

def train_rf(X, y, save_path="models/rf_volatility_model.pkl"):
    """
    Train RandomForest on given features X and target y.
    Saves the trained model to save_path.
    """
    # Time-based train-test split
    train_size = int(len(X) * 0.8)
    X_train, X_test = X[:train_size], X[train_size:]
    y_train, y_test = y[:train_size], y[train_size:]

    # Train Random Forest
    rf = RandomForestRegressor(n_estimators=200, random_state=42, n_jobs=-1)
    rf.fit(X_train, y_train)

    # Make predictions
    y_pred = rf.predict(X_test)

    # Print metrics
    print_metrics(y_test, y_pred)

    # Save trained model
    joblib.dump(rf, save_path)
    print(f"Model saved at: {save_path}")

    return rf

def print_metrics(y_true, y_pred):
    rmse = mean_squared_error(y_true, y_pred, squared=False)
    mae = mean_absolute_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    print(f"RMSE: {rmse:.6f}, MAE: {mae:.6f}, R2: {r2:.4f}")

# --------- If run directly ----------
if __name__ == "__main__":
    import pandas as pd
    from src.features import add_returns, add_rolling_volatility, add_ATR, add_moving_averages, add_bollinger, add_liquidity

    # Load raw dataset
    df = pd.read_csv("../data/raw/sample_crypto.csv", parse_dates=['date'])

    # Feature engineering
    df = add_returns(df)
    df = add_rolling_volatility(df)
    df = add_ATR(df)
    df = add_moving_averages(df)
    df = add_bollinger(df)
    df = add_liquidity(df)

    df = df.dropna().reset_index(drop=True)

    # Features & Target
    feature_cols = ['ATR','ma_10','ma_30','bb_upper','bb_lower','vol_mcap_ratio']
    X = df[feature_cols].fillna(0)
    y = df['rolling_vol']

    # Train model
    train_rf(X, y)
