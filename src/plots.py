"""Plotting helpers for the insurance cost project.

Each function draws one chart and saves it as a .png file in the outputs/ folder
(next to src/), so it works on any laptop without absolute paths.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # no display needed; works on any machine
import matplotlib.pyplot as plt
import numpy as np

# outputs/ folder in the repo root, found relative to this file
OUTPUT_DIR = Path(__file__).resolve().parent.parent / "outputs"


def _save(fig, filename, outdir):
    """Create the output folder if needed, save the figure, and print its path."""
    outdir = Path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    path = outdir / filename
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)
    print(f"Saved {path.relative_to(outdir.parent)}")
    return path


def plot_target_distribution(y, target_name="annual_medical_cost_usd", outdir=OUTPUT_DIR):
    """Histogram of the target column, to show how its values are spread."""
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.hist(y, bins=40, edgecolor="black")
    ax.set_xlabel(target_name)
    ax.set_ylabel("Number of customers")
    ax.set_title(f"Distribution of {target_name}")
    return _save(fig, "target_distribution.png", outdir)


def plot_correlation_heatmap(df, outdir=OUTPUT_DIR):
    """Heatmap of correlations between the numeric columns of a DataFrame."""
    corr = df.select_dtypes(include="number").corr()
    fig, ax = plt.subplots(figsize=(9, 7))
    im = ax.imshow(corr.values, cmap="coolwarm", vmin=-1, vmax=1)
    ax.set_xticks(range(len(corr.columns)))
    ax.set_yticks(range(len(corr.columns)))
    ax.set_xticklabels(corr.columns, rotation=90)
    ax.set_yticklabels(corr.columns)
    fig.colorbar(im, ax=ax, label="Correlation")
    ax.set_title("Correlation between numeric columns")
    return _save(fig, "correlation_heatmap.png", outdir)


def plot_predicted_vs_actual(y_true, y_pred, outdir=OUTPUT_DIR):
    """Scatter of real vs predicted values; points near the line mean good predictions."""
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.scatter(y_true, y_pred, alpha=0.4, s=12)
    low = min(y_true.min(), y_pred.min())
    high = max(y_true.max(), y_pred.max())
    ax.plot([low, high], [low, high], color="red", linestyle="--", label="Perfect prediction")
    ax.set_xlabel("Actual value")
    ax.set_ylabel("Predicted value")
    ax.set_title("Predicted vs actual")
    ax.legend()
    return _save(fig, "predicted_vs_actual.png", outdir)


def plot_residuals(y_true, y_pred, outdir=OUTPUT_DIR):
    """Histogram of errors (actual - predicted); should be centred near zero."""
    residuals = np.asarray(y_true) - np.asarray(y_pred)
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.hist(residuals, bins=40, edgecolor="black")
    ax.axvline(0, color="red", linestyle="--")
    ax.set_xlabel("Residual (actual - predicted)")
    ax.set_ylabel("Number of customers")
    ax.set_title("Residuals")
    return _save(fig, "residuals.png", outdir)


def plot_coefficients(feature_names, coefficients, top_n=15, outdir=OUTPUT_DIR):
    """Bar chart of the largest model coefficients (by absolute size)."""
    coefficients = np.asarray(coefficients)
    order = np.argsort(np.abs(coefficients))[::-1][:top_n][::-1]
    names = [feature_names[i] for i in order]
    values = coefficients[order]
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.barh(names, values)
    ax.axvline(0, color="black", linewidth=0.8)
    ax.set_xlabel("Coefficient")
    ax.set_title(f"Top {len(names)} features by coefficient size")
    return _save(fig, "coefficients.png", outdir)
