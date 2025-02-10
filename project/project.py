import pandas as pd
import matplotlib.pyplot as plt
import glob

# Load all CSV files from the folder
file_paths = glob.glob("C:/Users/user/Documents/data--science/project/*.csv")  # Update path if needed

# Read and merge data
df_list = []
for file in file_paths:
    df = pd.read_csv(file)
    
    # Fix Date column (handles different formats)
    df["Date"] = df["Date"].astype(str).str.split(" ").str[0]  # Remove time if present
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")  # Convert to datetime
    
    df_list.append(df)

# Combine all years into one DataFrame
df_all = pd.concat(df_list, ignore_index=True)

# Sort by Date
df_all = df_all.sort_values(by="Date")

# Check for missing or incorrect data
print(df_all.isnull().sum())  # Shows missing values
print(df_all.head())  # Preview first rows

# Plot production trends (Factory Weight over time)
plt.figure(figsize=(12, 6))
plt.plot(df_all["Date"], df_all["Factory W"], marker='o', linestyle='-', label="Factory Weight")
plt.xlabel("Date")
plt.ylabel("Factory Weight (kg)")
plt.title("Production Trend Over Time")
plt.legend()
plt.grid(True)
plt.show()
