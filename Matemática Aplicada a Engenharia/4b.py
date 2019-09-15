import numpy as np
import matplotlib.pyplot as plt

def plotGraphic(eixoy, var, x, y):
	var.set_ylabel(eixoy)
	var.set_title(eixoy)
	var.plot(x, y)
	var.grid()

w = np.arange(-5, 5, 0.1)
a = 5
b = 3
z = a * (1j*w) / (b + 1j*w)
modulo = abs(z)
angulo = np.arctan(z.imag/z.real)
fig, ax = plt.subplots(2)

plotGraphic('Magnitude', ax[0], w, modulo)
plotGraphic('Fase', ax[1], w, angulo)
plt.subplots_adjust(hspace=0.5)
plt.show()