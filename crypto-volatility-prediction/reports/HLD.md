High-Level Design (HLD) Document
Project: Cryptocurrency Volatility Prediction System
1. Objective

The system predicts cryptocurrency price volatility using historical market data, engineered features, and a machine learning model to provide insights for risk assessment.

2. System Components

✔ Data Source (Historical crypto prices)
✔ Data Preprocessing Pipeline
✔ Feature Engineering
✔ Machine Learning Model (Random Forest)
✔ Local Prediction Interface (Streamlit App)

3. Architecture Overview
DATA COLLECTION  
        ↓  
DATA PROCESSING & CLEANING  
        ↓  
FEATURE ENGINEERING  
        ↓  
MODEL TRAINING & EVALUATION  
        ↓  
MODEL SAVING  
        ↓  
LOCAL DEPLOYMENT (Streamlit App)  
        ↓  
USER INPUT → PREDICTION OUTPUT

4. Technology Stack
Layer	Tools Used
Data Handling	Python, Pandas
Feature Engineering	Pandas, NumPy
Model Training	Scikit-Learn (RandomForestRegressor)
Visualization	Matplotlib
Deployment	Streamlit
Model Persistence	Joblib
5. Data Flow Description

✔ Dataset → loaded into Pandas dataframe
✔ Preprocessing applied → missing values handled
✔ New features created → ATR, MA-10, MA-30, Bollinger Bands, Liquidity ratio
✔ Train-test split applied
✔ Model trained
✔ Evaluation metrics computed
✔ Model saved as .pkl
✔ Streamlit UI loads model and predicts volatility for new inputs

6. High-Level Diagram (insert in diagrams folder)
[Dataset]
   ↓
[Preprocessing Module]
   ↓
[Feature Engineering Module]
   ↓
[Model Training Module]
   ↓
[Saved Model File]
   ↓
[Streamlit App UI]
   ↓
[User Input → Prediction Output]

7. Assumptions

✔ Dataset is valid and consistent
✔ Historical patterns help predict future volatility
✔ Engineered features carry predictive information

8. Limitations

✘ Model doesn't incorporate live data
✘ Only Random Forest used, no model comparison performed

9. Outcome

✔ A working prediction pipeline
✔ A deployed local app usability verified