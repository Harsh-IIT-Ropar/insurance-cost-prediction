import pandas as pd

import model
import plots
import preprocess


def main():
    df = preprocess.load_data()
    print(f"Loaded data: {df.shape[0]} rows, {df.shape[1]} columns")

    X, y = preprocess.prepare_features(df)
    X_train, X_test, y_train, y_test = model.split_data(X, y)
    print(f"Train rows: {len(X_train)}, test rows: {len(X_test)}")

    lin = model.train_model(X_train, y_train)
    y_pred = lin.predict(X_test)

    scores = model.evaluate(y_test, y_pred)
    print("Model: Linear Regression")
    print(f"R2 on test set: {scores['R2']:.4f}")
    print(f"RMSE: {scores['RMSE']:.2f}")
    print(f"MAE: {scores['MAE']:.2f}")

    plots.OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    plots.plot_target_distribution(y, preprocess.TARGET)
    plots.plot_correlation_heatmap(df)
    plots.plot_predicted_vs_actual(y_test, y_pred)
    plots.plot_residuals(y_test, y_pred)
    plots.plot_coefficients(list(X.columns), lin.coef_)

    results = pd.DataFrame(
        {
            "customer_id": df.loc[y_test.index, "customer_id"],
            "actual_cost": y_test,
            "predicted_cost": y_pred,
        }
    )
    results["error"] = results["actual_cost"] - results["predicted_cost"]
    results.to_csv(plots.OUTPUT_DIR / "predictions.csv", index=False)
    print("Saved outputs/predictions.csv")


if __name__ == "__main__":
    main()
