import random
import statistics
import matplotlib.pyplot as plt

import matplotlib
from math import sqrt



class Shoot:
    def __init__(self,max_x, max_y, amount_of_shots):
        self.max_x = max_x
        self.max_y = max_y
        self.middle_cordinates = [max_x / 2, max_y / 2]
        self.amount_of_shots = amount_of_shots
        self.archer_stats = None

    def ArcherShot(self):
        shot_coordinates = [random.uniform(0, self.max_x), random.uniform(0, self.max_y)]
        return shot_coordinates

    def HowMuchPoints(self, shoot_coordinates):
        temp = 0
        for i in range(0,2):
            temp += (self.middle_cordinates[i] - shoot_coordinates[i])**2

        how_far_from_middle = sqrt(temp)

        amount_of_points = 10
        for i in range(0,10):
            if (2 + 2*i >= how_far_from_middle):
                return  [amount_of_points, how_far_from_middle]
            else:
                amount_of_points -= 1
        return [0, how_far_from_middle]

    def ShootSimulation(self, verbose = False):
        archer_stats = []
        for i in range(self.amount_of_shots):
            shoot_coordinates = self.ArcherShot()
            result = self.HowMuchPoints(shoot_coordinates)
            archer_stats.append(result[0])

            if verbose:
                print(f"{i}- amount of points:{result[0]} distance from middle: {result[1]} shoot cordinates:{shoot_coordinates}")
        self.archer_stats = archer_stats
        return archer_stats

    def CalculateMeanAndSD(self, verbose = False):
        archer_stats = self.archer_stats
        mean_stats = sum(archer_stats)/len(archer_stats)

        temp = 0
        for i in range(len(archer_stats)):
            temp += (archer_stats[i] - mean_stats)**2

        standard_deviation = sqrt(temp/ (len(archer_stats) - 1))

        if verbose:
            print(f"mean: {mean_stats} using statistics: {statistics.mean(archer_stats)}")
            print(f"standard deviation: {standard_deviation} using statistics: {statistics.stdev(archer_stats)}")
        return [standard_deviation, mean_stats]

    def IsStatisticalSignificant(self, critical_value):
        temp = self.CalculateMeanAndSD(False)

        standard_deviation = temp[0]
        mean = temp[1]
        t_value = sqrt(self.amount_of_shots)*(mean - 5) / standard_deviation
        if (abs(t_value) > critical_value):
            print("difference is statisticly significant")
        else:
            print("difference is NOT statisticly significant")


    def CreateHistogram(self):
        plt.hist(self.archer_stats)
        plt.xlabel("points")
        plt.ylabel("how much occurance")
        plt.savefig("ds.png")
#create obj
obj10 = Shoot(40,40, 10)
obj100 = Shoot(40,40, 100)
obj1000 = Shoot(40,40, 100000)


# simulate shoots for objects
obj10.ShootSimulation(True)
obj100.ShootSimulation()
obj1000.ShootSimulation()


#create histogram
obj1000.CreateHistogram()


# calculate mean and standard deviation
obj10.CalculateMeanAndSD()
obj100.CalculateMeanAndSD()
obj1000.CalculateMeanAndSD()

#check if its significant
obj10.IsStatisticalSignificant(2.28)
obj100.IsStatisticalSignificant(1.984)
obj1000.IsStatisticalSignificant(1.962)
