# This script will be used when you choose to take a derivative of a function.

import numpy as np
import sympy as smp
from sympy import *
from math import *

def derivative():
    f = input("Enter the function you wish to take a derivative of: ")
    x = symbols('x')
    fprime = diff(f, x)
    return fprime
    
    
if __name__ == "__main__":  
    print("The derivative of the function you entered is: ", derivative())
