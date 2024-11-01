import random
import matplotlib.pyplot as plt
from math import sqrt
import numpy as np
import scipy.stats as stats
import time
random.seed(3)


class Object:
    def __init__(self,how_much,a, b, m, seed):
        self.how_much = how_much
        self.stats = []
        self.a = a
        self.b = b
        self.m = m
        self.seed = seed

    def Random_sim(self, x):
        return (((self.a * x + self.b) % self.m) / self.m) * 2 - 1

    def Simulate(self):
        self.stats.append(self.Random_sim(self.seed))
        for _ in range(0, self.how_much):
            self.stats.append(self.Random_sim(self.stats[-1]))

    # Statistics calculations
    def CalculateMeanAndSD(self, verbose=False):
        mean_temp = 0
        sd_temp = 0
        #print(f"sd {np.std(self.stats)}")
        #print(f"mean {np.mean(self.stats)}")
        for i in range(0, self.how_much):
            mean_temp += self.stats[i]

        mean = mean_temp / len(self.stats)

        for i in range(0, self.how_much):
            sd_temp += (self.stats[i] - mean) ** 2

        sd = sqrt(sd_temp / (len(self.stats) - 1))
        if verbose:
            print(f"mean: {mean}")
            print(f"sd: {sd}")

        return mean, sd

    def CalculateMedian(self):
        lista = self.stats
        lista.sort()
        print(f"median {np.median(lista)}")
        if (self.how_much % 2 == 0):
            return ((lista[self.how_much // 2]) + (lista[self.how_much // 2 - 1]))/2
        else:
            return (lista[self.how_much // 2])

    def CalculateVariance(self):
        mean, sd = self.CalculateMeanAndSD()
        print(f"variance {np.var(self.stats)}")
        return sd*sd

    def CalculateSkewness(self):
        mean, sd = self.CalculateMeanAndSD()
        skewness_temp = 0
        for i in range(0, self.how_much):
            skewness_temp += ((self.stats[i] - mean) / sd) ** 3
        skewness = skewness_temp * self.how_much / (self.how_much - 1) / (self.how_much - 2) 
        print(stats.skew(self.stats, bias= True))
        return skewness

    def CalculateKurtosis(self):
        first = self.how_much * (self.how_much + 1) / (self.how_much - 1) / (self.how_much - 2) / (self.how_much - 3)
        mean, sd = self.CalculateMeanAndSD()

        temp = 0
        for i in range(0, self.how_much):
            temp += ((self.stats[i] - mean) / sd) ** 4

        second = 3 * (self.how_much - 1) * (self.how_much - 1) / (self.how_much - 2) / (self.how_much - 3)
        
        print(f"kurtoza {stats.kurtosis(self.stats)}" )
        return first * temp - second


    def CalculateMode(self):
        if (self.how_much == len(set(self.stats))):
            return "No mode"
        else:
            frequency = {}
            for value in self.stats:
                if value in frequency:
                    frequency[value] += 1
                else:
                    frequency[value] = 1
            
            max_frequency = max(frequency.values())
            modes = [key for key, value in frequency.items() if value == max_frequency]
            
            if len(modes) == 1:
                return modes[0]
            else:
                return modes
        
    def CalculatePercentile(self, percentile):
        lista = self.stats
        lista.sort()

        index = (self.how_much - 1) * percentile / 100
        if (index - int(index) == 0):
            return lista[int(index)]
        
        lower = int(np.floor(index))
        upper = int(np.ceil(index))
        interpolation = index - lower
        
        return (1- interpolation) * lista[lower] + interpolation * lista[upper]
        
        

    def CheckIfRelevant(self, critical_value):
        mean, sd = self.CalculateMeanAndSD(False)
        value = sqrt(self.how_much) * mean / sd
        
        if (abs(value) > critical_value):
            print(f"for {self.how_much} elements we are rejecting null hipo")
        else:
            print(f"for {self.how_much} elements we are NOT rejecting null hip")



    def histogram_discreet(self):
        fig, axs = plt.subplots(1,2)
        axs = axs.flatten()
        
        # Creating density graph
        denisty_less_x = np.linspace (-1.5, -1, 100000)
        denisty_more_x = np.linspace (1, 1.5, 100000)
        density_less_y = np.linspace(0, 0, 100000)
        density_more_y = np.linspace(0, 0, 100000)
        
        
        density_x = np.linspace(-1, 1, 100000)
        denisty_y = np.linspace(1,1,100000)
        
        axs[1].plot(denisty_less_x, density_less_y,color = "blue")
        axs[1].plot(density_x, denisty_y, color = "blue")
        axs[1].plot(denisty_more_x, density_more_y, color = "blue")
        axs[1].grid(True)
        axs[1].set_ylim(0, 1.5)
        axs[1].set_xlabel("value")
        axs[1].set_ylabel("frequency")
        axs[1].set_title("Density function")

        # Plotting histogram
        a = np.hstack(self.stats)
        axs[0].set_title(f"amount of elements:{self.how_much}")
        axs[0].hist(a, align="left", edgecolor="black")
        axs[0].set_xlabel("value")
        axs[0].set_ylabel("frequency")
        axs[0].set_xlim(-2,2)
        plt.show()
        
    

object_15 = Object(15, 14684, 29655, 29241, 2)
object_120 = Object(1200, 14684, 29655, 29241, 2)

object_15.Simulate()
object_120.Simulate()
print("mean, sd")
print(object_15.CalculateMeanAndSD())
print(object_120.CalculateMeanAndSD())
print()
print("kurtozja")
print(object_15.CalculateKurtosis())
print(object_120.CalculateKurtosis())
print()
print("Median")
print(object_15.CalculateMedian())
print(object_120.CalculateMedian())
print()
print("skosnosc")
print(object_15.CalculateSkewness())
print(object_120.CalculateSkewness())
print()
print("mode")
print(object_15.CalculateMode())
print(object_120.CalculateMode())
print()
print("variance")
print(object_15.CalculateVariance())
print(object_120.CalculateVariance())
object_15.histogram_discreet()
object_120.histogram_discreet()
średnich_5000 = []
for _ in range(int(50000/2)):
    nowy_obj = Object(1000,14684, 29655, 29241, int(time.time()))
    nowy_obj.Simulate()
    
    srednia, sd = nowy_obj.CalculateMeanAndSD()
    średnich_5000.append(srednia)



plt.hist(średnich_5000,bins= 1000)
plt.show()
object_15.CheckIfRelevant(2.144)
object_120.CheckIfRelevant(1.96)
