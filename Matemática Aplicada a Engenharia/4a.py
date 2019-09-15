import numpy as np
import matplotlib.pyplot as plt

def plotGraphic(eixoy, var, x, y):
	var.set_ylabel(eixoy)
	var.set_xlabel('W')
	var.set_title(eixoy)
	var.plot(x, y,)
	var.grid()

w = np.arange(-5, 5, 0.1) 
a = 3
z = (a) / (a + 1j*w)
angulo = np.arctan(z.imag/z.real)
modulo = abs(z)
fig, ax = plt.subplots(2)

plotGraphic('Magnitude(w)', ax[0], w, modulo)
plotGraphic('Fase(w)', ax[1], w, angulo)
plt.subplots_adjust(hspace=0.5)
plt.show()