from scipy.signal import freqz
import scipy.signal as signal
import numpy as np
from matplotlib.pyplot import plot, subplot, xlabel, ylabel, title, grid, axis, figure, show
"""
Obtenha a resposta em frequencia da
sequencia finita dada por: X[k] = {0,1; 0,2; 0,4; 0,2; 0,1}
"""
step = np.pi / 1000
w = np.arange(0, np.pi, step)
L = 8
Fs = 8000

num = np.sin(w * L / 2)
den = np.sin(w / 2)
temp = num/den

# Resposta em Radiano (RAD)
X = (1 / L) * (abs(temp))

subplot(3, 1, 1)
plot(w, X)
xlabel('Frequência')
title('Frequência (RAD)')
grid()

# Resposta em Hz
F_Hz = (w / np.pi) * (Fs / 2)
subplot(3, 1, 2)
plot(F_Hz, X)
xlabel('Frequência')
title('Frequência (HZ)')
grid()


# Resposta em Decibel (DB)
X_Db = 20 * np.log10(X)
subplot(3, 1, 3)
plot(F_Hz, X_Db)
ylabel('Atenuação (DB)')
xlabel('Frequência')
title('Frequência (HZ)')
grid()
axis([0, 4000, -70, 0]) # define os limites para plotagem

figure(2)

# Reposta em frequencia
num_ = np.zeros((1, L), dtype='float64')
num_[0, :] = 1 / L  # num = [.25 .25 .25 .25];
den_ = float(1)
[w, h] = freqz(num_.T, den_, worN=Fs, fs=Fs)
plot(w, 20 * np.log10(abs(h)), 'b')

title('Magnitude (FREQ)')
grid()
show()