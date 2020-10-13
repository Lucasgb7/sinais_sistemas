# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 15:36:19 2020

@author: lucas
"""
import matplotlib.pyplot as plt
import numpy as np

# Sinal analogico
Dt = 1/64
t = np.arange(-50*Dt, 50*Dt, Dt)

# Plota o sinal analógico
f = 60
xa = np.cos(2*np.pi*f*t)


# Sinal discreto
Fs = 1000
Ts = 1/Fs
n = np.arange(-50, 50, 1)
xd = np.cos(2*np.pi*n*f/Fs)

fig = plt.figure(1)

a = fig.add_subplot(2, 1, 1)
a.plot(t, xa)
a.set_xlabel("(a)")

a = fig.add_subplot(2, 1, 2)
a.stem(t, xd, "k-", "ko", "k-")
a.set_xlabel("(b)")

plt.show()