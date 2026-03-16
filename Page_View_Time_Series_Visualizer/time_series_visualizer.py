import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
from matplotlib.lines import Line2D

# ── Load & Clean ────────────────────────────────────────────────────────────

df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=["date"], index_col="date")

# Remove top and bottom 2.5 %
df = df[
    (df["value"] >= df["value"].quantile(0.025)) &
    (df["value"] <= df["value"].quantile(0.975))
]


# ── 1. LINE CHART ────────────────────────────────────────────────────────────

def draw_line_plot():
    data = df.copy()

    fig, ax = plt.subplots(figsize=(16, 5))

    ax.plot(data.index, data["value"], color="#e74c3c", linewidth=0.8)

    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019", fontsize=14)
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")

    fig.tight_layout()
    fig.savefig("line_plot.png", dpi=150)
    return fig


# ── 2. BAR CHART ─────────────────────────────────────────────────────────────

MONTHS = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]

def draw_bar_plot():
    data = df.copy()
    data["year"]  = data.index.year
    data["month"] = data.index.month

    monthly_avg = (
        data.groupby(["year", "month"])["value"]
        .mean()
        .unstack(level="month")        # columns = month numbers 1-12
    )
    monthly_avg.columns = [MONTHS[m - 1] for m in monthly_avg.columns]

    # Keep only months present in data (column order = Jan → Dec)
    ordered_months = [m for m in MONTHS if m in monthly_avg.columns]
    monthly_avg = monthly_avg[ordered_months]

    fig, ax = plt.subplots(figsize=(12, 7))

    monthly_avg.plot(kind="bar", ax=ax, width=0.8)

    ax.set_title("Average Daily Page Views per Month (Grouped by Year)")
    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")
    ax.legend(title="Months", labels=ordered_months, bbox_to_anchor=(1.01, 1), loc="upper left")
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{int(x):,}"))

    plt.xticks(rotation=45, ha="right")
    fig.tight_layout()
    fig.savefig("bar_plot.png", dpi=150)
    return fig


# ── 3. BOX PLOTS ─────────────────────────────────────────────────────────────

MONTH_ABBR = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

def draw_box_plot():
    data = df.copy().reset_index()
    data["year"]       = data["date"].dt.year
    data["month"]      = data["date"].dt.month
    data["month_abbr"] = pd.Categorical(
        data["date"].dt.strftime("%b"),
        categories=MONTH_ABBR,
        ordered=True,
    )

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 7))

    # ── Year-wise ───────────────────────────────
    sns.boxplot(
        data=data, x="year", y="value",
        ax=ax1,
        palette="Set2",
        flierprops=dict(marker=".", markersize=2, alpha=0.4),
    )
    ax1.set_title("Year-wise Box Plot (Trend)")
    ax1.set_xlabel("Year")
    ax1.set_ylabel("Page Views")
    ax1.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{int(x):,}"))

    # ── Month-wise ──────────────────────────────
    sns.boxplot(
        data=data, x="month_abbr", y="value",
        ax=ax2,
        palette="husl",
        flierprops=dict(marker=".", markersize=2, alpha=0.4),
    )
    ax2.set_title("Month-wise Box Plot (Seasonality)")
    ax2.set_xlabel("Month")
    ax2.set_ylabel("Page Views")
    ax2.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{int(x):,}"))

    fig.tight_layout()
    fig.savefig("box_plot.png", dpi=150)
    return fig
if __name__ == "__main__":
    draw_line_plot()
    draw_bar_plot()
    draw_box_plot()