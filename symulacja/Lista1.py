import random

import matplotlib.pyplot as plt
from math import  sqrt
import numpy as np

import scipy.stats as stats
random.seed(3)
class DiskThrow:
    def __init__(self, max_x, max_y, amount_of_throws):
        self.max_x = max_x
        self.max_y = max_y

        self.circle_1st = [10, 0]
        self.circle_2nd = [10, 20]
        self.amount_of_thorws = amount_of_throws
        self.stats = []

    def RandomCordinats(self):
        temp = [random.uniform(0, self.max_x), random.uniform(0, self.max_y)]
        return temp


    def CheckPoints(self, shoot_cordinates):
        distance1_temp = 0
        distance2_temp = 0
        for i in range(0, 2):
            distance1_temp += (self.circle_1st[i] - shoot_cordinates[i])**2
            distance2_temp += (self.circle_2nd[i] - shoot_cordinates[i])**2

        distance1 = sqrt(distance1_temp)
        distance2 = sqrt(distance2_temp)

        amount_of_points_1 = 10
        amount_of_points_2 = 10

        final_points = 0

        added1 = False
        added2 = False
        for i in range(0,11):
            if (1 + i >= distance1 and added1 == False):
                final_points += amount_of_points_1
                added1 = True
            else:
                amount_of_points_1 -= 1

            if (i + 1 >= distance2 and added2 == False):
                final_points += amount_of_points_2
                added2 = True
            else:
                amount_of_points_2 -= 1

        return [final_points, distance1, distance2]




    def SimulateThrows(self):
        for i in range(0, self.amount_of_thorws):
            throw = self.RandomCordinats()
            amount_of_points = self.CheckPoints(throw)
            self.stats.append(amount_of_points[0])

    def CalculateMeanAndSD(self, verbose = True):
        mean_temp = 0
        sd_temp = 0
        for i in range(0, self.amount_of_thorws):
            mean_temp += self.stats[i]

        mean = mean_temp / len(self.stats)


        for i in range(0, self.amount_of_thorws):
            sd_temp = (self.stats[i] - mean)**2

        sd = sqrt(sd_temp / (len(self.stats) -1))
        if verbose:
            print(f"mean: {mean}")
            print(f"sd: {sd}")

        return mean, sd

    def CheckIfRelevant(self, critical_value):
        mean, sd = self.CalculateMeanAndSD(False)

        value = sqrt(self.amount_of_thorws) * (mean - 5) / sd

        if (value > critical_value):
            print("Rejecting null hipo")
        else:
            print("NOT rejecting null hip")
    
    
    
    def Histogram(self):
        a = np.hstack(self.stats)
        plt.title(f"amount of throws:{self.amount_of_thorws}")
        plt.hist(a, bins = range(0,12), align= "left", edgecolor ="black")
        plt.xticks(range(0,12))
        plt.xlabel("points")
        plt.ylabel("frequency")
        plt.show()


    def TestIfUnif(self):
        sample_data = np.full(shape = (1, 11), fill_value = self.amount_of_thorws / 11)
        sample_data = sample_data[0].tolist()

        hist_of_our_data = [self.stats.count(x) for x in range(0,11)]
        chi_val = 0
        for i in range(0, len(sample_data)):
            chi_val += ((sample_data[i] - hist_of_our_data[i]) ** 2)/sample_data[i]

        if (chi_val >= stats.chi2.ppf(0.95, len(sample_data) - 1)):
            print(f"For amount of throws:{self.amount_of_thorws} <- reject null hypothesis")
        else:
            print(f"For amount of throws:{self.amount_of_thorws} <- accept null hypothesis")
        

#creating objects
Throw10 = DiskThrow(20,20,10)
Throw100 = DiskThrow(20,20,100)
Throw1000 = DiskThrow(20,20,1000)


#Simulating throws
Throw10.SimulateThrows()
Throw100.SimulateThrows()
Throw1000.SimulateThrows()

#Calcualting mean and sd
print("for 10")
Throw10.CalculateMeanAndSD()
print("\nfor 100")
Throw100.CalculateMeanAndSD()
print("\nfor 1000")
Throw1000.CalculateMeanAndSD()

# Test
print()
print("significancy test")
print("for 10")
Throw10.CheckIfRelevant(2.228)
print("\nfor 100")
Throw100.CheckIfRelevant(1.984)
print("\nfor 1000")
Throw1000.CheckIfRelevant(1.962)


##histogram
Throw10.Histogram()
Throw100.Histogram()
Throw1000.Histogram()

# Uniformity test wanna kms
Throw10.TestIfUnif()
Throw100.TestIfUnif()
Throw1000.TestIfUnif()