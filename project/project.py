import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import glob

# Load all CSV files
file_paths = glob.glob("C:/Users/user/Documents/data--science/project/*.csv")

df_list = []
for file in file_paths:
    df = pd.read_csv(file)
    print(f"📂 Processing: {file} - Columns Found: {df.columns.tolist()}")  # Debugging
    
    df.columns = [col.strip().lower() for col in df.columns]  # Normalize column names

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

# ✅ Remove Duplicate Dates
df_all.set_index("date", inplace=True)
df_all = df_all[~df_all.index.duplicated(keep="first")]

# Filter data for 2024
df_2024 = df_all[df_all.index.year == 2024]

# Compute Monthly Averages
df_2024["month"] = df_2024.index.to_period("M")
monthly_avg = df_2024.groupby("month")["factory w"].mean()

# Compute Rolling Mean
df_all["rolling_avg"] = df_all["factory w"].rolling(window=30, min_periods=1).mean()

# Year-over-Year Comparison
df_all["year"] = df_all.index.year
yearly_avg = df_all.groupby("year")["factory w"].mean()

# 📊 Plot Results
fig, ax = plt.subplots(2, 2, figsize=(15, 10))

# 1️⃣ Monthly Production Trend - 2024
sns.lineplot(x=monthly_avg.index.astype(str), y=monthly_avg, marker="o", ax=ax[0, 0], color="blue")
ax[0, 0].set_title("Monthly Production Trend - 2024")
ax[0, 0].set_xticklabels(monthly_avg.index.astype(str), rotation=45)

# 2️⃣ Yearly Comparison
sns.barplot(x=yearly_avg.index.astype(str), y=yearly_avg, hue=yearly_avg.index.astype(str), ax=ax[0, 1], palette="coolwarm", legend=False)
ax[0, 1].set_title("Yearly Average Production Comparison")

# 3️⃣ Rolling Average
sns.lineplot(x=df_all.index, y=df_all["rolling_avg"], ax=ax[1, 0], color="green")
ax[1, 0].set_title("Smoothed Production Trend (Rolling Average)")

# 4️⃣ Anomaly Detection
threshold = df_all["factory w"].mean() - 2 * df_all["factory w"].std()
df_all["anomaly"] = df_all["factory w"] < threshold
sns.scatterplot(x=df_all.index, y=df_all["factory w"], hue=df_all["anomaly"], palette={True: "red", False: "gray"}, ax=ax[1, 1])
ax[1, 1].set_title("Anomaly Detection in Production")

plt.tight_layout()
plt.show()
