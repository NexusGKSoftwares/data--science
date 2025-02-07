import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = "data_2025.csv"  # Update this to your actual file path
data_2025 = pd.read_csv(file_path)

# Fix Date column parsing
data_2025["Date"] = pd.to_datetime(data_2025["Date"], errors="coerce", dayfirst=True)

# Handle missing Date values (replace with default or drop)
data_2025["Date"].fillna(pd.Timestamp("2025-01-01"), inplace=True)  # Replace NaN dates with Jan 1, 2025

# Ensure numerical columns are correctly formatted
numeric_cols = ["Field Wght", "Factory W", "Variance", "Average", "Rainfall", "Running totals"]
for col in numeric_cols:
    data_2025[col] = pd.to_numeric(data_2025[col], errors="coerce")

# Fill missing numeric values with 0
data_2025.fillna(0, inplace=True)

# Sort by Date
data_2025 = data_2025.sort_values(by="Date")

# ---- Data Analysis ----

# Check for production trends
plt.figure(figsize=(12, 6))
sns.lineplot(x="Date", y="Factory W", data=data_2025, marker="o", label="Factory Weight")
sns.lineplot(x="Date", y="Field Wght", data=data_2025, marker="s", label="Field Weight")
plt.xlabel("Date")
plt.ylabel("Weight (kg)")
plt.title("Production Trends (Factory vs. Field Weight) - 2025")
plt.legend()
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Variance trend
plt.figure(figsize=(12, 6))
sns.lineplot(x="Date", y="Variance", data=data_2025, marker="o", color="red")
plt.xlabel("Date")
plt.ylabel("Variance")
plt.title("Variance Over Time - 2025")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Average weight vs. Rainfall
plt.figure(figsize=(10, 5))
sns.scatterplot(x="Rainfall", y="Average", data=data_2025, color="green")
plt.xlabel("Rainfall (mm)")
plt.ylabel("Average Weight")
plt.title("Impact of Rainfall on Average Weight - 2025")
plt.grid(True)
plt.show()

# Detecting drops in production
data_2025["Factory_W_Change"] = data_2025["Factory W"].diff()
data_2025["Field_W_Change"] = data_2025["Field Wght"].diff()

plt.figure(figsize=(12, 6))
sns.lineplot(x="Date", y="Factory_W_Change", data=data_2025, marker="o", label="Factory Weight Change")
sns.lineplot(x="Date", y="Field_W_Change", data=data_2025, marker="s", label="Field Weight Change")
plt.xlabel("Date")
plt.ylabel("Change in Weight")
plt.title("Daily Changes in Production Weight - 2025")
plt.legend()
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Display processed data
print(data_2025.head())

# Save cleaned data
data_2025.to_csv("cleaned_data_2025.csv", index=False)
