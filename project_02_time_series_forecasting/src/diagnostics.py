import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.graphics.tsaplots import plot_acf

df = pd.read_csv("data/airline-passengers.csv")
df["Month"] = pd.to_datetime(df["Month"])
df = df.sort_values("Month")
df.set_index("Month", inplace=True)
df = df.asfreq("MS")

train = df.iloc[:-12]

model = SARIMAX(
    train["Passengers"],
    order=(1,1,1),
    seasonal_order=(1,1,1,12)
)
fit = model.fit(disp=False)

residuals = fit.resid


plt.figure(figsize=(10,4))
plt.plot(residuals)
plt.title("SARIMA Residuals Over Time")
plt.tight_layout()
plt.savefig("output/sarima_residuals_time.png")
plt.close()


plt.figure(figsize=(6,4))
plt.hist(residuals, bins=20)
plt.title("Residual Distribution")
plt.tight_layout()
plt.savefig("output/sarima_residuals_hist.png")
plt.close()


plot_acf(residuals, lags=24)
plt.tight_layout()
plt.savefig("output/sarima_residuals_acf.png")
plt.close()


