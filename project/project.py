import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.seasonal import seasonal_decompose
import glob

# Load all CSV files
file_paths = glob.glob("C:/Users/user/Documents/data--science/project/*.csv")

df_list = []
for file in file_paths:
    df = pd.read_csv(file)

    # Standardize column names
    df.columns = [col.strip().lower() for col in df.columns]

    if 'date' not in df.columns:
        print(f"⚠️ Skipping {file}: No 'Date' column found!")
        continue

    df["date"] = pd.to_datetime(df["date"], errors="coerce", dayfirst=True)
    df.replace("-", np.nan, inplace=True)

    if "factory w" in df.columns:
        df["factory w"] = pd.to_numeric(df["factory w"], errors="coerce")

    df_list.append(df)

if not df_list:
    print("❌ No valid CSV files found with a 'Date' column. Check your data.")
    exit()

df_all = pd.concat(df_list, ignore_index=True)
df_all.dropna(subset=["date"], inplace=True)
df_all.sort_values(by="date", inplace=True)

# Filter data for 2024
df_2024 = df_all[df_all["date"].dt.year == 2024]

# Compute Monthly Averages
df_2024["month"] = df_2024["date"].dt.to_period("M")
monthly_avg = df_2024.groupby("month")["factory w"].mean()

# Compute Rolling Mean (Smoothing)
df_all["rolling_avg"] = df_all["factory w"].rolling(window=30, min_periods=1).mean()

# YoY Comparison (Compare 2024 vs Previous Years)
df_all["year"] = df_all["date"].dt.year
yearly_avg = df_all.groupby("year")["factory w"].mean()

# Seasonal Decomposition (Trend & Seasonality Detection)
df_all.set_index("date", inplace=True)
result = seasonal_decompose(df_all["factory w"].dropna(), model="additive", period=30)

# Anomaly Detection (Detect Sudden Drops)
threshold = df_all["factory w"].mean() - 2 * df_all["factory w"].std()
df_all["anomaly"] = df_all["factory w"] < threshold

# 📊 Plot Results
fig, ax = plt.subplots(2, 2, figsize=(15, 10))

# 1️⃣ Plot Monthly Trend for 2024
sns.lineplot(x=monthly_avg.index.astype(str), y=monthly_avg, marker="o", ax=ax[0, 0], color="blue")
ax[0, 0].set_title("Monthly Production Trend - 2024")
ax[0, 0].set_xticklabels(monthly_avg.index.astype(str), rotation=45)

# 2️⃣ Compare 2024 vs Previous Years
sns.barplot(x=yearly_avg.index.astype(str), y=yearly_avg, ax=ax[0, 1], palette="coolwarm")
ax[0, 1].set_title("Yearly Average Production Comparison")
ax[0, 1].set_xticklabels(yearly_avg.index.astype(str), rotation=45)

# 3️⃣ Show Rolling Average (Smoothed Trend)
sns.lineplot(x=df_all.index, y=df_all["rolling_avg"], ax=ax[1, 0], color="green")
ax[1, 0].set_title("Smoothed Production Trend (Rolling Average)")

# 4️⃣ Mark Anomalies
sns.scatterplot(x=df_all.index, y=df_all["factory w"], hue=df_all["anomaly"], palette={True: "red", False: "gray"}, ax=ax[1, 1])
ax[1, 1].set_title("Anomaly Detection in Production")

plt.tight_layout()
plt.show()
