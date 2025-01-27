# descriptive statitics
# mean , median, mode , variance, standard deviation, 

# mean - average of the data points
# median - middle value of the data points when it is sorted in ascending order 
# mode - the value that appears most frequently in the data points
# variance - measure of how spread out the data points in a data set are  around the mean
# standard deviation - square root of the variance; represents the average 
# deviation of each data point from the mean

# # mean
import numpy as np
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print('Mean:', np.mean(data))
print('Median:', np.median(data))
print('Mode:', max(set(data), key=data.count))
print('Variance:', np.var(data))
print('Standard deviation:', np.std(data))

# data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100] task

# which statistics is most resistant to outliers?
# median is most resistant to outliers  
# outliers are data points that are significantly different from other data points in a data set
#  for example in the data set [1, 2, 3, 4, 1000], the median is 3, while the mean is 202
#  the mean is significantly affected by the outlier 1000, while the median is not
#  thus, the median is more resistant to outliers than the mean