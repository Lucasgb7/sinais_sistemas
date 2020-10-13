import numpy as np
import matplotlib.pyplot as plt
from matplotlib import patches
from matplotlib.pyplot import axvline, axhline
from collections import defaultdict
from plot_zplane import zplane

# N = [1, 1.5, 2]
# D = [1, 0, 0]
# N = [1, 0.6]
# D = [1, 0.6, 0.2]
N = np.array([1, 0.8])
D = np.array([1, 1, 0.41])

zeros = np.roots(N)
poles = np.roots(D)

print(zeros)
print(poles)

zplane(N, D)