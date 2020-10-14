import numpy as np
import pandas as pd
from scipy import signal
import matplotlib.pyplot as plt
def sine_generator(fs, sinefreq, t):
    T = t
    nsamples = fs * T
    w = 2. * np.pi * sinefreq
    t_sine = np.linspace(0, T, nsamples, endpoint=False)
    y_sine = np.sin(w * t_sine)
    result = pd.DataFrame({ 
        'data' : y_sine} ,index=t_sine)
    return result

def butter_highpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = signal.butter(order, normal_cutoff, btype='high', analog=False)
    return b, a

def butter_highpass_filter(data, cutoff, fs, order=5):
    b, a = butter_highpass(cutoff, fs, order=order)
    y = signal.filtfilt(b, a, data)
    return y

with open('C:\\Users\\lucas\\Desenvolvimento\\sinais_sistemas\\Processamento Digitais de Sinais\\Aula_07\\Sweep10_3600.pcm', 'rb') as f:
    buf = f.read()
    data_i = np.frombuffer(buf, dtype='int16')
    data_len = len(data_i)


Fs = 8000
Fc = 1000
t = np.arange(0, data_len/Fs, 1 / Fs)
filtered_sine = butter_highpass_filter(data_i, Fc, Fs)

plt.figure(figsize=(20,10))
plt.subplot(211)
plt.plot(t, data_i[: len(t)])
plt.title('Sinal de entrada')
plt.subplot(212)
plt.plot(range(len(filtered_sine)),filtered_sine)
plt.title('Sinal de saída')
plt.show()

file_name = "C:\\Users\\lucas\\Desenvolvimento\\sinais_sistemas\\Processamento Digitais de Sinais\\Aula_07\\passaAlta_output.pcm"
with open(file_name, 'wb') as f:
    for d in filtered_sine:
        f.write(d)