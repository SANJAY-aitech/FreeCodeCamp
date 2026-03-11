import pandas as pd

# ---------------------------
# Load Dataset
# ---------------------------
df = pd.read_csv("adult.data.csv")

# ---------------------------
# 1. Count of each race
# ---------------------------
race_count = df["race"].value_counts()

print("Number of each race:")
print(race_count)
print()


# ---------------------------
# 2. Average age of men
# ---------------------------
average_age_men = df[df["sex"] == "Male"]["age"].mean()

print("Average age of men:", round(average_age_men, 1))
print()


# ---------------------------
# 3. Percentage with Bachelor's degree
# ---------------------------
percentage_bachelors = (df["education"] == "Bachelors").mean() * 100

print("Percentage with Bachelors degrees:", round(percentage_bachelors, 1))
print()


# ---------------------------
# 4. Percentage with advanced education earning >50K
# ---------------------------
advanced_education = df["education"].isin(["Bachelors", "Masters", "Doctorate"])

higher_education_rich = (
    (df[advanced_education]["salary"] == ">50K").mean() * 100
)

print("Percentage with advanced education earning >50K:",
      round(higher_education_rich, 1))
print()


# ---------------------------
# 5. Percentage without advanced education earning >50K
# ---------------------------
lower_education_rich = (
    (df[~advanced_education]["salary"] == ">50K").mean() * 100
)

print("Percentage without advanced education earning >50K:",
      round(lower_education_rich, 1))
print()


# ---------------------------
# 6. Minimum work hours
# ---------------------------
min_work_hours = df["hours-per-week"].min()

print("Minimum work hours per week:", min_work_hours)
print()


# ---------------------------
# 7. Percentage earning >50K among minimum-hour workers
# ---------------------------
min_workers = df[df["hours-per-week"] == min_work_hours]

rich_percentage = (
    (min_workers["salary"] == ">50K").mean() * 100
)

print("Percentage earning >50K among minimum-hour workers:",
      round(rich_percentage, 1))
print()


# ---------------------------
# 8. Country with highest percentage of >50K earners
# ---------------------------
country_salary = (
    df[df["salary"] == ">50K"]["native-country"]
    .value_counts()
    / df["native-country"].value_counts()
) * 100

highest_earning_country = country_salary.idxmax()
highest_earning_country_percentage = country_salary.max()

print("Country with highest percentage of >50K earners:",
      highest_earning_country)

print("Highest percentage of people earning >50K in that country:",
      round(highest_earning_country_percentage, 1))
print()


# ---------------------------
# 9. Most popular occupation for >50K earners in India
# ---------------------------
top_IN_occupation = (
    df[(df["native-country"] == "India") &
       (df["salary"] == ">50K")]["occupation"]
    .value_counts()
    .idxmax()
)

print("Most popular occupation for those earning >50K in India:",
      top_IN_occupation)