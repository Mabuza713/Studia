import random
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np

x_data1 = []
x_data2 = []

def func1(x):
    x_data1.append(x)
    return 0.5 * x + 50 +random.uniform(0, 5)

def func2(x):
    x_data2.append(x)
    return 0.5 * x + 10+random.uniform(0, 3)

# Generate data
data1 = [func1(random.uniform(0, x)) for x in range(1, 100)]
data2 = [func2(random.uniform(100, x)) for x in range(1, 100)]
data3 = []
x_data3 = []
for i in range(0,len(data1)):
    data3.append(data1[i])
    x_data3.append(x_data1[i])
for i in range(0,len(data2)):
    data3.append(data2[i])
    x_data3.append(x_data2[i])

# Split the data for regression
X_train1, X_test1, y_train1, y_test1 = train_test_split(np.array(x_data1), np.array(data1), test_size=0.25)
X_train2, X_test2, y_train2, y_test2 = train_test_split(np.array(x_data2), np.array(data2), test_size=0.25)
X_train3, X_test3, y_train3, y_test3 = train_test_split(np.array(x_data3), np.array(data3), test_size=0.25)
# Reshape data for sklearn
X_train1 = X_train1.reshape(-1, 1)
X_train2 = X_train2.reshape(-1, 1)
X_train3 = X_train3.reshape(-1, 1)
# Fit linear regression models
model1 = LinearRegression()
model1.fit(X_train1, y_train1)

model2 = LinearRegression()
model2.fit(X_train2, y_train2)

model3 = LinearRegression()
model3.fit(X_train3, y_train3)

# Predictions for the training set
y_pred1 = model1.predict(X_train1)
y_pred2 = model2.predict(X_train2)
y_pred3 = model3.predict(X_train3)

# Plotting
plt.figure(figsize=(12, 6))

# Data1 plot
plt.subplot(1, 1, 1)
plt.scatter(x_data1, data1, label='Data 1', color='blue')
plt.plot(X_train1, y_pred1, color='red', linewidth=2, label='Linear Regression 1')
plt.title('Data 1 with Linear Regression')
plt.xlabel('X Data 1')
plt.ylabel('Y Data 1')
plt.legend()

# Data2 plot
plt.subplot(1, 1, 1)
plt.scatter(x_data2, data2, label='Data 2', color='green')
plt.plot(X_train2, y_pred2, color='orange', linewidth=2, label='Linear Regression 2')
plt.title('Data 2 with Linear Regression')
plt.xlabel('X Data 2')
plt.ylabel('Y Data 2')
plt.legend()


plt.subplot(1, 1, 1)
plt.plot(X_train3, y_pred3, color='pink', linewidth=2, label='Linear Regression 1')
plt.title('Data 1 with Linear Regression')
plt.xlabel('X Data 1')
plt.ylabel('Y Data 1')
plt.legend()

plt.tight_layout()
plt.show()
