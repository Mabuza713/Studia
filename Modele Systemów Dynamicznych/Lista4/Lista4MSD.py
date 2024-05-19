import numpy as np
from sympy import Function, dsolve, Symbol,parse_expr, Derivative, simplify,  checkodesol, Rational, solve, N
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

    def CreatingArrayOfValues(T,dt,name):
        array = []
        eq = Pendulum.SolveWithSympy(1, constants.pi/4)
        Tspan = []

        for i in range(0,int(T / dt)):
            i = i * dt

            Tspan.append(i)
            result = eq.evalf(subs = {t: i})
            array.append(result.rhs)
        Pendulum.Plotting(Tspan, array,name),
        return array

    def SolveWithODEINT(stringLength, initialTilt, T, dt):
        def deriv(Y, t):
            g = constants.g
            return(Y[1], -g/stringLength*np.sin(Y[0]))


        time = linspace(0,T,int(T/dt))
        sol = odeint(deriv, [pi/4, 0], time)
        plt.plot(time, sol[:,0])
        plt.savefig("dasd.png")

    def Plotting(array, Tspan, name):
        fig , ax = plt.subplots()
        ax.plot(array, Tspan)
        ax.grid(axis = "both")
        ax.set_xlabel("Time")
        ax.set_ylabel("Angle")
        ax.set_title(name)
        fig.savefig(f"{name}.png")



# print(Pendulum.CreatingArrayOfValues(10,0.01, "RozwiazaniePrzySympy"))
print(Pendulum.SolveWithODEINT(1, constants.pi/4, 10, 1))


