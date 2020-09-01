# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 15:36:19 2020

@author: lucas
"""
import matplotlib.pyplot as plt
import numpy as np

# Sinal analogico
dT = 5*10**(-5)
t = np.arange(-dT, dT, dT)
f = 400
xA = np.cos(2*np.pi*f*t)

plt.plot(t*1000, xA)
plt.grid(True)
plt.ylabel('xA(t)')
plt.xlabel('Tempo (ms)')
plt.title('Sinal de freq. = ' + str(f) + 'Hz')
plt.show()
