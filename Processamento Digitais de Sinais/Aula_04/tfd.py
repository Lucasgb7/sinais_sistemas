# -*- coding: utf-8 -*-
"""
Transformada de Fourier Discreta
Calcule e plote a magnitude e fase da TFD do sinal.
@author: lucas
"""
import numpy as np
import matplotlib.pyplot as plt

a = 0.5
w = np.arange(-1*np.pi, 1*np.pi, np.pi/100) # -pi : pi/100 : pi

num = 1
den = 1 - a * np.exp(-1j*w) # (complex(0, -1)*w) # 1-a^(-j*w) 
x = num/den

mod_x = np.absolute(x)
fase_x = np.angle(den)

plt.plot(mod_x)
plt.title('Modulo de X')
plt.xlabel('w')
plt.grid(True)

plt.plot(fase_x)
plt.title('Fase de X')
plt.xlabel('w')
plt.grid(True)

plt.show()