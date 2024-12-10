import numpy as np
import math

step = 0.01
starting_point = 0
epsilon = 0.001
r = 10

document = open("output.txt", "w")


document.write("\documentclass[a4paper,12pt]{article}\n\n\\usepackage{amsmath}\n\n\\begin{document}\n\n\section*{Iteracja $n$}\n\n\subsection*{Funkcja kary gradient}")

document.write("")
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
        p += r * max(0, x - 2)
    if (max(0,-x-2)) != 0:
        p += r * (max(0, -x - 2))
    return p

def Finall_func(x):
    document.write("funkcja kary gradient")

    if (max(0, x-2) != 0 and max(0,-x-2) == 0):
        document.write("Aktywne: $x-2$")
        document.write("\[")
        document.write(f"3 \cdot {x:.5f}^2 - 9 + 2 \cdot {r} \cdot ({x:.5f} - 2) = ")
        document.write("\]")


        document.write("\[")
        document.write(f"3 \cdot {(x*x):.5f} - 9 + {2*r} \cdot {(x-2):.5f} = ")
        document.write("\]")

        document.write("\[")
        document.write(f"{(3*x*x):.5f} - 9 + {(2*r*(x-2)):.5f} =")
        document.write("\]")


        document.write("\[")
        document.write(f"{((x*x)-9+2*r*(x-2)):.5f}")
        document.write("\]")


    elif (max(0,-x-2) != 0 and max(0,x-2) == 0):
        document.write("Aktywne: $-x-2$")
        document.write("\[")
        document.write(f"3 \cdot {x:.5f}^2 - 9 + 2 \cdot {r} \cdot ({-1 * x:.5f} - 2) = ")
        document.write("\]")

        document.write("\[")
        document.write(f"3 \cdot {(x*x):.5f} - 9 + {2*r} \cdot {(-1 * x-2):.5f} =")
        document.write("\]")



        document.write("\[")
        document.write(f"{(3*(x*x)):.5f} - 9 + {(2*r*(-1 * x-2))} = {(3*(x*x)-9+2*r*(-1 * x-2)):.5f}")
        document.write("\]")
    elif (max(0,-x-2) != 0 and max(0,x-2) != 0):
        document.write("active: x-2 and -x-2 <--- cba writing it wont happen")
    else:
        document.write("Nie ma ograniczeń")
        document.write("\[")
        document.write(f"3 \cdot {x:.5f}^2 - 9 =")
        document.write("\]")

        document.write("\[")
        document.write(f"3 \cdot {(x*x):.5f} - 9 = {(3*(x*x) - 9):.5f}")
        document.write("\]")
    return gradient_func(x) + 2 * func_kara(x, r)



def validate(x1, x2):
    document.write("\n")
    document.write("\subsection*{Walidacja:}")
    document.write("\[")
    document.write(f"({x1:.5f} - {x2:.5f})^2 + ({func(x1):.5f} - {func(x2):.5f})^2")
    document.write("\]")

    document.write("\[")
    document.write(f"({(x1 - x2):.5f})^2 + ({(func(x1) - func(x2)):.5f})^2")
    document.write("\]")

    document.write("\n")
    return math.sqrt((x1 - x2)*(x1 - x2) + (func(x1) - func(x2)) * (func(x1) - func(x2)))

point = starting_point
for i in range(0, 1000):
    document.write(f"\section*{{Iteracja numer: ${i}$}}")
    gradient_func_val = Finall_func(point)

    document.write("\[")
    document.write(f"{{F(X)}} \leftarrow \\text {{Wartosc gradientu dla x{i}: }}{gradient_func_val}")
    document.write("\]")
    next_point = point - step * gradient_func_val
    document.write("\[")
    document.write(f"{{next point: x{i + 1}}} = {point} - {step}({gradient_func_val}) = {next_point}")
    document.write("\]")
    check_value = validate(point, next_point)
    document.write(f"\\text{{Wartosc bledu:  {check_value:.5f}}}")
    if check_value < epsilon:
        document.write("finished")
        document.write(f"for point {point} and min value = {func(point)}")
        document.write("\end{document}")
        break
    else:
        point = next_point

    document.write("\n"*3)