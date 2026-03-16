import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


# -------------------------------------------------------
# 1. LOAD DATA
# -------------------------------------------------------
df = pd.read_csv("medical_examination.csv")


# -------------------------------------------------------
# 2. CREATE OVERWEIGHT COLUMN USING BMI
# -------------------------------------------------------
height_m = df["height"] / 100
bmi = df["weight"] / (height_m ** 2)
df["overweight"] = (bmi > 25).astype(int)


# -------------------------------------------------------
# 3. NORMALIZE CHOLESTEROL AND GLUCOSE
# -------------------------------------------------------
df["cholesterol"] = (df["cholesterol"] > 1).astype(int)
df["gluc"] = (df["gluc"] > 1).astype(int)



# -------------------------------------------------------
# 5. DRAW CATEGORICAL PLOT
# -------------------------------------------------------
def draw_cat_plot():

    # Create DataFrame for cat plot
    df_cat = pd.melt(
        df,
        id_vars=["cardio"],
        value_vars=[
            "cholesterol",
            "gluc",
            "smoke",
            "alco",
            "active",
            "overweight"
        ]
    )

    # Group and count values
    df_cat = (
        df_cat
        .groupby(["cardio", "variable", "value"])
        .size()
        .reset_index(name="total")
    )

    # Draw catplot
    fig = sns.catplot(
        data=df_cat,
        x="variable",
        y="total",
        hue="value",
        col="cardio",
        kind="bar"
    )

    fig = fig.fig

    fig.savefig("catplot.png")
    return fig


# -------------------------------------------------------
# 6. DRAW HEATMAP
# -------------------------------------------------------
def draw_heat_map():

    # Clean the data
    df_heat = df[
        (df["ap_lo"] <= df["ap_hi"]) &
        (df["height"] >= df["height"].quantile(0.025)) &
        (df["height"] <= df["height"].quantile(0.975)) &
        (df["weight"] >= df["weight"].quantile(0.025)) &
        (df["weight"] <= df["weight"].quantile(0.975))
    ]

    # Correlation matrix
    corr = df_heat.corr()

    # Mask for upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Set up matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 10))

    # Draw heatmap
    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt=".1f",
        center=0,
        square=True,
        linewidths=0.5,
        cbar_kws={"shrink": 0.5}
    )

 
    fig.savefig("heatmap.png")
    return fig

    

if __name__ == "__main__":
    draw_cat_plot()
    draw_heat_map()