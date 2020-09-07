# -*- coding: utf-8 -*-
"""
Implemente um programa em Python que execute a equacao do driagrama de blocos do eco:
    y[n] = a0.x[n] + a1.x[n-n1] + a2.x[n=n2]
    
@author: lucas
"""
import numpy as np
import matplotlib.pyplot as plt

with open ('alo.pcm', 'rb') as f:   # Le o arquivo em binario
    buf = f.read ()
    data = np.frombuffer (buf, dtype = 'int16') # Dado é inteiro de 16 bits
    L = data [:: 2]     # Canal de audio esquerdo
    R = data [1 :: 2]   # Canal de audio direito

Fs = 8000 
t1 = 1.0 * 10**-3 
t2 = 1.5 * 10**-3
n = [int(t1 * Fs), int(t2 * Fs), 0] # atrasos de 10ms e 15ms

# Ganhos
a = [.5, .3, .2]
delay_length = n[2]
vector_delay = np.zeros(len(data), dtype = "int16");

# Entradas
result = np.copy(data)

for i in range(len(a)):
    for j in range(len(data)):
        vector_delay[j] = a[i] * data[j]
        
        np.concatenate([result, np.zeros(n[i], dtype = "int16")])
        
    result = np.concatenate([result, vector_delay])

plt.figure("Amostras de eco", figsize=(15,8))

plt.subplot(211)
plt.title("Entrada")
plt.xlabel("Nº de amostras")
plt.ylabel("Amplitude")
plt.grid(1)
plt.plot(data, color='green')

plt.subplot(212)
plt.title("Saída")
plt.xlabel("Nº de amostras")
plt.ylabel("Amplitude")
plt.grid(1)
plt.plot(result, color='red')

plt.tight_layout()
plt.show()

with open("eco_result.pcm", "wb") as new_file:
    for x in result:
        new_file.write(x)
    new_file.close()
