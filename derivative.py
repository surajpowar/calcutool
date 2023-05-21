import sympy as sym
from sympy import *
import matplotlib.pyplot as plt
import numpy as np
import math

x = symbols("x")

fx = input("Please enter the function you wish to evaluate: ")

fprimex = diff(fx, x)


def newtons(x):
    h = fx / fprimex
    while abs(h) >= 0.000001:
        h = fx/fprimex
        x = x - h
        print(x)
     
    print("The value of the root is : ", "%.4f"% x)
    x_plot = np.linspace(-2, 2, 1000)
    y_plot = fx_plot
 

    fig = plt.figure()
    plt.plot(x_plot, y_plot, c="blue")
    plt.plot(fx, fprimex, c="red", marker="o", fillstyle="none")
    plt.xlim([-5, 5])
    plt.ylim([-15, 15])
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Newton's Method")
    plt.grid()
    plt.show()


 
if __name__ == "__main__":
    x_0 = -20 
    newtons(x_0)
