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
# df['Cabin'].fillna(df['Cabin'].mode()[0], inplace=True)


# - forward fill(use previous values)
# df['Age'].fillna(method='ffill', inplace=True) # forward fill
# # - backward fill(use next values)
# df['Age'].fillna(method='bfill', inplace=True) # backward fill




# mode
# data = {'Name': ['Tom', 'nick', 'krish', 'jack', None, 'Nick', None]}

# df = pd.DataFrame(data)

# print("before filling missing values",)
# print(df)
# #  filling the missing

# df['Name'].fillna(df['Name'].mode()[0], inplace=True)

# print("\n After filling missing values",)
# print(df)

# sometimes mode fails due to:
# incorrect data types
# empty mode result
# multiple modes
# missing values

#  2 Handling duplicates

# duplicate data can distort insights and leads to biased results

# # identify the duplicates
# print(df.duplicated().sum()) # -- count the duplicate rows
# print(df[df.duplicated()]) # -- display duplicate rows


# removing the duplicates
# 1 drop the duplicate rows

# example

# df.drop_duplicates(inplace=True)

# example 2
data = {'ID': [1,2,2,3,4,4,5,]}

df = pd.DataFrame(data)

duplicates = df[df.duplicated()]
print("Duplicate Rows:\n", duplicates)

removed_duplicates = df[df.duplicated(keep=False)]
print("All Duplicates:\n ", duplicates)
df_cleaned = df.drop_duplicates()

print("\n Data after removing duplicates:\n", df_cleaned)

