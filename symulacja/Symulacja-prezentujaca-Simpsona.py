import random
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

x_data1 = []
x_data2 = []

def func1(x):
    x_data1.append(x)
    return 0.5*x + 100 + random.uniform(0,5)



def func2(x):
    x_data2.append(x)
    return 0.5*x + 1.7 + random.uniform(0,3)


data1 = [func1(random.uniform(0,x)) for x in range(0,100)]
data2 = [func2(random.uniform(0,x)) for x in range(0,100)]




plt.scatter(x_data1,data1)
plt.scatter(x_data2, data2)

plt.plot(data1)
plt.plot(data2)



