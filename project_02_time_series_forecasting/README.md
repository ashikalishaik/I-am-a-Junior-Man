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

## Time Series Decomposition

The decomposition separates the observed series into trend, seasonal, and residual components.

- The trend component confirms a long-term increase in passenger demand.
- The seasonal component shows a repeating yearly pattern, validating strong seasonality.
- The residual component appears relatively random, suggesting that most structure is captured by trend and seasonality.

The increasing amplitude of seasonal effects supports the use of a multiplicative model.

I decomposed the series to validate trend and seasonality assumptions before selecting a forecasting model.
