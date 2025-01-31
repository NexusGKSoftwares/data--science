# descriptive statitics
# mean , median, mode , variance, standard deviation, 

# mean - average of the data points
# median - middle value of the data points when it is sorted in aascending order 
# mode - the value that appears most frequently in the data points
# variance - measure of how spread out the data points in  data set are  around the mean
# standard deviation - square root of the variance; represents the average 
# deviation of each data point from the mean

# # mean
import numpy as np
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

titanic = pd.read_csv('train.csv')
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

# correlation in an heat map visualization
# sns.heatmap(titanic.corr(), annot=True, cmap='coolwarm')
# plt.title('correlation heatmap')
# plt.show()

# real life example of correlation
# consider the finance sector where the correlation between two stocks is being analyzed
# to determine the extent to which the stocks move together
# consider the education sector where the correlation between study time and exam scores is being analyzed
# to determine the extent to which study time affects exam scores

# real life example of covariance
# consider the finance sector where the covariance between two stocks is being analyzed
# to determine the extent to which the stocks move together

# consider the education sector where the covariance between study time and exam scores is being analyzed
# to determine the extent to which study time affects exam scores
# correlation and covariance are used to analyze the relationship between two variables


# example 
import numpy as np
# advertising = [1000, 2000, 300, 400, 500]
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
# covariance = np.cov(titanic['Age'], titanic['Fare'])[0][1]
# print('Covariance:', covariance)

# calculate the correlation coefficient
# correlation = np.corrcoef(titanic['Age'], titanic['Fare'])[0][1]
# print('Correlation coefficient:', correlation)

# introduction to Exploratory Data Analysis

# Exploratory Data Analysis (EDA) is an approach to analyzing data sets to summarize their main characteristics 

# eda is a process of examining datasets to summarise their main characteristics, often with visual methods
# it helps to understand the data, identify patterns, relationships, and anomalies in the data
# it is an important step in the data analysis process as it provides insights into the data

#  why eda is important
# 1. understand the data - eda helps to understand the data and its structure
# 2. identify patterns - eda helps to identify patterns and relationships in the data
# 3. detect anomalies - eda helps to detect anomalies and outliers in the data
# 4. make informed decisions - eda helps to make informed decisions based on the data
# 5. communicate insights - eda helps to communicate insights and findings to stakeholders
# 6. improve data quality - eda helps to improve data quality by identifying and addressing data

# steps of eda
# 1. load the data - load the dataset into the analysis environment
# 2. check the data - check the data for missing values, duplicates, and outliers
# 3. explore the data - explore the data using descriptive statistics and visualizations
# 4. analyze the data - analyze the data to identify patterns, relationships, and anomalies
# 5. interpret the data - interpret the data to draw insights and make informed decisions
# 6. communicate the results - communicate the results to stakeholders using visualizations and reports

# tools for eda
# 1. python - pandas, numpy, matplotlib, seaborn
# pandas - data manipulation and analysis and summary statistics
# numpy - numerical computing and array operations
# matplotlib - data visualization and plotting
# seaborn - data visualization and statistical graphics

# example of eda
# consider the titanic dataset from seaborn library
# we will perform eda on the dataset to understand the data, identify patterns, and relationships

# load the data
df = pd.read_csv('train.csv')

# print(df.head())
# print(df.info())
# print(df.describe())

# check for the missing values
# print(df.isnull().sum())

import seaborn as sns
import matplotlib.pyplot as plt

# set the seaborn style
sns.set_theme(style='darkgrid')

#  2 customizing maplotlib and seaborn plots

#   - it helps us to enhance the readability and impact
#   - figure size, labels and titles



# sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
# plt.title('missing values')
# plt.show()

# summarise the dataset
# print(df.describe())
 
# analyse the data distribution using an histogram

# sns.histplot(df['Age'], bins=30, kde=True)
# plt.title('Age distribution')
# plt.show()

# explore the relationship between age and fare using a scatter plot
# sns.scatterplot(x='Age', y='Fare', data=df)
# plt.title('Age vs Fare')
# plt.show()

# #  sns regplot
# sns.regplot(x='Age', y='Fare', data=df)
# plt.title('Age vs Fare')
# plt.show()


# data visualization techniques in eda
# 1. histograms - visualize the distribution of a numerical variable
# 2. scatter plots - visualize the relationship between two numerical variables
# 3. box plots - visualize the distribution of a numerical variable by quartiles
# 4. bar plots - visualize the distribution of a categorical variable/ dataset
# 5. line plots - visualize the trend of a numerical variable over time
# 6. heatmaps - visualize the correlation between numerical variables
# 7. pair plots - visualize the relationship between numerical variables in a dataset

# common Data Visualization Techniques
# 1. univariate analysis - analysis of a single variable
#   - histograms
#    shows the distribution of a numerical data
#    helps to identify patterns and anomalies in the data
    #  example - age distribution in a dataset
# sns.histplot(df['Age'], bins=30, kde=True)
# plt.title('Age distribution')
# plt.show()


# 2. bivariate analysis - analysis of two variables
#   - scatter plots(relationship between two numerical variables)
#  helps to identify the trends and correlations between two variables

#   - bar plots (distribution of a categorical variable)
#   helps to identify the distribution of a categorical variable in a dataset
#   example
# sns.countplot(x='Sex', data=df)
# plt.title('number of passengers by Gender')
# plt.xlabel('gender')
# plt.ylabel('count')
# plt.show()
    
# 3. multivariate analysis - analysis of more than two variables
#   - pair plots (relationship between multiple numerical variables)
#   helps to identify the relationships between multiple numerical variables in a dataset
#   example
# sns.pairplot(df[['Age', 'Fare', 'Sex', 'Pclass']])
# plt.title('pair plot')
# plt.show()

# advanced data visualization with seaborn and matplotlib


# 1 setting up the environment
#   - install the required libraries
#   - import the required libraries

# set the seaborn style
sns.set_theme(style='darkgrid')

#  2 customizing maplotlib and seaborn plots

#   - it helps us to enhance the readability and impact
#   - figure size, lables and titles

# plt.figure(figsize=(10, 6))
# sns.histplot(data=df, x='Age', bins=30, kde=True)
# plt.title('Age distribution')
# plt.xlabel('Age')
# plt.ylabel('count')
# plt.show()

# custom color palettes
# seaborn offers built in palletes like coolwarm, viridis and magma

sns.set_palette('viridis')

# custom_pallete = ["#FF6F61", "#6B4226", "#FFC107", "#8BC34A"]
# sns.set_palette(custom_pallete)


# 3 Advanced Seaborn Plots

#   - pairplot(multivariate analysis)
#   enables us to visualize relationships in numerical data
#   example
# sns.pairplot(df[['Age', 'Fare', 'Survived', 'Pclass']])
# plt.title('pair plot')
# plt.show()

#  - heatmap(correlation Matrix)

# plt.figure(figsize=(10, 6))
# sns.heatmap(df.corr(), annot=True, cmap='coolwarm', square=True)
# plt.title('correlation matrix')
# plt.show()

#  - boxplot (outlier detection)

# plt.figure(figsize=(10, 6))
# sns.boxplot(data=df, x='Age')
# plt.title('box plot')
# plt.show()

# violin plot (distribution & density)

# plt.figure(figsize=(10, 6))
# sns.violinplot(data=df, x='Age')
# plt.title('violin plot')
# plt.show()

# Facegrid(multiple plot in one figure)

# plt.figure(figsize=(10, 6))
# g = sns.FacetGrid(df, col='Survived', hue="Pclass", height=4)
# g.map(sns.scatterplot, 'Age', 'Fare').add_legend()
# plt.show()


# 4 combining the seaborn & matplotlib
# we can use matplotlib to add more features to seaborn plots
# example

# fig, ax = plt.subplots(figsize=(10, 6))
# sns.scatterplot(data=df, x='Age', y='Fare' )
# ax.set_title('Scatter plot')
# ax.set_xlabel('Age')
# ax.set_ylabel('Fare')
# plt.xticks(rotation=45)
# plt.show()

# 5 interactive plots with seaborn and matplotlib
# we can use interactive plots to explore data in more detail
# example
import plotly.express as px
# import plotly.graph_objects as go
# fig = px.scatter(df, x='Age', y='Fare')
# fig.show()

# using mplcursors for hover display 
import mplcursors

# fig, ax = plt.subplots()
# scatter = sns.scatterplot(df, x="Age", y="Fare", hue="Survived", alpha=0.7)

# # add interactive hover tooltips
# cursor = mplcursors.cursor(scatter, hover=True)
# cursor.connect("add", lambda sel: sel.annotation.set_text(f"Age: {sel.target[0]:.1f}\nFare: {sel.target[1]:.2f}"))

# plt.show()

# install mplcursors using pip install mplcursors
# !pip install mplcursors

# interactive histogram with seaborn and plotly
# import plotly.express as px
# fig = px.histogram(df, x="Age", nbins=50, title="Histogram of Age", color_discrete_sequence=["#3498db"], hover_data=["Fare"])
# fig.show()


# interactive boxplot using plotly
# import plotly.express as px
# fig = px.box(df, x="Pclass", y="Fare", title="Box", color="Pclass", hover_data=["Sex", "Age"])
# fig.show()

# interactive filtering with ipwidgets
import ipywidgets as widgets
from  IPython.display import display
# create a dropdown widget
# pclass = widgets.Dropdown(options=['1st', '2nd', '3rd'],value='1st',description='Pclass:',disabled=False)
# # display the widget
# display(pclass)


class_selector = widgets.Dropdown(options=["All"] + list(df['Pclass'].unique()), value="All", description='Pclass:', disabled=False)

def update_plot(selected_class):
    plt.clf()
    filtered_data = df if selected_class == "All" else df[df['Pclass'] == selected_class]
    sns.histplot(data = filtered_data, x="Age", y="Fare", hue="Survived", bins=20, kde=True)
    plt.title(f"age distribution - {selected_class}")
    plt.show()
    
widgets.interactive(update_plot, selected_class=class_selector)
display(class_selector)


# conclusion
# use mplcursors to add interactive hover tooltips to plots
# use plotly to create interactive bar, scatter and box plots
# use ipywidgets to create interactive dropdown menus and sliders to filter data