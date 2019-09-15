import numpy as np
import matplotlib.pyplot as pl

t = np.arange(-5, 5, 0.1) 
t0 = 2
w0 = (2*np.pi)/t0
a0 = 1
b = 0

for n in t:
    f = b * np.sin(n * w0 * t)
for (v, i) in f.range():
    f = (v, i) + (v, i-1)

plt.plot(t, f)
plt.ylabel('F(t)')
plt.xlabel('T')
plt.title('Ex.1 Fourier')
plt.grid(True)