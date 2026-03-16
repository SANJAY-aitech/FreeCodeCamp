import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress


def draw_plot():
    # ── Load data ────────────────────────────────────────────────────────────
    df = pd.read_csv("epa-sea-level.csv")

    fig, ax = plt.subplots(figsize=(12, 6))

    # ── Scatter plot ─────────────────────────────────────────────────────────
    ax.scatter(
        df["Year"],
        df["CSIRO Adjusted Sea Level"],
        color="#2980b9",
        alpha=0.6,
        s=18,
        label="Observed Data",
        zorder=3,
    )

    # ── Line of best fit (full dataset 1880–2050) ────────────────────────────
    slope1, intercept1, *_ = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    x1 = np.arange(df["Year"].min(), 2051)
    y1 = slope1 * x1 + intercept1

    ax.plot(
        x1, y1,
        color="#e74c3c",
        linewidth=2,
        label=f"Best Fit (1880–2050)  →  {slope1 * 2050 + intercept1:.2f} in by 2050",
    )

    # ── Line of best fit (2000 onwards → 2050) ───────────────────────────────
    df_recent = df[df["Year"] >= 2000]
    slope2, intercept2, *_ = linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])
    x2 = np.arange(2000, 2051)
    y2 = slope2 * x2 + intercept2

    ax.plot(
        x2, y2,
        color="#27ae60",
        linewidth=2,
        linestyle="--",
        label=f"Best Fit (2000–2050)  →  {slope2 * 2050 + intercept2:.2f} in by 2050",
    )

    # ── Mark 2050 predictions ────────────────────────────────────────────────
    pred_full   = slope1 * 2050 + intercept1
    pred_recent = slope2 * 2050 + intercept2

    ax.scatter([2050, 2050], [pred_full, pred_recent],
               color=["#e74c3c", "#27ae60"], s=80, zorder=5, marker="*")

    ax.axvline(2050, color="gray", linewidth=0.8, linestyle=":", alpha=0.6)

    # ── Labels & formatting ──────────────────────────────────────────────────
    ax.set_xlabel("Year", fontsize=12)
    ax.set_ylabel("Sea Level (inches)", fontsize=12)
    ax.set_title("Rise in Sea Level", fontsize=14, fontweight="bold")
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)

    fig.tight_layout()
    fig.savefig("sea_level_plot.png", dpi=150)
    return fig


if __name__ == "__main__":
    draw_plot()
    print("✅  Saved → sea_level_plot.png")
