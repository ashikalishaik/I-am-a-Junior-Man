import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

# Load data
df = pd.read_csv("data/airline-passengers.csv")
df["Month"] = pd.to_datetime(df["Month"])
df = df.sort_values("Month")

# Set index to time
df.set_index("Month", inplace=True)

# Decompose (multiplicative)
decomposition = seasonal_decompose(
    df["Passengers"],
    model="multiplicative",
    period=12
)

# Plot decomposition
decomposition.plot()
plt.tight_layout()

# Save plot
plt.savefig("output/time_series_decomposition.png")
plt.close()

