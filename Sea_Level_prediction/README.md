# Sea Level Predictor

This project analyzes historical sea level data and predicts future sea level rise using **linear regression**.

## Project Objective

The goal is to visualize sea level changes over time and estimate the sea level rise by the year **2050**.

## Dataset

The dataset `epa-sea-level.csv` contains historical sea level measurements with the following fields:

* **Year** – Year of measurement
* **CSIRO Adjusted Sea Level** – Sea level in inches

## What the Program Does

The script:

* Loads sea level data using **Pandas**
* Creates a **scatter plot** of historical sea level measurements
* Calculates a **line of best fit using linear regression** for:

  * The full dataset (1880–present)
  * Data from **2000 onwards**
* Extends both prediction lines to the year **2050**
* Highlights the **predicted sea level values for 2050**
* Saves the final visualization as `sea_level_plot.png`

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* SciPy

## How to Run

Install required libraries:

```bash id="a91f2g"
pip install pandas matplotlib numpy scipy
```

Run the script:

```bash id="p8x4d2"
python sea_level_predictor.py
```

The program will generate the output file:

```
sea_level_plot.png
```
