import pandas as pd
import matplotlib.pyplot as plt
import glob

# Load all CSV files from the folder
file_paths = glob.glob("C:/Users/user/Documents/data--science/project/*.csv")  # Update path if needed

df_list = []
for file in file_paths:
    df = pd.read_csv(file)
    
    # Fix column names (force lowercase for consistency)
    df.columns = [col.strip().lower() for col in df.columns]  

    # Check if 'date' column exists in the CSV
    if 'date' not in df.columns:
        print(f"⚠️ Skipping {file}: No 'Date' column found!")
        continue  # Skip file if no Date column

    # Convert 'date' column to datetime (handles different formats)
    df["date"] = pd.to_datetime(df["date"], errors="coerce", dayfirst=True)  

    df_list.append(df)

# Check if data was loaded
if not df_list:
    print("❌ No valid CSV files found with a 'Date' column. Check your data.")
    exit()

# Combine all years into one DataFrame
df_all = pd.concat(df_list, ignore_index=True)

# Sort by Date
df_all = df_all.sort_values(by="date")

# Check for missing or incorrect data
print(df_all.isnull().sum())  # Shows missing values
print(df_all.head())  # Preview first rows

# Plot production trends (Factory Weight over time)
plt.figure(figsize=(12, 6))
plt.plot(df_all["date"], df_all["factory w"], marker='o', linestyle='-', label="Factory Weight")
plt.xlabel("Date")
plt.ylabel("Factory Weight (kg)")
plt.title("Production Trend Over Time")
plt.legend()
plt.grid(True)
plt.show()
