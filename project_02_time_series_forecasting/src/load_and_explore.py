import pandas as pd

data=pd.read_csv("data/airline-passengers.csv")


data["Month"]=pd.to_datetime(data["Month"])
data=data.sort_values("Month")
print(data.head())
print(data.columns)
print(data.shape)
summary=data.describe()
with open("output/summary.txt","w") as f:
    f.write(str(summary))

print(data.info())
print(data.isna().sum())

print("\nDate range:")
print(data["Month"].min(), "to", data["Month"].max())