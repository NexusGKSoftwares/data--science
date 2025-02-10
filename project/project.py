import pandas as pd
import matplotlib.pyplot as plt
import glob
import numpy as np

# Load all CSV files from the folder
file_paths = glob.glob("C:/Users/user/Documents/data--science/project/*.csv")

df_list = []
for file in file_paths:
    df = pd.read_csv(file)
    
    # Fix column names (force lowercase & remove spaces)
    df.columns = [col.strip().lower() for col in df.columns]  

    # Check if 'date' column exists
    if 'date' not in df.columns:
        print(f"⚠️ Skipping {file}: No 'Date' column found!")
        continue  # Skip file if no Date column

    # Convert 'date' column to datetime
    df["date"] = pd.to_datetime(df["date"], errors="coerce", dayfirst=True)  

    # Convert '-' or empty strings to NaN
    df.replace("-", np.nan, inplace=True)

    # Convert factory weight column to numeric (force coercion)
    if "factory w" in df.columns:
        df["factory w"] = pd.to_numeric(df["factory w"], errors="coerce")

    df_list.append(df)

# Check if any valid data exists
if not df_list:
    print("❌ No valid CSV files found with a 'Date' column. Check your data.")
    exit()

# Combine all years into one DataFrame
df_all = pd.concat(df_list, ignore_index=True)

# Drop rows where 'date' is NaT (invalid)
df_all.dropna(subset=["date"], inplace=True)

# Sort by Date
df_all = df_all.sort_values(by="date")

# Check for missing data
print(df_all.isnull().sum())

# Plot production trends (Factory Weight over time)
plt.figure(figsize=(12, 6))
plt.plot(df_all["date"], df_all["factory w"], marker='o', linestyle='-', label="Factory Weight", color="blue")
plt.xlabel("Date")
plt.ylabel("Factory Weight (kg)")
plt.title("Production Trend Over Time")
plt.legend()
plt.grid(True)
plt.show()
