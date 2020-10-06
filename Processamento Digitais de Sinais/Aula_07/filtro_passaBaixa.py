import numpy as np
import matplotlib.pyplot as plt
import scipy as sc
from scipy import signal
import math

if __name__ == "__main__":
    R = 10
    C = 10*10**-6
    w0 = 2*np.pi*1000
    f0 = w0/(2*np.pi)

    num = [1, 3, 3]
    den = [1, 2, 1]
    H = signal.TransferFunction(num, den)
    H_Bode = signal.bode(H)

    # Aplicando a Transformacao Bilinier (S -> Z)
    Fs = 8000
    Ts = 1 / Fs
    Hd = signal.cont2discrete(H, Ts, method='bilinear') # Metodo de Trustin
    #[H, w] = signal.freqz(sc.fraction)