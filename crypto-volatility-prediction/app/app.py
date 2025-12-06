import streamlit as st
import joblib
import numpy as np

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, "models", "rf_volatility_model.pkl")

model = joblib.load(model_path)


try:
    model = joblib.load(model_path)
    model_loaded = True
except:
    model_loaded = False
    st.error("❌ Model file not found! Please train and save the model first.")

# --- UI Title ---
st.title("🔮 Crypto Volatility Prediction App")
st.write("Enter financial feature values to predict market volatility")

# --- Input Form ---
ATR = st.number_input("ATR value", value=0.01)
ma_10 = st.number_input("10-day Moving Average", value=0.01)
ma_30 = st.number_input("30-day Moving Average", value=0.01)
bb_upper = st.number_input("Bollinger Upper Value", value=0.01)
bb_lower = st.number_input("Bollinger Lower Value", value=0.01)
vol_mcap_ratio = st.number_input("Volume MarketCap Ratio", value=0.01)

if st.button("Predict Volatility"):
    if model_loaded:
        # Convert input to array
        input_data = np.array([[ATR, ma_10, ma_30, bb_upper, bb_lower, vol_mcap_ratio]])
        
        prediction = model.predict(input_data)[0]

        st.success(f"📌 Predicted Volatility = {prediction:.4f}")

        if prediction > 0.02:
            st.warning("⚠️ Market High Risk / High Volatility")
        else:
            st.info("✅ Market Stable / Low Volatility")
