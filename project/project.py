import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import glob

# Load all CSV files dynamically
files = glob.glob("*.csv")  # Load all CSVs in the current directory
dataframes = []

# Read and process each CSV file
for file in files:
    df = pd.read_csv(file)
    df["Date"] = pd.to_datetime(df["Date"], format="%d.%m.%Y")
    df["Year"] = df["Date"].dt.year
    dataframes.append(df)

# Combine all datasets
df = pd.concat(dataframes)

# Fill missing values with zeros
df.fillna(0, inplace=True)

# Extract Month for monthly trend analysis
df["Month"] = df["Date"].dt.month

# ==============================
# 1. Yearly Production Trend Analysis
# ==============================
yearly_production = df.groupby("Year")["Factory W"].sum()

plt.figure(figsize=(10, 5))
plt.plot(yearly_production.index, yearly_production.values, marker="o", linestyle="-")
plt.title("Total Yearly Factory Production (2019-2025)")
plt.xlabel("Year")
plt.ylabel("Total Factory Weight (kg)")
plt.grid()
plt.show()

# ==============================
# 2. Monthly Production Comparison Across Years
# ==============================
monthly_production = df.groupby(["Year", "Month"])["Factory W"].sum().unstack()

plt.figure(figsize=(12, 6))
monthly_production.T.plot(kind="line", marker="o")
plt.title("Monthly Factory Production (2019-2025)")
plt.xlabel("Month")
plt.ylabel("Factory Weight (kg)")
plt.legend(title="Year")
plt.grid()
plt.show()

# ==============================
# 3. Variance Analysis (Factory W - Field W)
# ==============================
df["Variance"] = df["Factory W"] - df["Field W"]
variance_trend = df.groupby(["Year", "Month"])["Variance"].mean().unstack()

plt.figure(figsize=(12, 6))
variance_trend.T.plot(kind="bar", alpha=0.7)
plt.title("Average Monthly Variance (Factory W - Field W) [2019-2025]")
plt.xlabel("Month")
plt.ylabel("Variance (kg)")
plt.legend(title="Year")
plt.grid()
plt.show()

# ==============================
# 4. Moving Average (7-day rolling)
# ==============================
df["Factory_W_MA7"] = df.groupby("Year")["Factory W"].transform(lambda x: x.rolling(7, min_periods=1).mean())

plt.figure(figsize=(14, 6))
sns.lineplot(data=df, x="Date", y="Factory_W_MA7", hue="Year")
plt.title("7-Day Moving Average of Factory Production (2019-2025)")
plt.xlabel("Date")
plt.ylabel("Factory Weight (kg)")
plt.legend(title="Year")
plt.xticks(rotation=45)
plt.grid()
plt.show()

# ==============================
# 5. Correlation Between Rainfall & Production
# ==============================
correlation_matrix = df[["Factory W", "Rainfall"]].corr()
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Between Rainfall and Production")
plt.show()

# ==============================
# 6. Percentage Change in Production Per Year
# ==============================
percentage_change = yearly_production.pct_change() * 100

print("\nYearly Production Data (Factory Weight):")
print(yearly_production)

print("\nPercentage Change in Production Per Year:")
print(percentage_change)

