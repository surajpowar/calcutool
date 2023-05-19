# Author : Suraj Powar
# Date: 05/18/2023

import numpy as np
import sympy as smp
from sympy import *
import scipy
from scipy.integrate import quad
from math import *

question = input("Do you want to take a derivative or integrate a function (press d for derivative or i for integration): ")

if question == str("d"):
    f = input("Enter the function you wish to take a derivative of: ")
    x = symbols('x')
    fprime = diff(f, x)
    print("The derivative of the function you entered is: ",fprime)
else:
    p = input("Enter the function you wish to integrate: ")
    b = input("Enter upper bound: ")
    a = input("Enter lower bound: ")
    i = quad(p, a, b)
    print("The integration value is: ", i)

