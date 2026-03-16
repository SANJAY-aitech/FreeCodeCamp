# Medical Data Visualizer

This project analyzes a medical examination dataset and visualizes health-related factors using Python.

## What This Project Does

* Loads medical data from `medical_examination.csv`.
* Calculates **BMI** and creates an `overweight` column.
* Normalizes **cholesterol** and **glucose** values.
* Generates visual insights about patient health conditions.

## Visualizations

### 1. Categorical Plot

Shows the count of health indicators such as:

* Cholesterol
* Glucose
* Smoking
* Alcohol consumption
* Physical activity
* Overweight

The data is separated based on whether the patient has **cardiovascular disease (cardio)**.

Output file:

```
catplot.png
```

### 2. Heatmap

Displays the **correlation between medical variables** after removing incorrect or extreme values.

Output file:

```
heatmap.png
```

## Technologies Used

* Python
* Pandas
* NumPy
* Seaborn
* Matplotlib

## Run the Project

```bash
python medical_data_visualizer.py
```

This will generate:

* `catplot.png`
* `heatmap.png`
