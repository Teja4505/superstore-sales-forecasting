## 🚀 Live Demo

👉 [Click here to view the live dashboard](https://superstore-sales-forecasting-czcbkhhl43wuhisl8qt3vs.streamlit.app/)

---
# Superstore Sales Forecasting & Demand Intelligence System

## Project Overview

This project is an end-to-end data science solution developed to analyze historical Superstore sales data, identify business patterns, forecast future demand, detect unusual sales behavior, and segment products based on demand.

The project combines Exploratory Data Analysis, Time Series Analysis, Machine Learning, Anomaly Detection, Clustering, and an interactive Streamlit dashboard to support data-driven business decisions.

## Project Objectives

- Analyze historical sales performance
- Identify category-wise and region-wise sales trends
- Study monthly and seasonal sales patterns
- Forecast future sales using multiple forecasting models
- Compare forecasting models using MAE, RMSE, and MAPE
- Detect unusual sales spikes and drops
- Segment products into demand groups
- Build a business dashboard for visual insights

## Dataset

The Superstore dataset contains:

- 9,800 sales records
- 18 original features
- Order and shipping information
- Customer segments
- Product categories and sub-categories
- Geographic regions
- Sales values

## Project Workflow

### 1. Data Cleaning and Exploration

- Loaded and inspected the dataset
- Checked missing values and duplicate records
- Handled missing Postal Code values
- Converted Order Date and Ship Date into datetime format
- Analyzed category, region, segment, product, and state-level sales
- Calculated shipping duration and regional shipping patterns

### 2. Time Series Analysis

- Aggregated sales into daily, weekly, and monthly time series
- Created Year, Month, Week Number, Day of Week, Quarter, and Season features
- Analyzed monthly and yearly sales trends
- Applied seasonal decomposition to separate trend, seasonality, and residual components
- Performed the Augmented Dickey-Fuller (ADF) stationarity test

### 3. Sales Forecasting

Three forecasting approaches were developed and compared:

- SARIMA
- Prophet
- XGBoost

The models were evaluated using:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- Mean Absolute Percentage Error (MAPE)

The best-performing model was selected based on forecasting performance.

### 4. Category and Region Forecasting

- Analyzed category-wise monthly sales
- Forecasted future category demand
- Analyzed region-wise monthly sales
- Forecasted future regional sales
- Identified the highest forecasted category and region

### 5. Anomaly Detection

Two anomaly detection methods were applied:

- Isolation Forest
- Rolling Z-Score

The methods were compared to identify unusual weekly sales spikes and drops that may be associated with seasonal demand, promotions, bulk orders, or unexpected demand changes.

### 6. Product Demand Segmentation

K-Means clustering was used to segment products using:

- Total Sales
- Order Frequency
- Average Order Value

Products were classified into:

- High Demand
- Medium Demand
- Low Demand

These segments can support inventory planning, promotion strategies, and stock management.

### 7. Streamlit Dashboard

A Streamlit dashboard was developed to display:

- Total Sales
- Total Orders
- Average Sales
- Maximum Sale
- Monthly Sales Trend
- Category-wise Sales
- Region-wise Sales
- Top 10 Products
- Segment-wise Sales
- Key Business Insights

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Statsmodels
- Prophet
- XGBoost
- Streamlit
- Google Colab

## Project Files

- `Teja_Asapu_Superstore_Sales_Forecasting.ipynb` — Complete data analysis and machine learning workflow
- `app.py` — Streamlit dashboard application
- `train.csv` — Dataset
- `README.md` — Project documentation

## Key Business Value

This project demonstrates how historical sales data can be transformed into useful business intelligence. The solution can help businesses:

- Improve demand planning
- Reduce stock-outs and excess inventory
- Identify high-value products and markets
- Detect unusual sales behavior
- Support forecasting and strategic decision-making

## Author

**Teja Asapu**

B.Tech — Artificial Intelligence and Data Science
