import pandas as pd

# --------------------------------------------------
# 1. LOAD DATA
# --------------------------------------------------
df = pd.read_csv("medical_examination.csv")

print("Original shape:", df.shape)


# --------------------------------------------------
# 2. CLEAN COLUMN NAMES (optional but good practice)
# --------------------------------------------------
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)


# --------------------------------------------------
# 3. REMOVE DUPLICATES
# --------------------------------------------------
df = df.drop_duplicates().reset_index(drop=True)


# --------------------------------------------------
# 4. HANDLE MISSING VALUES (if any)
# --------------------------------------------------
numeric_cols = df.select_dtypes(include="number").columns

for col in numeric_cols:
    if df[col].isnull().sum() > 0:
        df[col] = df[col].fillna(df[col].median())


# --------------------------------------------------
# 5. CREATE OVERWEIGHT COLUMN USING BMI
# --------------------------------------------------
height_m = df["height"] / 100

bmi = df["weight"] / (height_m ** 2)

df["overweight"] = (bmi > 25).astype(int)


# --------------------------------------------------
# 6. NORMALIZE CHOLESTEROL AND GLUCOSE
# --------------------------------------------------
df["cholesterol"] = (df["cholesterol"] > 1).astype(int)
df["gluc"] = (df["gluc"] > 1).astype(int)


# --------------------------------------------------
# 7. REMOVE INVALID BLOOD PRESSURE
# --------------------------------------------------
df = df[df["ap_lo"] <= df["ap_hi"]]


# --------------------------------------------------
# 8. REMOVE HEIGHT OUTLIERS
# --------------------------------------------------
height_low = df["height"].quantile(0.025)
height_high = df["height"].quantile(0.975)

df = df[(df["height"] >= height_low) & (df["height"] <= height_high)]


# --------------------------------------------------
# 9. REMOVE WEIGHT OUTLIERS
# --------------------------------------------------
weight_low = df["weight"].quantile(0.025)
weight_high = df["weight"].quantile(0.975)

df = df[(df["weight"] >= weight_low) & (df["weight"] <= weight_high)]


# --------------------------------------------------
# 10. FINAL VALIDATION
# --------------------------------------------------
print("Cleaned shape:", df.shape)
print("Missing values:", df.isnull().sum().sum())
print("Columns:", df.columns.tolist())


# --------------------------------------------------
# 11. SAVE CLEANED DATASET
# --------------------------------------------------
df.to_csv("medical_examination_cleaned.csv", index=False)

print("Cleaned dataset saved as medical_examination_cleaned.csv")