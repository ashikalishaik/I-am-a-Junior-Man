# I-am-a-Junior-Man
I am regaining my confidence that I am equal to a Senior IT Manager

## Day 1
- Installed: Python, Git, VS Code
- Created a GitHub repository
- Created a folder using `mkdir`
- Created a Python file (`echo "" > hello.py`)
- Edited the file using VS Code (`code hello.py`)
- Ran the script using Python
- Git workflow: `git status` → `git add .` → `git commit` → `git push`

## Day 2
- Built and ran a mini calculator script (supports + - * /, handles division by zero)
- Practiced terminal workflow: run → status → commit → push
- Built Project 01 using pandas without AI-generated code
- Loaded CSV, inspected schema, checked missing values, generated summary report
- Saved output to output/summary.txt


- ### Project 01 – Pandas Basics

- #### Goal
- Build confidence using pandas by analyzing a real CSV dataset from scratch.

- #### What this project demonstrates
- Loading and inspecting data with pandas
- Understanding dataset structure
- Computing basic statistics
- Writing results to an output file

- #### Why this matters
- This project is focused on hands-on confidence and ownership, not advanced ML.

## Day 3
- Loaded CSV, inspected schema, checked missing values, generated summary report
- Saved output to output/insights_v2.txt
- DATA.GROUPBY("","")[""].APPLY().SORT()
- DATA[""]=DATA[""]/DATA[""]*100

## Day 4
- I build a complete exploratory analysis pipeline: data loading, feature engineering, groupby insights, saved visualizations, and business interprettations.


## Day 5

### Project 02 – Time Series Forecasting

#### Problem
Forecast future airline passenger demand based on historical monthly data.

#### Why this matters
Accurate demand forecasting supports capacity planning, pricing, and operational decisions.

#### Approach
- Explore trend and seasonality
- Establish a baseline forecast
- Evaluate before improving

#### Time Series Visualization Insights

##### Overall Trend
The number of airline passengers increases steadily over time, indicating a strong upward trend.
This suggests that simple stationary models may not perform well without transformation.

##### Seasonality
Passenger counts show clear seasonal patterns, with certain months consistently having higher demand.
This indicates the presence of yearly seasonality that must be modeled explicitly.

##### Variability
The amplitude of fluctuations increases over time, suggesting multiplicative seasonality rather than additive.
This has implications for model selection and data transformation.

#### “Before forecasting, I analyzed trend, seasonality, and variance to understand whether the series is stationary and what modeling assumptions are valid.”

#### Time Series Data Decomposition

The decomposition is done by setting the index and then using the `statsmodels.tsa.seasonal seasonal_decompose where seasonal_decompose(data["Passengers"], model="multiplicative", period=12)`

#### “Before forecasting, I decomposed the series to understand trend, seasonality, and noise, and selected a multiplicative model based on increasing variance.”

#### Forecasting Results

Baseline and SARIMA models were evaluated using MAE and RMSE.

- Naive forecast performed poorly due to lack of seasonality modeling.
- Seasonal naive captured yearly patterns but remained limited.
- SARIMA significantly reduced error (MAE ≈ 16, RMSE ≈ 21), demonstrating improved modeling of trend and seasonal structure.

Warnings related to frequency inference and convergence were addressed by explicitly setting time frequency and noting that further parameter tuning could improve optimization stability.
