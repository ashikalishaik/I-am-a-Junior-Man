import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("data/sales.csv")

data["tip_pct"]=data["tip"]/data["total_bill"] * 100
avg_tip_by_day=data.groupby("day")["tip_pct"].mean()
avg_tip_by_day.plot(kind="bar")
plt.title("Average Tip Percentage by Day")
plt.xlabel("Day of the Week")
plt.ylabel("Average Tip Percentage (%)")
plt.tight_layout()
plt.savefig("output/avg_tip_by_day_bar.png")
plt.close()
# plt.show()

plt.figure()
data.boxplot(column="tip_pct", by="day")
plt.title("Box Plot of Tip Percentage by Day")
plt.xlabel("Day of the Week")
plt.ylabel("Tip Percentage (%)")
plt.suptitle("")  # Remove the default title
plt.tight_layout()
plt.savefig("output/avg_tip_by_day_box.png")
plt.close()
# plt.show()


