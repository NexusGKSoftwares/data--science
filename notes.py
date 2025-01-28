# descriptive statitics
# mean , median, mode , variance, standard deviation, 

# mean - average of the data points
# median - middle value of the data points when it is sorted in aascending order 
# mode - the value that appears most frequently in the data points
# variance - measure of how spread out the data points in  data set are  around the mean
# standard deviation - square root of the variance; represents the average 
# deviation of each data point from the mean

# # mean
# import numpy as np
# data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print('Mean:', np.mean(data))
# print('Median:', np.median(data))
# print('Mode:', max(set(data), key=data.count))
# print('Variance:', np.var(data))
# print('Standard deviation:', np.std(data))

# data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100] task

# which statistics is most resistant to outliers?
# median is most resistant to outliers  
# outliers are data points that are significantly different from other data points in a data set
#  for example in the data set [1, 2, 3, 4, 1000], the median is 3, while the mean is 202
#  the mean is significantly affected by the outlier 1000, while the median is not
#  thus, the median is more resistant to outliers than the mean

# dataset which will use is titanic dataset from seaborn library 
# we will use the age column from the dataset to demonstrate the effect of outliers on the mean and median
# we will load the dataset and calculate the mean and median of the age column

import seaborn as sns
import pandas as pd

titanic = pd.read_csv('test.csv')
# print(titanic.head())

# age column

# print('Mean:', titanic['Age'].mean())
# print('Median:', titanic['Age'].median())
# print('Mode:', titanic['Age'].mode()[0])
# print('Variance:', titanic['Age'].var())
# print('Standard deviation:', titanic['Age'].std())

# real life example of the effect of outliers on the mean and median
# consider the finance sector where the salary of employees in a company is being analyzed
# calculating average salary of employees in the company, expenses, and revenue/returns on investment
# consider education sector where the average score of students in a class is being calculated

# variance and standard deviation are critical in real life scenarios since 
# it help to understand the spread of data points in a data set/ variability of data points

# finance sector - variance and standard deviation are used to measure the risk associated with an investment

# fraud scenario - variance and standard deviation are used to detect fraud in financial transactions
# if the variance and standard deviation of a transaction are significantly different from the mean,
# it may be an indication of fraud

# sample 
#  if a customer's average daily spending is $100, and the standard deviation is $20
#  if the customer spends $200 in a day, it may be an indication of fraud
#  since the spending is significantly different from the mean
#  the standard deviation is used to determine how far the data points are from the mean


# fare column

# print('Mean:', titanic['Fare'].mean())
# print('Median:', titanic['Fare'].median())
# print('Mode:', titanic['Fare'].mode()[0])
# print('Variance:', titanic['Fare'].var())
# print('Standard deviation:', titanic['Fare'].std())

# correlation - strength of the relationship between two variables
# correlation is a statistical measure that describes the relationship between two variables
# it indicates the extent to which two variables change together
# correlation can be positive, negative, or zero
# positive correlation - both variables move in the same direction
# negative correlation - both variables move in opposite directions
# zero correlation - no relationship between the variables

# correlation coefficient - a value that ranges from -1 to 1

# covariance - a measure of how two variables change together -direction of the relationship between two variables
# it indicates the extent to which two variables change together
# covariance can be positive, negative, or zero
# positive covariance - both variables move in the same direction
# negative covariance - both variables move in opposite directions
# zero covariance - no relationship between the variables

# correlation coefficient - a value that ranges from -1 to 1
# 1 - perfect positive correlation
# -1 - perfect negative correlation
# 0 - no correlation

# real life example of correlation
# consider the finance sector where the correlation between two stocks is being analyzed
# to determine the extent to which the stocks move together
# consider the education sector where the correlation between study time and exam scores is being analyzed
# to determine the extent to which study time affects exam scores


# example 
import numpy as np
# advertising = [10, 20, 300, 400, 500]
# sales = [50, 150, 250, 350, 450]

# # calculate the covariance
# covariance = np.cov(advertising, sales)[0][1]
# print('Covariance:', covariance)

# calculate the correlation coefficient
# correlation = np.corrcoef(advertising, sales)[0][1]
# print('Correlation coefficient:', correlation)

# example of real dataset
# consider the titanic dataset from seaborn library
# we will calculate the correlation between the age and fare columns in the dataset
# to determine the relationship between the age of passengers and the fare they paid

# calculate the covariance
covariance = np.cov(titanic['Age'], titanic['Fare'])[0][1]
print('Covariance:', covariance)

# calculate the correlation coefficient
correlation = np.corrcoef(titanic['Age'], titanic['Fare'])[0][1]
print('Correlation coefficient:', correlation)