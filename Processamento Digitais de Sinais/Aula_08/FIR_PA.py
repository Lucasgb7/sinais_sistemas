# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 08:39:08 2020

@author: lucas
"""
from pylab import *
from scipy.signal import freqz
import numpy as np
import matplotlib.pyplot as plt
"""
Exemplo – Transformação “s” -> “z”
• TAREFAS: Obter a função de transferencia H[z] do filtro passa-baixas.
• Plotar os pólos e zeros.
• Implementar um programa para executar a equação diferença do filtro.
• Validar essa implementação com um sinal de entrada de sweep.
"""
sample_rate = 8000
media_buf = np.zeros(2)
output = 0
Fc = 400
Fs = sample_rate

# Cálculo de Magnitude
wc = 2*np.pi*Fc

# F' (F_linha)
Fl = 2 * Fs

# Coeficientes para equação
a = wc/(Fl+wc)      #  0.282
b = (wc-Fl)/(Fl+wc) # -0.4361

print("Coeficiente A:", a)
print("Coeficiente B:", b)

# Leitura de arquivo
with open("C:\\Users\\lucas\\Desenvolvimento\\sinais_sistemas\\Processamento Digitais de Sinais\\Aula_08\\sweep_3800.pcm",'rb') as f:     # Sweep de 1 a 3.6KHz
    buf = f.read()
    data_i = np.frombuffer(buf, dtype='int16')
    data_len = len(data_i)

    # Arquivo cópia para salvar o resultado lido
    output_data = np.zeros_like(data_i)

    for i in range(data_len):
        media_buf[0] = data_i[i]

        m = (a * media_buf[0]) + (a * media_buf[1]) - (b * output)
        output = m
        output_data[i] = m
        media_buf[1:2] = media_buf[0:1]

# 100ms
t = np.arange(0, data_len/sample_rate, 1 / sample_rate)
output_data = data_i - output_data
figure(1)
plt.stem(t, data_i[: len(t)], "k-", "ko", "k-", label="Input")
plt.plot(t, output_data[: len(t)], label="Output")
plt.legend()
plt.title("Filtro passa-alta")
plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude")
plt.show()

figure(2)
num_mag = [Fl, -Fl]
den_mag = [Fl+wc, wc-Fl]
[w, h] = freqz(num_mag, den_mag, worN=Fs, fs=Fs)
plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude")
plt.title("Magnitude")
plot(w, 20*log10(abs(h)), 'r')

# Escreve resultado em outro arquivo .pcm
file_name = "output_PA.pcm"
with open(file_name, 'wb') as f:
    for d in output_data:
        f.write(d)
