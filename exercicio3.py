# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

def u(tempo):
    array = []
    for x in tempo:
        if x >= 0.0:
            array.append(1)
        else:
            array.append(0)
    return array

t = np.arange(-4, 4.1, 0.1)
plt.figure('Exercicio 3')

# Função Original F(t)
f1 = (((2 * (t+2) * u(t+2)) - (2*(t+1) * u(t+1)))
    -(((2 * (t+2) * u(t+2)) - (2*(t+1) * u(t+1)))*u(t-1)))+((2 * np.e ** -(t - 1)) * u(t - 1))
plt.subplot(221)
plt.ylabel('f(t)')
plt.xlabel('t')
plt.title('Função Original F(t)')
plt.plot(t, f1)
plt.grid(True)

# Função Inversa F(-t)
f2 = (((2 * (-t+2) * u(-t+2)) - (2*(-t+1) * u(-t+1)))
    -(((2 * (-t+2) * u(-t+2)) - (2*(-t+1) * u(-t+1)))
    *u(-t-1))) + ((2 * np.e ** -(-t - 1)) * u(-t - 1))
plt.subplot(222)
plt.ylabel('f(t)')
plt.xlabel('t')
plt.title('Função Inversa F(-t)')
plt.plot(t, f2)
plt.grid(True)

# Função Par
f3 = 0.5*(f1+f2)
plt.subplot(223)
plt.ylabel('f(t)')
plt.xlabel('t')
plt.title('Função Par')
plt.plot(t, f3)
plt.grid(True)

# Função Impar
f4 = 0.5*(f1-f2)
plt.subplot(224)
plt.ylabel('f(t)')
plt.xlabel('t')
plt.title('Função Impar')
plt.plot(t, f4)
plt.grid(True)

plt.subplots_adjust(hspace=.5)
plt.show()