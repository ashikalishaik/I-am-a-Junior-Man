import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("data/airline-passengers.csv")
data["Month"]=pd.to_datetime(data["Month"])
data=data.sort_values("Month")
data.set_index("Month",inplace=True)

train=data.iloc[:-12]
test=data.iloc[-12:]

naive_forecast =[train["Passengers"].iloc[-1]]*len(test)

seasonal_naive=train["Passengers"].iloc[-12:].values

plt.figure(figsize=(12, 6))
plt.plot(test.index, test["Passengers"], label="Actual")
plt.plot(test.index, naive_forecast, label="Naive Forecast")
plt.plot(test.index, seasonal_naive, label="Seasonal Naive Forecast")
plt.plot(train.index, train["Passengers"], label="Train Data")
plt.legend()
plt.title("Baseline Forecast Comparision")
plt.tight_layout()

plt.savefig("output/baseline_forecast_comparison.png")
plt.close()