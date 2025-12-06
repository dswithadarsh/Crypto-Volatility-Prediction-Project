Low-Level Design (LLD) — Cryptocurrency Volatility Prediction
1. Project file layout (detailed)
crypto-volatility-prediction/
│── data/
│   ├── raw/
│   └── processed/
│
│── src/
│   ├── data_loader.py
│   ├── preprocess.py
│   ├── features.py
│   ├── train.py
│   └── utils.py
│
│── notebooks/
│   └── pipeline.ipynb
│
│── reports/
│   ├── EDA_report.md
│   ├── model_results.md
│   ├── HLD.md
│   └── LLD.md
│
│── diagrams/
│   └── pipeline.png
│
│── models/
│   └── rf_volatility_model.pkl
│
│── app/
│   └── app.py
│
│── requirements.txt
│── README.md

2. Module-level responsibilities
src/data_loader.py

Responsibility: Load CSVs from data/raw/ or data/processed/ and return pandas DataFrame.

Key functions:

load_raw_data(path: str) -> pd.DataFrame

save_processed(df: pd.DataFrame, path: str) -> None

Pseudo:

def load_raw_data(path):
    return pd.read_csv(path, parse_dates=['date'])

src/preprocess.py

Responsibility: Clean data, handle missing values, convert types, scale/normalize if needed.

Key functions:

clean_df(df: pd.DataFrame) -> pd.DataFrame # drop duplicates, fill NA

scale_columns(df, cols, scaler) -> pd.DataFrame # optionally use StandardScaler/MinMax

Important steps:

Drop exact duplicates.

Sort by date and symbol.

Fill missing numeric values (forward-fill or median).

Ensure numeric types for OHLC/volume/mcap columns.

src/features.py

Responsibility: Generate engineered features used by model.

Key functions:

add_atr(df, period=14) -> pd.DataFrame

add_moving_averages(df, windows=[10,30]) -> pd.DataFrame

add_bollinger_bands(df, window=20) -> pd.DataFrame

add_vol_mcap_ratio(df) -> pd.DataFrame

add_rolling_volatility(df, window=10) -> pd.DataFrame # target

Pseudo example (ATR):

def add_atr(df, period=14):
    high_low = df['high'] - df['low']
    high_close = (df['high'] - df['close'].shift()).abs()
    low_close = (df['low'] - df['close'].shift()).abs()
    tr = pd.concat([high_low, high_close, low_close], axis=1).max(axis=1)
    df['ATR'] = tr.rolling(period).mean()
    return df

src/train.py

Responsibility: Prepare features/target, train model, evaluate, save model.

Key functions:

prepare_data(df, feature_cols, target_col) -> X_train, X_test, y_train, y_test

train_rf(X_train, y_train, params) -> trained_model

evaluate_model(model, X_test, y_test) -> dict(metrics)

save_model(model, path)

Hyperparams: n_estimators=200, random_state=42, n_jobs=-1

Evaluation metrics returned: RMSE, MAE, R²

src/utils.py

Responsibility: Shared helper utilities (logging, path helpers).

Key functions:

get_project_root() -> str

safe_load_model(path) -> model or None

plot_actual_vs_pred(y_true, y_pred, save_path=None)

app/app.py (Streamlit)

Responsibility: Simple interactive UI to load model and predict from user inputs.

Key functions/blocks:

Model path resolution using os.path

Input fields for ATR, ma_10, ma_30, bb_upper, bb_lower, vol_mcap_ratio

Predict button, result display, simple threshold-based message (e.g., >0.02 high risk)

3. Data formats & schemas
Raw CSV columns (expected)

date (YYYY-MM-DD), symbol, open, high, low, close, volume, market_cap

Processed Data required by model (sample)

date, symbol, ATR, ma_10, ma_30, bb_upper, bb_lower, vol_mcap_ratio, rolling_vol (target)

All feature columns numeric, rolling_vol numeric.

4. Feature selection used in model

Final features:

ATR, ma_10, ma_30, bb_upper, bb_lower, vol_mcap_ratio
Target:

rolling_vol (e.g., rolling std of returns over 10 days)

5. Training workflow (order of operations)

Load processed CSV: data/processed/crypto_features.csv

Select features and target

Time-based train-test split (80% train, 20% test)

Instantiate RandomForestRegressor with chosen params

Fit on X_train, y_train

Predict y_pred = model.predict(X_test)

Compute metrics (RMSE, MAE, R²)

Save model to models/rf_volatility_model.pkl

Save evaluation plot to reports/actual_vs_predicted.png

6. API / CLI / UI contract

Streamlit UI: no external API required. Inputs -> predicted volatility (float).

CLI test script (optional):

python app/predict_cli.py --atr 0.02 --ma10 0.015 ...

Returns a printed float prediction.

7. Error handling & edge cases

Missing model file: show friendly error in Streamlit and instructions to train.

Invalid numeric input: Streamlit number_input controls numeric types; also validate np.isnan.

Shape mismatch on predict: Validate input shape before calling model.predict.

Corrupt model file: catch exception on joblib.load and provide message.

8. Logging & monitoring (local)

Use Python logging at module level:

import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


Log events:

data load success/failure

model training start/end

model save path

prediction requests (optional count)

9. Reproducibility & requirements

requirements.txt (example)

pandas
numpy
scikit-learn
matplotlib
joblib
streamlit


Run commands

Train (notebook): open notebooks/pipeline.ipynb and run Step 5 cells

Save model: ensure joblib.dump(rf, "models/rf_volatility_model.pkl") executed

Run app: python -m streamlit run app/app.py

10. Testing checklist (before submission)

 data/processed/crypto_features.csv exists and loads

 models/rf_volatility_model.pkl exists in models/

 python -m streamlit run app/app.py opens UI and runs without errors

 reports/actual_vs_predicted.png present

 reports/model_results.md filled with metrics and embedded image

 reports/HLD.md and reports/LLD.md present

11. Security & privacy notes

No credentials used; local-only deployment.

If using real API keys / data, avoid committing keys to repo.

12. Example code snippets (copy-paste ready)
Train & save model (minimal)
from sklearn.ensemble import RandomForestRegressor
import joblib

rf = RandomForestRegressor(n_estimators=200, random_state=42, n_jobs=-1)
rf.fit(X_train, y_train)
joblib.dump(rf, "models/rf_volatility_model.pkl")

Safe load in Streamlit (use in app.py)
import os, joblib
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, "models", "rf_volatility_model.pkl")
model = joblib.load(model_path)

13. Deliverable mapping (what to include in final repo)

src/ — code modules

notebooks/pipeline.ipynb — runnable notebook

models/rf_volatility_model.pkl — trained model

app/app.py — Streamlit UI

reports/ — EDA_report.md, model_results.md, HLD.md, LLD.md, Final_Report.pdf (or MD)

diagrams/pipeline.png — pipeline diagram

requirements.txt, README.md