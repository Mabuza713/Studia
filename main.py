import numpy as np
import math

step = 0.01
starting_point = 3
epsilon = 0.001
r = 10

def func(x):
    return x * (x + 3) * (x - 3)


def constraint1(x):
    return -x - 2

def constraint2(x):
    return x - 2


def gradient_func(x):
    return 3*x*x-9

def func_kara(x, r):
    p = 0
    if (max(0, x-2)) != 0:
        p += 2 * r * max(0, x - 2)
    if (max(0,-x-2)) != 0:
        p += 2 * r * (max(0, -x - 2))
    return p

def Finall_func(x):
    print("funkcja kary gradient")

    if (max(0, x-2) != 0 and max(0,-x-2) == 0):
        print("active: x-2")
        print(f"3 * {x}^2 - 9 + 2 * {r} * ({x} - 2) = 3 * {x*x} - 9 + {2*r} * {x-2} = {3*x*x} - 9 + {2*r*(x-2)} = {3*x*x-9+2*r*(x-2)}")
    elif (max(0,-x-2) != 0 and max(0,x-2) == 0):
        print("active: -x-2")
        print(f"3 * {x}^2 - 9 + 2 * {r} * ({-1 * x} - 2) = 3 * {x*x} - 9 + {2*r} * {-1 * x-2} = {3*x*x} - 9 + {2*r*(-1 * x-2)} = {3*x*x-9+2*r*(-1 * x-2)}")
    elif (max(0,-x-2) != 0 and max(0,x-2) != 0):
        print("active: x-2 and -x-2 <--- cba writing it wont happen")
    else:
        print(f"3 * {x}^2 - 9 = 3 * {x*x} - 9 = {3*x*x - 9}")

    print("\n")
    return gradient_func(x) + 2 * func_kara(x, r)



def validate(x1, x2):
    return math.sqrt((x1 - x2)*(x1 - x2) + (func(x1) - func(x2)) * (func(x1) - func(x2)))

point = starting_point
for i in range(0, 100):
    print(f"iteration nr{i}")
    gradient_func_val = Finall_func(point)
    print(f"F(X) <-gradient func value for x{i}: {gradient_func_val}")

    print(f"next point: x{i + 1} = {point} - {step}({gradient_func_val}) = {point - step * gradient_func_val}")
    next_point = point - step * gradient_func_val

    check_value = validate(point, next_point)
    if check_value < epsilon:
        print("finished")
        print(f"for point {point} and min value = {func(point)}")
        break
    else:
        print(f"next point = {next_point}")
        point = next_point

    print("\n"*3)