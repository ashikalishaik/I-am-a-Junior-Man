import pandas as pd

# Load data
df = pd.read_csv("data/sales.csv")

# Basic averages
avg_total_bill = df["total_bill"].mean()
avg_tip = df["tip"].mean()

# Tip percentage for each row
df["tip_pct"] = (df["tip"] / df["total_bill"]) * 100

avg_tip_pct = df["tip_pct"].mean()

# Grouped insights
tip_pct_by_day = df.groupby("day")["tip_pct"].mean().sort_values(ascending=False)
tip_pct_by_day_time = df.groupby(["day", "time"])["tip_pct"].mean().sort_values(ascending=False)

# Build a clean, readable report
lines = []
lines.append("=== Business Insights (tips.csv) ===\n")
lines.append(f"1) Average total bill: {avg_total_bill:.2f}")
lines.append(f"2) Average tip: {avg_tip:.2f}")
lines.append(f"3) Average tip percentage: {avg_tip_pct:.2f}%\n")

lines.append("4) Average tip percentage by day:")
for day, val in tip_pct_by_day.items():
    lines.append(f"   - {day}: {val:.2f}%")
lines.append("")

lines.append("5) Average tip percentage by day and time:")
for (day, time), val in tip_pct_by_day_time.items():
    lines.append(f"   - {day} / {time}: {val:.2f}%")

report = "\n".join(lines) + "\n"

# Print and save
print(report)

with open("output/insights_v2t", "w", encoding="utf-8") as f:
    f.write(report)