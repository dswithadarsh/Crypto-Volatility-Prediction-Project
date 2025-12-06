"""
data_loader.py
Simple data loader functions.
"""
import pandas as pd
from pathlib import Path

def load_crypto_data(path):
    """
    Reads the cryptocurrency CSV file and returns a pandas DataFrame.
    Automatically parses the date column.
    """
    path = Path(path)
    df = pd.read_csv(path, parse_dates=["date"])
    return df


if __name__ == "__main__":
    df = load_crypto_data("../data/raw/crypto.csv")
    print(df.head())
    print(df.info())
