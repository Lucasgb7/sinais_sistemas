from scipy import signal
from scipy import linspace
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

exercicio = 5
print ("Exercicio " + str(exercicio) + "-")
capacitor = 0.000001
resistor = 10000.0
indutor = 0.1
il = 24000.0
k = 2.0

# 1
if (exercicio == 1):
    numerador = np.poly1d([k, 0], variable='s')
    denominador = np.poly1d([1, 1/(resistor*capacitor)], variable='s')

# 2
if (exercicio == 2):
    numerador = np.poly1d([k/(capacitor*indutor)], variable='s')
    denominador = np.poly1d([1, resistor/indutor, 1/(capacitor*indutor)], variable='s')

# 3
if (exercicio == 3):
    numerador = np.poly1d([k], variable='s')
    denominador = np.poly1d([1/(indutor/capacitor), indutor/resistor, 1], variable='s')

if (exercicio == 4):
    numerador = np.poly1d([1], variable='s')
    denominador = np.poly1d([resistor*resistor*capacitor*capacitor, 
                (resistor*capacitor+resistor*capacitor+resistor*capacitor), 1], variable='s')
# 5
if (exercicio == 5):
    numerador =  np.poly1d([il/(indutor*capacitor)])
    denominador = np.poly1d([1, 1/(resistor*capacitor), 1/(indutor*capacitor)])

print ("Numerador: {}".format(numerador))
print ("Denominador: {}".format(denominador))

hs = signal.TransferFunction(numerador, denominador) # H(s) = Vo(s)/Vi(s)
zeros, polos, k = signal.tf2zpk(numerador, denominador) # Zeros, polos e ganho

print ("--/--/--")
print ("H(s)=", hs)
print ("Polos=", polos)
print ("Zeros=", zeros)
print ("Ganho=", k)
print ("--/--/--")

# Polos e Zeros
fig, ax = plt.subplots()
plt.title('Polos e Zeros')
ax.scatter(p.real, p.imag)
t1 = plt.plot(p.real, p.imag, 'rx', ms=100)
plt.setp( t1, markersize=10.0, markeredgewidth=1.0, markeredgecolor='k', markerfacecolor='g')
t2 = plt.plot(z.real, z.imag, 'go', ms=10)
plt.setp( t2, markersize=12.0, markeredgewidth=3.0, markeredgecolor='r', markerfacecolor='r')
ax.grid()


# # Resposta em f(t)
# t, s = signal.step(hs)
# plt.figure()
# plt.title('Resposta em f(t)')
# plt.plot(t, s, 'k-')


# Resposta em frequência
w, h = signal.freqresp(hs)
plt.figure()
plt.title('Resposta em frequencia')
plt.plot(w, h)

### Diagramas de Bode
## Resposta em F(jw)
# Módulo
w, mag, phase = signal.bode(hs)
plt.figure()
plt.semilogx(w, mag)
plt.title('Diagrama de Bode')
plt.xlabel('Frequencia (Hz)')
plt.ylabel('Magnitude (dB)')

# Fase
plt.figure()
plt.semilogx(w, phase)
plt.title('Diagrama de Bode')
plt.xlabel('Frequencia (Hz)')
plt.ylabel('Fase (grau)')
plt.show()