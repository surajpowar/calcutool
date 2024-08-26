# Author : Suraj Powar
# Date: 05/18/2023

import numpy as np
import sympy as smp
from sympy import *
import scipy
from scipy.integrate import quads
from math import *
import subprocess 
from subprocess import call 
from subprocess import Popen
from integration import integration as main1
from derivative import derivative as main2

def run(runfile):
  with open(runfile,"r") as rnf:
    exec(rnf.read())

input1 = input("Do you wish to integrate a function or derivate? [Type integrate or derivate]: ").lower()
if input1 == "integrate":
    run("integration.py")
elif input1 == "derivate":
    run("derivative.py")
else:
    print("Please type either integrate or derivate for using the package.")