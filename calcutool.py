# Author : Suraj Powar
# Date: 05/18/2023

import sympy as smp

def integration(f_str, a=None, b=None):
    # Convert the function string to a sympy expression
    x = smp.Symbol('x')
    f = smp.sympify(f_str)

    if a is not None and b is not None:
        # Definite integral
        result = smp.integrate(f, (x, a, b))
    else:
        # Indefinite integral
        result = smp.integrate(f, x)

    return result

def derivative(f_str):
    # Convert the function string to a sympy expression
    x = smp.Symbol('x')
    f = smp.sympify(f_str)

    # Compute the derivative
    fprime = smp.diff(f, x)
    return fprime

# Main script for user input
if __name__ == "__main__":
    action = input("Do you wish to integrate a function or differentiate? [Type integrate or differentiate]: ").lower()
    
    if action == "integrate":
        f_str = input("Enter the function you wish to integrate (e.g., x**2 + 2*x): ")
        has_limits = input("Do you have upper and lower limits for the function? (Type y/n): ").lower()
        if has_limits == "y":
            a = float(input("Enter the lower limit: "))
            b = float(input("Enter the upper limit: "))
            result = integration(f_str, a, b)
        else:
            result = integration(f_str)
        print(f"The result of the integration is: {result}")

    elif action == "differentiate":
        f_str = input("Enter the function you wish to differentiate (e.g., x**2 + 2*x): ")
        result = derivative(f_str)
        print(f"The derivative of the function is: {result}")

    else:
        print("Please type either 'integrate' or 'differentiate' to use the package.")
