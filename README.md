# Water Quality Dashboard

## Overview
This **Dashboard** is a Streamlit web application provides descriptive statistics, interactive 2D and 3D visualizations, and integrates NASA’s Astronomy Picture of the Day API for an additional data-driven feature.

This project demonstrates data analysis, visualization, and API integration using Python and Streamlit.

## Dataset
The application uses a CSV dataset named:

**`biscayneBay_waterquality`**

The dataset includes water quality and geospatial measurements such as:
- Time
- Temperature (°C)
- pH
- Dissolved Oxygen (ODO mg/L)
- Latitude and Longitude
- Total Water Column (m)

The dataset is loaded using **pandas** and is displayed along with its descriptive statistics inside the app.

## Features
- **Descriptive Statistics Tab**
  - Displays the raw dataset
  - Shows summary statistics using `df.describe()`

- **2D Plots**
  - Line plot of Temperature over Time
  - Scatter plot of Temperature vs. Dissolved Oxygen, colored by pH

- **3D Plots**
  - 3D scatter plot using geographic coordinates and water depth
  - Depth axis is reversed to reflect realistic water column behavior

- **NASA APOD**
  - Retrieves NASA’s Astronomy Picture of the Day using the APOD API
  - Uses an API key stored in environment variables

