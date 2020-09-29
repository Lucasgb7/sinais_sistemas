import numpy as np
import matplotlib.pyplot as plt
from plot_zplane import zplane # biblioteca para plotar no plano Z

if __name__ == "__main__":
    num = [1, 1.5, 2]
    den = [1, 0, 0]

    z = np.roots(num)
    p = np.roots(den)

    zplane(p, z)