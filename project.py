import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = "production_2025.csv"  # Change this to the correct filename if needed
data_2025 = pd.read_csv(file_path)

# Fix date format issues
print("Checking the first few rows of the 'Date' column:")
print(data_2025["Date"].head())  # Print sample dates to debug format issues

# Convert the Date column to datetime format
data_2025["Date"] = pd.to_datetime(data_2025["Date"], errors="coerce", dayfirst=True)

# Check for missing dates
if data_2025["Date"].isna().sum() > 0:
    print("Warning: Some dates could not be converted. Check for inconsistencies.")

# Sort data by date
data_2025 = data_2025.sort_values(by="Date")

# Ensure numerical columns are converted properly
cols_to_convert = ["Field Wght", "Factory W", "Variance", "Average", "Rainfall", "Running totals"]
for col in cols_to_convert:
    data_2025[col] = pd.to_numeric(data_2025[col], errors="coerce")

# Fill missing values with zero (or use another imputation strategy)
data_2025.fillna(0, inplace=True)

# Generate a rolling average (7-day moving average) for Factory Weight
data_2025["Factory W MA7"] = data_2025["Factory W"].rolling(window=7, min_periods=1).mean()

# Plot production trends
plt.figure(figsize=(12, 6))
sns.lineplot(data=data_2025, x="Date", y="Factory W", label="Factory Weight", marker="o")
sns.lineplot(data=data_2025, x="Date", y="Factory W MA7", label="7-day Moving Average", linestyle="--")

plt.xlabel("Date")
plt.ylabel("Factory Weight")
plt.title("Production Trend Analysis - 2025")
plt.xticks(rotation=45)
plt.legend()
plt.grid()
plt.show()

# Identify significant drops in production (>10% drop from previous day)
data_2025["Daily Change %"] = data_2025["Factory W"].pct_change() * 100
significant_drops = data_2025[data_2025["Daily Change %"] < -10]

if not significant_drops.empty:
    print("\nSignificant production drops (>10%) detected on these dates:")
    print(significant_drops[["Date", "Factory W", "Daily Change %"]])
else:
    print("\nNo significant production drops detected.")

# Save cleaned data for further analysis
data_2025.to_csv("cleaned_production_2025.csv", index=False)
print("\nCleaned data saved as 'cleaned_production_2025.csv'.")
