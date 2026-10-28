from preprocess import load_data, preprocess
from model import train_model, evaluate

def main():
    df = load_data()
    X_train, X_test, y_train, y_test = preprocess(df)
    model = train_model(X_train, y_train)
    metrics, preds = evaluate(model, X_test, y_test)
    print(metrics)

if __name__ == "__main__":
    main()
