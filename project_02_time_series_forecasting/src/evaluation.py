import pandas as pd
import numpy as np

data= pd.read_csv("data/airline-passengers.csv")
data["Month"] = pd.to_datetime(data["Month"])
data.sort_values("Month")
data.set_index("Month", inplace=True)

train=data.iloc[:-12]
test=data.iloc[-12:]

naive_forecast = np.repeat(train['Passengers'].iloc[-1], len(test))
seasonal_naive = train['Passengers'].iloc[-12:].values

def mae(actual, predicted):
    return np.mean(np.abs(actual - predicted))

def rmse(actual, predicted):
    return np.sqrt(np.mean((actual - predicted) ** 2))

results={
    "Naive MAE": mae(test['Passengers'], naive_forecast),
    "Naive RMSE": rmse(test['Passengers'], naive_forecast),
    "Seasonal Naive MAE": mae(test['Passengers'], seasonal_naive),
    "Seasonal Naive RMSE": rmse(test['Passengers'], seasonal_naive),
    }

for k,v in results.items():
    print(f"{k}: {v:.2f}")
    
from statsmodels.tsa.statespace.sarimax import SARIMAX

model = SARIMAX(
    train["Passengers"],
    order=(1, 1, 1),
    seasonal_order=(1, 1, 1, 12)
)

model_fit = model.fit(disp=False)
sarima_forecast = model_fit.forecast(steps=12)

print("\nSARIMA MAE:", mae(test["Passengers"], sarima_forecast))
print("SARIMA RMSE:", rmse(test["Passengers"], sarima_forecast))
