import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Load data
df = pd.read_csv("data/airline-passengers.csv")
df["Month"] = pd.to_datetime(df["Month"])
df = df.sort_values("Month")
df.set_index("Month", inplace=True)

# Time features
df["month"] = df.index.month
df["year"] = df.index.year

# Lag features
df["lag_1"] = df["Passengers"].shift(1)
df["lag_12"] = df["Passengers"].shift(12)

df = df.dropna()

# Train / test split
train = df.iloc[:-12]
test = df.iloc[-12:]

X_train = train[["month", "year", "lag_1", "lag_12"]]
y_train = train["Passengers"]

X_test = test[["month", "year", "lag_1", "lag_12"]]
y_test = test["Passengers"]

# Model
model = RandomForestRegressor(
    n_estimators=300,
    random_state=42
)

model.fit(X_train, y_train)
preds = model.predict(X_test)

# Evaluation
mae = mean_absolute_error(y_test, preds)
rmse = np.sqrt(mean_squared_error(y_test, preds))

print("ML MAE:", mae)
print("ML RMSE:", rmse)
