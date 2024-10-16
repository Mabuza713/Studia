import random

import matplotlib.pyplot as plt
from math import sqrt
import numpy as np

import scipy.stats as stats



class Object:
    def __init__(self,how_much):
        self.how_much = how_much
        self.stats = []

    def Random_sim(self):
        return random.uniform(-1,1)


    def Simulate(self):
        for i in range(0, self.how_much):
            self.stats.append(self.Random_sim())

    def CalculateMeanAndSD(self, verbose=True):
        mean_temp = 0
        sd_temp = 0
        for i in range(0, self.how_much):
            mean_temp += self.stats[i]

        mean = mean_temp / len(self.stats)

        for i in range(0, self.how_much):
            sd_temp = (self.stats[i] - mean) ** 2

        sd = sqrt(sd_temp / (len(self.stats) - 1))
        if verbose:
            print(f"mean: {mean}")
            print(f"sd: {sd}")

        return mean, sd

    def CalculateMedian(self):
        lista = self.stats
        lista.sort()
        print(lista)
        if (self.how_much % 2 == 0):
            return ((lista[self.how_much // 2]) + (lista[self.how_much // 2 - 1]))/2
        else:
            return (lista[self.how_much // 2])

    def CalculateVariance(self):
        mean, sd = self.CalculateMeanAndSD()
        return sd*sd

    def CalculateSkosnosc(self):
        mean, sd = self.CalculateMeanAndSD()
        skonsonc_temp = 0
        for i in range(0, self.how_much):
            skonsonc_temp = (self.stats[i] - mean) ** 3
        skosnosc = skonsonc_temp * self.how_much / (self.how_much - 1)/ (self.how_much - 2) / sd / sd / sd

        return skosnosc

    def CalculateKurtuoza(self):
        pierwszy = self.how_much * (self.how_much + 1) / (self.how_much - 1) . (self.how_much - 2) / (self.how_much - 3)

        mean, sd = self.CalculateMeanAndSD()

        temp = 0
        for i in range(0, self.how_much):
            temp += ((self.stats[i] - mean) / sd) * ((self.stats[i] - mean) / sd) * ((self.stats[i] - mean) / sd) * ((self.stats[i] - mean) / sd)

        dwa = 3 * (self.how_much - 1) * (self.how_much - 1) / (self.how_much - 2) / (self.how_much - 3)
        return pierwszy * temp - dwa

    def CalculateMode(self):
        hist_of_our_data = [self.stats.count(x) for x in self.stats]
        if (len(hist_of_our_data) == 1):
            return "no mode"
        else:
            max_amount =0
            mode = 0
            for i in range(0, self.how_much):
                if (self.stats.count(self.stats[i]) > max_amount):
                    max_amount = self.stats.count(self.stats[i])
                    mode = self.stats[i]
        return mode



    def CheckIfRelevant(self, critical_value):
        mean, sd = self.CalculateMeanAndSD(False)
        value = sqrt(self.how_much) * mean / sd

        if (value > critical_value):
            print("Rejecting null hipo")
        else:
            print("NOT rejecting null hip")



    def histogram_discreet(self):
        a = np.hstack(self.stats)
        plt.title(f"amount of throws:{self.how_much}")
        plt.hist(a, align="left", edgecolor="black")
        plt.xlabel("points")
        plt.ylabel("frequency")
        plt.show()


object_15 = Object(15)
object_120 = Object(120)

object_15.Simulate()
object_120.Simulate()


object_15.histogram_discreet()
object_120.histogram_discreet()


