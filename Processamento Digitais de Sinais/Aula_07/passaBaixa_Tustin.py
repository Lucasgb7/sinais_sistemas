from scipy.signal import freqz, TransferFunction, bode, cont2discrete
import scipy.signal as signal
import numpy as np
from numpy import pi, sin, log10, zeros
from matplotlib.pyplot import plot, subplot, xlabel, ylabel, title, grid, axis, figure, show
"""
Exemplo de filtro passa baixa utilizando Tustin
            a
H(s) = -----------
         (s + a)
S -> Z
H[Z] = Y[Z] / X[Z]
"""
W0 = 2*pi*1000
f0 = W0/(2*pi)  # F0 em HZ

# w0 = 2*pi*f0;

# Definindo os coeficientes
num = [W0, 0]
den = [W0, 1]
H = TransferFunction(num, den)
print(type(H))
bode(H)

Fs = 8000
Ts = 1/Fs

# Transforma de continuo para discreto, utilizando metodo de Tustin
Hd = cont2discrete(H, Ts, 'bilinear')

# Plotar em frequencia (Hz)
[H, w] = freqz(Hd.Numerator[0, 0], Hd.Denominator[0, 0], fs=Fs/(2*pi))

figure(2)
plot(w, 20*log10(abs(H)))
grid()