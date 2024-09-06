# Author : Suraj Powar
# Date: 05/18/2023

import numpy as np
import sympy as smp
from sympy import *
from math import *
import scipy
from scipy.integrate import quad

def derivative(f_str):
    """
    Computes the derivative of a given function f with respect to x.
    
    Parameters:
        f_str (str): Function to differentiate in string format (e.g., 'x**2 + 2*x').
    
    Returns:
        sympy expression: Derivative of the function.
    """
    x = smp.Symbol('x')
    f = smp.sympify(f_str)
    fprime = smp.diff(f, x)
    
    return fprime
    
    
if __name__ == "__main__":  
    print("The derivative of the function you entered is: ", derivative())
