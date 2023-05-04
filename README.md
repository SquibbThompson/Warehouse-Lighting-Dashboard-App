Smart Lights Optimal Time Dashboard

This project provides a dashboard and a pie chart display for measuring the optimal time for auto-updating smart lights in a warehouse setting. It is based on ergonomic design theory and aims to visualize the best timeframes for different light colors to ensure a comfortable and efficient working environment.
Overview

The project consists of two main parts:

    Dashboard: A Python-based interactive dashboard created using Panel, Pandas, and Seaborn for visualizing the optimal time ranges for different colors of smart lights. It includes three tabs: Dataframe, Metadata, and Visualization. The Dataframe tab shows the raw data used in the project, the Metadata tab displays detailed information about each color, and the Visualization tab presents a bar chart to display the optimal time ranges for each color. The dashboard also includes interactive sliders for adjusting the start and end times of each color.

    Pie Chart Display: A Python-based pie chart display created using Matplotlib to visualize the ratio of each color's timeframe with respect to the total duration. The output colors in the pie chart match their corresponding labels.

Usage
Dashboard

To run the dashboard, simply execute the dashboard.py file in a Python environment with the required libraries installed. The dashboard will open in your default web browser, and you can interact with the sliders to adjust the optimal time range for each color.
Pie Chart Display

To display the pie chart, execute the pie_chart_display.py file in a Python environment with the required libraries installed. The pie chart will be displayed in a separate window, showing the ratio of each color's timeframe with respect to the total duration.
Requirements

The following libraries are required to run the dashboard and pie chart display:

    Pandas
    Panel
    Seaborn
    Matplotlib

You can install these libraries using pip or conda.
