import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def load_data(path="data/medical_insurance_cost_dataset_enhanced.csv"):
    return pd.read_csv(path)

def preprocess(df, target="annual_medical_cost_usd"):
    df = df.drop_duplicates().dropna()
    df = pd.get_dummies(df, drop_first=True)
    X = df.drop(columns=[target])
    y = df[target]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    return X_train, X_test, y_train, y_test
