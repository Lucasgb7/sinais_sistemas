import numpy as np
import matplotlib.pyplot as pl
from scipy.integrate import quad

def integral_a0(x, a, b):
    return a*x**2 + b

def integral_a0_2(x, a, b):
    return a

t = np.arange(-5, 5, 0.1)
t0 = 3
w0 = (2 * np.pi)/t0
a0 = (1/t0)*(quad(integrand, -2, -1, args=(a=2, b=0)) + quad(integra_a0, -1, 1, args=(a=2, b=0)))

