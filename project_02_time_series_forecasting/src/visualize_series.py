import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("data/airline-passengers.csv")

data["Month"]=pd.to_datetime(data["Month"])
data=data.sort_values("Month")

plt.figure(figsize=(10,6))
data.plot(kind="line",x="Month",y="Passengers")
plt.title("Airline Passengers Over Time")
plt.xlabel("Year")
plt.ylabel("Number of Passengers")
plt.tight_layout()
plt.savefig("output/line_chart.png")
plt.close()
# plt.show()

data["Year"]=data["Month"].dt.year
data["Month"]=data["Month"].dt.month

monthly_avg=data.groupby("Month")["Passengers"].mean()
plt.figure(figsize=(10,6))
monthly_avg.plot(kind="bar")
plt.title("Monthly Average Airline Passengers")
plt.xlabel("Month")
plt.ylabel("Average Number of Passengers")
plt.tight_layout()
plt.savefig("output/monthly_avg_bar_chart.png")
plt.close()
# plt.show()

yearly_avg=data.groupby("Year")["Passengers"].mean()
plt.figure(figsize=(10,6))
yearly_avg.plot(kind="line")
plt.title("Yearly Average Airline Passengers")
plt.xlabel("Year")
plt.ylabel("Average Number of Passengers")
plt.tight_layout()
plt.savefig("output/yearly_avg_line_chart.png")
plt.close()
# plt.show()