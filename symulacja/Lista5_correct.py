import random
import matplotlib.pyplot as plt
import numpy as np
from numpy import sqrt, log, sin, cos, pi
import scipy.stats as stats
import time
random.seed(3)

from Lista4 import Object as Object_lista4
from Lista3 import Object as Object_lista3


class Object:
    def __init__(self,how_much,mean, sd):
        self.how_much = how_much
        self.stats = []
        self.mean = mean
        self.sd = sd
        
    def Simulate(self):
        u1_obj = Object_lista4(self.how_much//2, 1103515245, 12345, 2**31,  abs(int(time.perf_counter()) * 10000000000000000000))
        u2_obj = Object_lista4(self.how_much//2, 1103515245, 12345, 2**31, abs(int(time.perf_counter()) * 10000000000000000000)+ abs(int(time.perf_counter()) * 10000000000000000000) - 44)
        
        u1_obj.Simulate()
        u2_obj.Simulate()
        for i in range(self.how_much // 2):

            
            # Generate two uniform random numbers
            u1 = u1_obj.stats_sim_vals[i] / 2147483648
            u2 = u2_obj.stats_sim_vals[i] / 2147483648
            #u1 = np.random.uniform()
            #u2 = np.random.uniform()
            z1 = sqrt(-2 * log(u1)) * cos(2 * pi * u2)
            z2 = sqrt(-2 * log(u1)) * sin(2 * pi * u2)
            
            self.stats.append(self.mean + self.sd * z1)
            self.stats.append(self.mean + self.sd * z2)
    
    def CalculateMeanAndSD(self, verbose=False):
        mean_temp = 0
        sd_temp = 0

        for i in range(0, len(self.stats)):
            mean_temp += self.stats[i]

        mean = mean_temp / len(self.stats)

        for i in range(0, len(self.stats)):
            sd_temp += (self.stats[i] - mean) ** 2

        sd = sqrt(sd_temp / (len(self.stats) - 1))
        if verbose:
            print(f"mean: {mean}")
            print(f"sd: {sd}")
            
            #print(f"sd {np.std(self.stats)}")
            #print(f"mean {np.mean(self.stats)}")

        return mean, sd
    
    def CalculateMedian(self):
        lista = self.stats
        lista.sort()
        print(f"median {np.median(lista)}")
        if (len(self.stats) % 2 == 0):
            return ((lista[len(self.stats) // 2]) + (lista[len(self.stats) // 2 - 1]))/2
        else:
            return (lista[len(self.stats) // 2])
        
    def CalculateVariance(self):
        mean, sd = self.CalculateMeanAndSD()
        print(f"variance {np.var(self.stats)}")
        return sd*sd
    
    def CalculateSkewness(self):
        mean, sd = self.CalculateMeanAndSD()
        skewness_temp = 0
        for i in range(0, len(self.stats)):
            skewness_temp += ((self.stats[i] - mean) / sd) ** 3
        skewness = skewness_temp * len(self.stats) / (len(self.stats) - 1) / (len(self.stats) - 2) 
        print(stats.skew(self.stats, bias= False))
        return skewness

    def CalculateKurtosis(self):
        first = len(self.stats) * (len(self.stats) + 1) / (len(self.stats) - 1) / (len(self.stats) - 2) / (len(self.stats) - 3)
        mean, sd = self.CalculateMeanAndSD()

        temp = 0
        for i in range(0, len(self.stats)):
            temp += ((self.stats[i] - mean) / sd) ** 4

        second = 3 * (len(self.stats) - 1) * (len(self.stats) - 1) / (len(self.stats) - 2) / (len(self.stats) - 3)
        
        print(f"kurtoza {stats.kurtosis(self.stats)}" )
        return first * temp - second
    
    def CalculateMode(self):
        if (len(self.stats) + 1 == len(set(self.stats))):
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
                return "no mode"
            
    def CalculatePercentile(self, percentile):
        lista = self.stats
        lista.sort()

        index = (len(self.stats) - 1) * percentile / 100
        if (index - int(index) == 0):
            return lista[int(index)]
        
        lower = int(np.floor(index))
        upper = int(np.ceil(index))
        interpolation = index - lower
        
        return (1 - interpolation) * lista[lower] + interpolation * lista[upper]
        
        
    def qq_plot(self):
        sorted_list = sorted(self.stats)
        stats.probplot(sorted_list, dist="norm", plot=plt)
        plt.title(f"qq-plot for {len(self.stats)} elements")
        plt.show()
    
    def boxplot(self):
        sorted_list = sorted(self.stats)
        plt.boxplot(sorted_list)
        plt.title(f"boxplot for {len(self.stats)} elements")
        plt.show()
        
    def CheckIfRelevant(self, critical_value):
        mean, sd = self.CalculateMeanAndSD(False)
        value = sqrt(len(self.stats)) * (mean -0.5) / sd
        
        if (abs(value) > critical_value):
            print(f"for {len(self.stats)} elements we are rejecting null hipo")
        else:
            print(f"for {len(self.stats)} elements we are NOT rejecting null hip")
            
    def histogram_discreet(self):
        fig, axs = plt.subplots(2,2)
        axs = axs.flatten()
        
        dane_list_3 = Object_lista3(self.how_much)
        dane_list_3.Simulate()
        
        # Creating density graph
        density_x = np.linspace(-2, 3, 100000)
        denisty_y = stats.norm.pdf(density_x, 0.5,0.5)
        

        axs[1].plot(density_x, denisty_y, color = "blue")
        axs[1].grid(True)
        axs[1].set_ylim(0, 1.5)
        axs[1].set_xlabel("value")
        axs[1].set_ylabel("frequency")
        axs[1].set_title("Density function")
        axs[1].set_xlim(-2,3)
        
        # Plotting histogram
        a = np.hstack(self.stats)
        axs[0].set_title(f"amount of elements:{len(self.stats)} using Box-Muller")
        axs[0].hist(a, align="left", edgecolor="black")
        axs[0].set_xlabel("value")
        axs[0].set_ylabel("frequency")
        axs[0].set_xlim(-2.5,2.5)
        
                # Creating density graph
        density_x = np.linspace(-2, 3, 100000)
        denisty_y = stats.norm.pdf(density_x, 0.5,0.5)
        

        axs[3].plot(density_x, denisty_y, color = "blue")
        axs[3].grid(True)
        axs[3].set_ylim(0, 1.5)
        axs[3].set_xlabel("value")
        axs[3].set_ylabel("frequency")
        axs[3].set_title("Density function")
        axs[3].set_xlim(-2,3)
        
        
        # Plotting histogram
        a = np.hstack(dane_list_3.stats)
        axs[2].set_title(f"amount of elements:{len(self.stats)} using numpy")
        axs[2].hist(a, align="left", edgecolor="black")
        axs[2].set_xlabel("value")
        axs[2].set_ylabel("frequency")
        axs[2].set_xlim(-2.5,2.5)
        
        plt.show()
        
object_15 = Object(20, 0.5, 0.5)
object_120 = Object(100, 0.5, 0.5)

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

object_15.CheckIfRelevant(1.96)
object_120.CheckIfRelevant(1.96)

object_15.histogram_discreet()
object_120.histogram_discreet()


print("\n\n\n\nshapiro willk")
def ShapiroWilk(amount_of_samples, amount_of_elemetns):
    list_sorted = []
    for _ in range(amount_of_samples):
        time.sleep(1)
        temp_obj = Object(amount_of_elemetns, 0.5, 0.5)
        temp_obj.Simulate()
        mean, sd = temp_obj.CalculateMeanAndSD()
        list_sorted.append(mean)
    list_sorted = sorted(list_sorted)
    W, p = stats.shapiro(list_sorted)
    print(f"wartość testu shapiro: {W} z p-value: {p}")
    return W, p
#
#hapiroWilk(250,20)
#hapiroWilk(250,100)



def CheckIfRelevant(lista1, lista2, critical_value, stat_from_list_2):
    mean1 = np.mean(lista1)
    sd1 = np.std(lista1, ddof=1)
    
    mean2 = np.mean(lista2)
    sd2 = np.std(lista2)

    value = (mean1 - mean2) / np.sqrt((sd1 ** 2 / len(lista1)) + (sd2 ** 2 / len(lista2)))
    if (abs(value) > critical_value):
        print(f"for {len(lista1)} elements we are rejecting null hipo")
    else:
        print(f"for {len(lista1)} elements we are NOT rejecting null hip")



list_sorted_mean = []
list_sorted_sd = []
list_sorted_kurtosis = []
list_sorted_skweness = []
list_sorted_variance = []


list2_sorted_mean = []
list2_sorted_sd = []
list2_sorted_kurtosis = []
list2_sorted_skweness = []
list2_sorted_variance = []
def CreateMeanMean(amount_of_samples, amount_of_elemetns):
    for _ in range(amount_of_samples):
        time.sleep(1)
        object_lista2 = Object_lista3(amount_of_elemetns)
        object_lista2.Simulate()
        temp_obj = Object(amount_of_elemetns, 0.5, 0.5)
        temp_obj.Simulate()
        
        mean, sd = temp_obj.CalculateMeanAndSD()
        kurtosis = temp_obj.CalculateKurtosis()
        skewness = temp_obj.CalculateSkewness()
        var = temp_obj.CalculateVariance()
        
        mean2, sd2 = object_lista2.CalculateMeanAndSD()
        kurtosis2 = object_lista2.CalculateKurtosis()
        skewness2 = object_lista2.CalculateSkewness()
        var2 = object_lista2.CalculateVariance()
        
        list2_sorted_kurtosis.append(kurtosis2)
        list2_sorted_skweness.append(skewness2)
        list2_sorted_variance.append(var2)
        list2_sorted_mean.append(mean2)
        list2_sorted_sd.append(sd2)
        
        list_sorted_kurtosis.append(kurtosis)
        list_sorted_skweness.append(skewness)
        list_sorted_variance.append(var)
        list_sorted_mean.append(mean)
        list_sorted_sd.append(sd)
    
    list_sorted_mean.sort()
    list_sorted_sd.sort()
    list_sorted_kurtosis.sort()
    list_sorted_skweness.sort()
    list_sorted_variance.sort()
    
CreateMeanMean(100, 100)
print()
print()
print()
print()
print()
print()

print("test for mean")
CheckIfRelevant(list_sorted_mean, list2_sorted_mean ,1.96, 0.06866020977708105)

print("test for sd")
CheckIfRelevant(list_sorted_sd, list2_sorted_sd,1.96, 0.5855700719712053)

print("test for kurt")
CheckIfRelevant(list_sorted_kurtosis, list2_sorted_kurtosis,1.96, -1.0533222257919426)

print("test for skew")
CheckIfRelevant(list_sorted_skweness, list2_sorted_skweness, 1.96, 0.00011500419053986119)

print("test for var")
CheckIfRelevant(list_sorted_variance,list2_sorted_variance, 1.96, 0.3428923091883625)
