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


## Baseline Forecasting

Two baseline approaches were evaluated before applying advanced models.

- The naive forecast assumes future demand equals the most recent observation and fails to capture seasonality.
- The seasonal naive forecast leverages last year’s monthly values and closely follows actual passenger trends.

This confirms strong yearly seasonality and establishes a meaningful benchmark for future models.


## Model Evaluation

Baseline forecasts were evaluated using MAE and RMSE.
Seasonal naive significantly outperformed naive forecasting, confirming strong seasonality.

A SARIMA model further reduced error by explicitly modeling trend and seasonal structure.
This demonstrates that model complexity is justified only after strong baselines are established.

## SARIMA Diagnostics

Residual analysis indicates that the SARIMA model has captured most of the temporal structure.
Residuals show no visible trend or seasonality, and autocorrelation is minimal.
This suggests the model assumptions are reasonable and forecasts are reliable.

## ML vs Statistical Models

A feature-based ML model (Random Forest) was evaluated using lag and calendar features.
While ML can model nonlinear relationships, SARIMA achieved comparable or better performance due to the strong and well-structured seasonality in the data.

This highlights that model selection should be driven by data characteristics rather than model complexity.

I evaluated both statistical and ML-based forecasting approaches and selected models based on residual diagnostics and error metrics rather than complexity

## Final Model Selection and Conclusion

Multiple forecasting approaches were evaluated, including naive baselines, seasonal baselines, classical time-series models, and feature-based machine learning models.

The SARIMA model achieved the lowest MAE and RMSE and produced residuals that appeared random, indicating that the model successfully captured the underlying trend and seasonal structure of the data.

While the machine learning model demonstrated competitive performance, it did not outperform SARIMA, likely due to limited data size and strong seasonal patterns. Based on quantitative evaluation and residual analysis, SARIMA was selected as the most appropriate model for this forecasting task.

