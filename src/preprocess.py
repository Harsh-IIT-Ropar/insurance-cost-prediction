from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = ROOT / "data" / "medical_insurance_cost_dataset_enhanced.csv"
TARGET = "annual_medical_cost_usd"


def load_data(path=DATA_PATH):
    return pd.read_csv(path)


def prepare_features(df, target=TARGET):
    df = df.copy()
    y = df[target]
    X = df.drop(columns=[target, "customer_id"])

    bp = X["blood_pressure"].str.split("/", expand=True).astype(float)
    X["systolic_bp"] = bp[0]
    X["diastolic_bp"] = bp[1]
    X = X.drop(columns=["blood_pressure"])

    text_cols = [c for c in X.columns if not pd.api.types.is_numeric_dtype(X[c])]
    X = pd.get_dummies(X, columns=text_cols, drop_first=True, dtype=float)
    return X, y
