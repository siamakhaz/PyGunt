# README.md for PyGuntt 

## Overview
This README provides information about a Python script designed to create a Gantt chart for a project titled "Automated Documentation Website Development." The script uses `matplotlib` for plotting and `pandas` for data handling.

## Requirements
To run this script, you need the following libraries:
- matplotlib
- pandas

Ensure these are installed in your Python environment. You can install them using pip:
```
pip install matplotlib pandas
```

## Description
The script performs the following key steps:
1. **Define Project Phases:** It starts by defining the different phases of the project along with their timelines.
2. **Data Preparation:** Converts the phases into a pandas DataFrame and processes the dates for plotting.
3. **Gantt Chart Creation:** Utilizes `matplotlib` to create a Gantt chart visualizing the timeline of each project phase.

## How to Run
1. Ensure that you have Python installed on your system.
2. Install the required libraries (matplotlib, pandas).
3. Run the script in your Python environment.

## Script Breakdown
- **Import Statements:** Imports required modules (`matplotlib`, `matplotlib.dates`, and `pandas`).
- **Project Phases Definition:** A dictionary `phases` holds the phases and their dates.
- **DataFrame Creation:** Converts the `phases` dictionary into a pandas DataFrame.
- **Date Processing:** The start and finish dates are converted from strings to datetime objects.
- **Gantt Chart Plotting:** The script plots a Gantt chart using `matplotlib`, showing the duration of each phase.

## Output
Upon execution, the script displays a Gantt chart with the following features:
- Horizontal bars representing each phase's duration.
- Custom labels and title.
- Date formatting for clear understanding of the timeline.

## Customization
You can customize the script by modifying the `phases` dictionary to reflect your project's timeline.

## Disclaimer
This script is provided as-is for educational purposes. Users are encouraged to modify and adapt it as per their project needs.