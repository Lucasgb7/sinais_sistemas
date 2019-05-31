import numpy as np
import math as m
import matplotlib.pyplot as plt

t = np.arange(-5, 5, 0.1)
formula = [	3 * (np.exp(1)**(2*t)),
			3 * (np.exp(1)**(-2*t)),
			3 * (np.exp(1)**(1j*2*t)),
			np.sqrt(2)*220*np.sin((2*np.pi)-(60*t))
			]

plt.figure(1)

# 3e^2t
plt.subplot(221)
plt.plot(t, formula[0])
plt.ylabel('Y(t)')
plt.xlabel('T')
plt.title('3e^2t')
plt.grid(True)

# 3e^-2t
plt.subplot(222)
plt.plot(t, formula[1])
plt.ylabel('Y(t)')
plt.xlabel('T')
plt.title('3e^-2t')
plt.grid(True)

# 3e^j2t
plt.subplot(223)
plt.plot(t, formula[2])
plt.ylabel('Y(t)')
plt.xlabel('T')
plt.title('3e^j2t')
plt.grid(True)

# sqrt(2).220sin(2*pi.60t)
plt.subplot(224)
plt.plot(t, formula[3])
plt.ylabel('Y(t)')
plt.xlabel('T')
plt.title('sqrt(2).220sin(2*pi.60t)')
plt.grid(True)

plt.subplots_adjust(hspace=.5)
plt.show()