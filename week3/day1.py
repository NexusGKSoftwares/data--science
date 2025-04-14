# WEEK 3: DATA CLEANING AND PREPROCESSING 

# Lesson 1: handling missing values and duplicates

# detecting missing values 
import pandas as pd

df = pd.read_csv("train.csv")
df.isnull().sum() # returns a series with the number of missing values in each column 
print(df.isnull().sum()) # prints the number of missing values in each column 


# handling missing values
# lets create a table 

# -------------------------------------------------------------------------
# |  Method    |  when to use it               |    code example           |
# | -----------|-------------------------------|---------------------------|
# |  drop rows |  if the missing data is small | df.dropna()               |
# |            | in number                     |                           |
# | coloumns   |                               | df.dropna(axis=1)         |
# |fill with   |for numerical columns          | df.fillna(df.mean())      |   df['column'].fillna(df['column'].mean())|
# | mean       |                               |                           |
# | fill with  |for categorical columns        | df.fillna(df.mode())      |   df['column'].fillna(df['column'].mode())|
# | mode       |                               |                           |
# | fill with  |for categorical columns        | df.fillna(df.median())    |   df['column'].fillna(df['column'].median())|
# | median     |                               |                           |
# | custom fill| if you want to fill with a    | df.fillna(0)              |
# | value      | custom value                  |                           |
# --------------------------------------------------------------------------

# the table above is a summary of the methods to handle missing values in pandas. 

# handling the duplicates
# how do we handle duplicates in pandas?
# df.duplicated() returns a boolean series indicating if each row is a duplicate
# df.drop_duplicates() drops the duplicate rows from the dataframe 

# df.drop_duplicates(subset=['column1', 'column2']) drops the duplicate rows based on the specified columns
# df.drop_duplicates(keep='first') keeps the first occurrence of the duplicate rows specified by the subset parameter
# keeping the first row of the duplicate rows we use the function df.drop_duplicates(keep='first')
# keeping the last row of the duplicate rows we use the function df.drop_duplicates(keep='last')
# keeping all the duplicate rows we use the function df.drop_duplicates(keep=False) -- this will drop all the duplicate rows 


# Lesson 2: Detecting and handling outliers 
# detecting outliers
# outliers are values that are significantly different from the rest of the data
# outliers can be detected using the IQR method
# IQR method
# IQR = Q3 - Q1
# Q1 = 25th percentile
# Q3 = 75th percentile
# IQR = Q3 - Q1

# code example 
Q1 = df['column'].quantile(0.25)  # 25th percentile
Q3 = df['column'].quantile(0.75)  # 75th percentile
IQR = Q3 - Q1

# Lower bound = Q1 - 1.5 * IQR   1.5 is used to determine the threshold for outliers 
# Upper bound = Q3 + 1.5 * IQR

outliers = df[(df['column'] < (Q1 - 1.5 * IQR)) | (df['column'] > (Q3 + 1.5 * IQR))]
# this will return a dataframe with the outliers 
# the outliers have been detected using the IQR method in the code above 
# explanation of the code above
# 1. Q1 and Q3 are calculated using the quantile method
# 2. IQR is calculated by subtracting Q1 from Q3
# 3. the lower bound and upper bound are calculated using the IQR method
# 4. the outliers are detected using the lower and upper bounds
# 5. the outliers are returned as a dataframe  


# handling outliers
# 1. remove the outliers from the dataframe
#  code example
df = df[~df['column'].isin(outliers['column'])] # this will remove the outliers from the dataframe 
# 2. replace the outliers with the mean or median
#  code example 
df.loc[df['column'] < (Q1 - 1.5 * IQR), 'column'] = df['column'].mean() # this will replace the outliers with the mean
df.loc[df['column'] > (Q3 + 1.5 * IQR), 'column'] = df['column'].median() # this will replace the outliers with the median

# df.loc is used to access a group of rows and columns by labels or a boolean array 

# visualizing outliers
import seaborn as sns
import matplotlib.pyplot as plt

# boxplot
sns.boxplot(x=df['column'])
plt.show() # this will show the boxplot of the column 

# histogram
sns.histplot(df['column'])
plt.show() # this will show the histogram of the column 
 

