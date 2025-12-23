import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX

data=pd.read_csv("data/airline-passengers.csv")
data["Month"]=pd.to_datetime(data["Month"])
data=data.sort_values("Month")
data.set_index("Month",inplace=True)

train=data.iloc[:-12]
test=data.iloc[-12:]

model= SARIMAX(train["Passengers"],order=(1,1,1),seasonal_order=(1,1,1,12))
model_fit=model.fit(disp=False)

forecast = model_fit.forecast(steps=12)

plt.figure(figsize=(10,4))
plt.plot(train.index, train["Passengers"], label="Train")
plt.plot(test.index, test["Passengers"], label="Actual")
plt.plot(test.index, forecast, label="SARIMA Forecast", linestyle="--")
plt.legend()
plt.title("SARIMA Forecast vs Actual")
plt.tight_layout()

plt.savefig("output/SARIMA_Forecast.png")
plt.close()


