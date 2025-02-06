# handling missing values and duplicates
# 1 handling missing values
# - can occur due to human errors, data entry errors, or data loss during transmission- system failures
# - can be handled using imputation techniques, interpolation, or deletion of rows with missing values

# identifying missing values
import pandas as pd
df = pd.read_csv("train.csv") # assuming you have a csv file named "train.csv"
# print(df.isnull().sum()) # this will print the count of missing values in each column
# print(df.info()) #check the data types and missing values

# handling strategies
# 1 remove the missing values(drop rows and columns)


df.dropna(inplace=True) # drop rows with missing values
df.dropna(inplace=True, axis=1) # drop columns with missing values

# 2 impute missing values
# - mean imputation: replace missing values with the mean of the column(numerical values)
# df['Age'].fillna(df['Age'].mean(), inplace=True) #mean
# - median imputation: replace missing values with the median of the column(numerical values)
# df['Age'].fillna(df['Age'].median(), inplace=True)
# - mode imputation: replace missing values with the most frequent value in the column(categorical values)
df['Cabin'].fillna(df['Cabin'].mode()[0], inplace=True)


# - forward fill(use previous values)
# df['Age'].fillna(method='ffill', inplace=True) # forward fill
# # - backward fill(use next values)
# df['Age'].fillna(method='bfill', inplace=True) # backward fill

# handling duplicates


