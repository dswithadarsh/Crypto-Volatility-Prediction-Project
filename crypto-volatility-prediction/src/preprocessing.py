"""
preprocessing.py
Handle missing values and scaling (templates)
"""
import pandas as pd

def clean_data(df):
    """
    Cleans the cryptocurrency dataset.
    Steps:
    1. Sort by symbol + date
    2. Forward fill + backward fill missing values
    3. Remove duplicates
    """
    # Sort properly
    df = df.sort_values(["symbol", "date"])

    # Missing values fill
    df = df.groupby("symbol").apply(lambda x: x.ffill().bfill()).reset_index(drop=True)

    # Remove duplicates
    df = df.drop_duplicates()

    return df


if __name__ == "__main__":
    sample = pd.read_csv("../data/raw/crypto.csv", parse_dates=["date"])
    cleaned = clean_data(sample)
    print(cleaned.isna().sum())
