import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import zscore

# Load dataset (change filename if needed)
file_path = "production_2025.csv"
data_2025 = pd.read_csv(file_path)

# ✅ Fix date parsing
data_2025["Date"] = pd.to_datetime(data_2025["Date"], errors="coerce", dayfirst=True)

# ✅ Ensure numerical columns are correctly formatted
numeric_cols = ["Field Wght", "Factory W", "Variance", "Average", "Rainfall", "Running totals"]
for col in numeric_cols:
    data_2025[col] = pd.to_numeric(data_2025[col], errors="coerce")

# ✅ Fill missing values (0 for numeric columns)
data_2025.fillna(0, inplace=True)

# ✅ Sort data by date
data_2025 = data_2025.sort_values(by="Date")

# ✅ Calculate 7-day moving average for Factory W
data_2025["Factory W MA7"] = data_2025["Factory W"].rolling(window=7, min_periods=1).mean()

# ✅ Calculate daily change percentage for Factory W
data_2025["Daily Change %"] = data_2025["Factory W"].pct_change() * 100

# ✅ Identify significant drops (>10% decrease)
significant_drops = data_2025[data_2025["Daily Change %"] < -10]

# ✅ Identify significant spikes (>10% increase)
significant_spikes = data_2025[data_2025["Daily Change %"] > 10]

# ✅ Detect anomalies using Z-score method
data_2025["Z-Score"] = zscore(data_2025["Factory W"])
anomalies = data_2025[np.abs(data_2025["Z-Score"]) > 2.5]  # Anomalies with Z-score > 2.5

# ✅ Calculate cumulative sum for running totals
data_2025["Cumulative Production"] = data_2025["Factory W"].cumsum()

# ✅ Plot Factory Weight Trends
plt.figure(figsize=(14, 6))
sns.lineplot(data=data_2025, x="Date", y="Factory W", label="Factory W", marker="o")
sns.lineplot(data=data_2025, x="Date", y="Factory W MA7", label="7-day Moving Avg", linestyle="--")
plt.xlabel("Date")
plt.ylabel("Factory Weight")
plt.title("📈 Factory Weight Trend in 2025")
plt.xticks(rotation=45)
plt.legend()
plt.grid()
plt.show()

# ✅ Plot Variance Over Time
plt.figure(figsize=(12, 5))
sns.barplot(data=data_2025, x="Date", y="Variance", color="red")
plt.xlabel("Date")
plt.ylabel("Variance")
plt.title("⚠️ Variance in Production Over Time")
plt.xticks(rotation=45)
plt.grid()
plt.show()

# ✅ Plot Running Totals Over Time
plt.figure(figsize=(12, 5))
sns.lineplot(data=data_2025, x="Date", y="Cumulative Production", color="green", marker="o")
plt.xlabel("Date")
plt.ylabel("Cumulative Production")
plt.title("📊 Cumulative Factory Production in 2025")
plt.xticks(rotation=45)
plt.grid()
plt.show()

# ✅ Rainfall vs Factory Weight (Correlation Analysis)
plt.figure(figsize=(12, 6))
sns.scatterplot(data=data_2025, x="Rainfall", y="Factory W", hue="Date", palette="coolwarm", size=2)
plt.xlabel("Rainfall")
plt.ylabel("Factory Weight")
plt.title("☔ Rainfall Impact on Production")
plt.grid()
plt.show()

# ✅ Highlight Significant Production Drops
if not significant_drops.empty:
    print("\n🚨 Significant production drops (>10%) detected:")
    print(significant_drops[["Date", "Factory W", "Daily Change %"]])
else:
    print("\n✅ No major production drops detected.")

# ✅ Highlight Significant Production Spikes
if not significant_spikes.empty:
    print("\n🚀 Significant production spikes (>10%) detected:")
    print(significant_spikes[["Date", "Factory W", "Daily Change %"]])
else:
    print("\n✅ No major production spikes detected.")

# ✅ Highlight Anomalies
if not anomalies.empty:
    print("\n⚠️ Detected Anomalies in Production Data:")
    print(anomalies[["Date", "Factory W", "Z-Score"]])
else:
    print("\n✅ No major anomalies detected.")

# ✅ Save cleaned data for further analysis
data_2025.to_csv("cleaned_production_2025.csv", index=False)
print("\n✅ Cleaned data saved as 'cleaned_production_2025.csv' for further analysis.")
