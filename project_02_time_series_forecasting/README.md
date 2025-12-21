# Project 02 – Time Series Forecasting

## Problem
Forecast future airline passenger demand based on historical monthly data.

## Why this matters
Accurate demand forecasting supports capacity planning, pricing, and operational decisions.

## Approach
- Explore trend and seasonality
- Establish a baseline forecast
- Evaluate before improving


## Time Series Visualization Insights

### Overall Trend
The number of airline passengers increases steadily over time, indicating a strong upward trend.
This suggests that simple stationary models may not perform well without transformation.

### Seasonality
Passenger counts show clear seasonal patterns, with certain months consistently having higher demand.
This indicates the presence of yearly seasonality that must be modeled explicitly.

### Variability
The amplitude of fluctuations increases over time, suggesting multiplicative seasonality rather than additive.
This has implications for model selection and data transformation.
