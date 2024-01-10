# Unemployment and Participation Rate Analysis

## Overview
This Python code utilizes the Fred API to fetch and analyze economic data related to unemployment and labor force participation rates in the United States. The analysis is conducted at both the national and state levels. The code includes data retrieval, cleaning, visualization, and comparison of unemployment and participation rates across different states.

## Key Steps

### 1. Data Retrieval
- The code installs the `fredapi` library and imports necessary Python packages.
- It sets up the Fred API key and initializes the Fred object.

### 2. Search for Economic Data
- Conducts a search for economic data related to the S&P index and unemployment rates in states.

### 3. Pull Raw Data & Plot
- Retrieves and plots the S&P 500 index data.

### 4. Pull and Join Multiple Data Series
- Fetches and processes unemployment rate data for states.
- Joins multiple data series for analysis.

### 5. Visualization
- Plots unemployment rates for each state.
- Analyzes and visualizes unemployment rates by state in May 2020.
- Extracts and visualizes labor force participation rates.

### 6. Unemployment versus Participation Rate
- Compares unemployment and participation rates for each state from 2020 to 2024.

## Requirements
- Python
- `fredapi` library
- Pandas, NumPy, Matplotlib, Plotly

## How to Use
1. Install the `fredapi` library using `pip install fredapi`.
2. Run the code cells sequentially in a Jupyter Notebook or another Python environment.

## Results
The code generates visualizations comparing unemployment and participation rates across different states, providing insights into economic trends and variations.

**Note:** Ensure the correct installation of required libraries and proper configuration of the Fred API key for successful execution.
