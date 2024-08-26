# Author : Suraj Powar
# Date: 05/18/2023

import numpy as np
import sympy as smp
from sympy import *
from math import *
import scipy
from scipy.integrate import quad
from math import *

def integration():
    f = input("Enter the function you wish to integrate: ")
    f2 = input("Do you have upper and lower limit for the function? (Type y/n):").lower()
    if f2 == "y":
        b = input("Enter the upper limits: ")
        a = input("Enter the lower limits: ")
        x = smp.Symbol('x')
        return smp.integrate(f, (x, a, b))
    else:
        x = smp.Symbol('x')
        return smp.integrate(f, x)
    
    
if __name__ == "__main__":  
    print("The integration of the function you entered is: ", integration())
