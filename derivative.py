# Author : Suraj Powar
# Date: 05/18/2023

import numpy as np
import sympy as smp
from sympy import *
from math import *
import scipy
from scipy.integrate import quad

def derivative():
    f = input("Enter the function you wish to take a derivative of: ")
    x = symbols('x')
    fprime = diff(f, x)
    return fprime
    
    
if __name__ == "__main__":  
    print("The derivative of the function you entered is: ", derivative())
