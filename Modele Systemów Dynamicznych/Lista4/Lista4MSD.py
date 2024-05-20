import numpy as np
from sympy import Function, dsolve, Derivative, Rational
from sympy.abc import t
from scipy import *
from scipy.integrate import *
from math import *
from numpy import *
import matplotlib.pyplot as plt


class Pendulum:
    def SolveWithSympy(stringLength, initialTilt):
        y = Function("y")
        g = constants.g
        result = dsolve(Derivative(y(t),t ,t ) +  Rational(g)/stringLength * y(t), y(t), ics = {y(0): initialTilt, y(t).diff(t).subs(t, 0):0})
        return result

    def CreatingArrayOfValues(T,dt,name, stringLength, initialTilt):
        array = []
        eq = Pendulum.SolveWithSympy(stringLength, initialTilt)
        Tspan = []

        for i in range(0,int(T / dt)):
            i = i * dt

            Tspan.append(i)
            result = eq.evalf(subs = {t: i})
            array.append(result.rhs)
        # Pendulum.Plotting(Tspan, array,name),
        return array

    def SolveWithODEINT(stringLength, initialTilt, T, dt):
        def deriv(Y, t):
            g = constants.g
            return(Y[1], -g/stringLength*np.sin(Y[0]))


        time = linspace(0,T,int(T/dt))
        sol = odeint(deriv, [initialTilt, 0], time)
        # plt.plot(time, sol[:,0])
        # plt.grid(axis = "both")
        # plt.show()
        return sol[:,0]

    def Plotting(array, Tspan, name):
        fig , ax = plt.subplots()
        ax.plot(array, Tspan)
        ax.grid(axis = "both")
        ax.set_xlabel("Time")
        ax.set_ylabel("Angle")
        ax.set_title(name)
        plt.show()
    def plotingTwo(stringLength, initialTilt, T, dt, name = ""):
        OdeIntArr = Pendulum.SolveWithODEINT(stringLength, initialTilt, T, dt)
        SympyArr = Pendulum.CreatingArrayOfValues(T,dt ,name, stringLength, initialTilt)
        fig, axs = plt.subplots(1,2,figsize = (13,13))
        axs[0].plot(linspace(0,T,int(T/dt)), OdeIntArr)
        axs[1].plot(linspace(0,T,int(T/dt)), SympyArr)

        axs[0].set_title("pendulum deflection using ODEINT")
        axs[1].set_title("pendulum deflection using Sympy")
        axs[0].grid(axis = "both"); axs[1].grid(axis = "both")
        axs[0].set_xlabel("Time"); axs[1].set_xlabel("Time")
        axs[0].set_ylabel("Angle");axs[1].set_ylabel("Angle")

        plt.show()

    def ErrorPlots(stringLength, initialTilt, T, dt_values, name=""):
        mean_errors = []
        pow_errors = []

        for dt in dt_values:
            OdeIntArr = Pendulum.SolveWithODEINT(stringLength, initialTilt, T, dt)
            SympyArr = Pendulum.CreatingArrayOfValues(T, dt, name, stringLength, initialTilt)

            meanOde = np.mean(np.abs(np.array(OdeIntArr) - np.array(SympyArr)))
            PowError = np.mean((np.array(OdeIntArr) - np.array(SympyArr)) ** 2)

            mean_errors.append(meanOde)
            pow_errors.append(PowError)

        plt.figure(figsize=(12, 6))
        plt.plot(dt_values, mean_errors, label='Mean Absolute Error', marker='o')
        plt.plot(dt_values, pow_errors, label='Mean Squared Error', marker='x')
        plt.xlabel('dt')
        plt.ylabel('Error')

        plt.title('Error Analysis for Different dt Values')
        plt.legend()
        plt.grid(axis="both")
        plt.show()

        return mean_errors, pow_errors
print(constants.g)
# print(Pendulum.CreatingArrayOfValues(10,0.01, "RozwiazaniePrzySympy"))
# print(Pendulum.SolveWithODEINT(1, constants.pi/4, 10, 0.01))
# print(Pendulum.ErrorPlots(1, constants.pi/4, 10, dt_values = [0.01,0.05,0.1,0.5,1]))

Pendulum.plotingTwo(1, constants.pi/4, 10, 0.1)

print(constants.g)