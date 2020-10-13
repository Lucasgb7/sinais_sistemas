import numpy as np
from plot_zplane import zplane
"""
        Z^2 + 1.5Z + 2
D(Z) =  --------------
             Z^2
"""
if __name__ == "__main__":
    num = np.array([1, 1.5, 2])
    dem = np.array([1, 0, 0])

    zplane(num, dem)