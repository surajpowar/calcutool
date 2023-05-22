# This script will be used when you choose to integrate a function

import numpy as np
import sympy as smp
from sympy import *
from math import *
import scipy
from scipy.integrate import quad
from math import *

def integration():
    f = input("Enter the function you wish to integrate: ")
    x = smp.Symbol('x')
    return smp.integrate(f, x)
    
if __name__ == "__main__":  
    print("The integration of the function you entered is: ", integration())
