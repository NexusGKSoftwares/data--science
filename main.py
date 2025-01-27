import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
# from sklearn.linear_model import LinearRegression
# from sklearn.preprocessing import PolynomialFeatures
# Load the data
# data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# plt.hist(data, bins=5, color='skyblue', edgecolor='black')
# plt.title('Histogram of data')
# plt.xlabel('Data')
# plt.ylabel('Frequency')
# plt.show()



# unique_values = pd.Series(data).value_counts()
# unique_values.plot(kind='bar', color='skyblue', edgecolor='black')
# plt.title('Bar plot of data')
# plt.xlabel('Data')
# plt.ylabel('Frequency')
# plt.show()

# x = np.random.randint(10, 50, 15)
# y = 2 * x + np.random.randint(10, 50, 15)
# sns.scatterplot(x=x, y=y)

# plt.title('Scatter plot of x and y')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.show()

# sns.regplot(x=x, y=y, scatter_kws={'color': 'skyblue'}, line_kws={'color': 'black'})
# plt.title('Scatter plot with trendline of x and y')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.show()
# file_path = 'dataset.csv'  
# df = pd.read_csv(file_path)
# df['Latitude'] = pd.to_datetime(df['Latitude'])


# # plot
# plt.scatter(df['Latitude'], df['Longitude'],
# color='orange', alpha=0.5, edgecolor='black')
# plt.title('Scatter plot of Latitude and Longitude')
# plt.xlabel('Latitude')
# plt.ylabel('Longitude')
# plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
# plt.show()

# fires_by_cause = df['Hazard Type'].value_counts()
# fires_by_cause.plot(kind='bar', color='skyblue', edgecolor='black')
# plt.title('Bar plot of fires by Hazard Type')
# plt.xlabel('Hazard Type')
# plt.ylabel('Frequency')
# plt.show()

# pie chart
# fire_by_cause = df['Hazard Type'].value_counts()

# # create a pie chart
# plt.pie(fire_by_cause, labels=fire_by_cause.index, autopct='%1.1f%%', startangle=140)
# plt.axis('equal')
# plt.title('Pie chart of fires by Hazard Type')
# plt.show()

# polynomial regression

# create a sample dataset
# x = np.linspace(0, 10, 100)
# y = np.sin(x)  + np.random.normal(0, 3, 100)

# # polynomial features transformations (degree = 2)
# poly = PolynomialFeatures(degree=2)
# X_poly = poly.fit_transform(x.reshape(-1, 1))

# # fit the model
# model = LinearRegression()
# model.fit(X_poly, y)

# # plotting the scatter plot and regrerssion curve
# plt.scatter(x, y, color='skyblue', lable='data')
# plt.plot(x, model.predict(X_poly), color='black', label='regression curve')
# plt.title('Polynomial regression')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.legend()
# plt.show()

# create a histogram of total_bill to show its distribution
# draw a box plot for a total_bill to identify 