# Page View Time Series Visualizer

This project analyzes **freeCodeCamp forum page view data** and visualizes trends using Python.

## What This Project Does

* Loads page view data from `fcc-forum-pageviews.csv`
* Removes extreme outliers (top and bottom 2.5%)
* Creates three visualizations to analyze traffic trends

## Visualizations

**1. Line Plot**
Shows daily freeCodeCamp forum page views from **2016 to 2019**.

**2. Bar Plot**
Displays **average monthly page views grouped by year**.

**3. Box Plots**

* Year-wise box plot → shows long-term trends
* Month-wise box plot → shows seasonal patterns

## Technologies Used

Python, Pandas, Matplotlib, Seaborn

## Run the Project

```bash
python time_series_visualizer.py
```

This will generate:

* `line_plot.png`
* `bar_plot.png`
* `box_plot.png`

