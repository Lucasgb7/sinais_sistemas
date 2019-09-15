import numpy as np
import matplotlib.pyplot as plt

# def degrau(x):     
#     y = np.zeros(len(x))     
#     for i in range(0,len(x)):         
#         if x[i] >= 0:             
#             y[i] = 1.     
#             return y

# tau = 1
# t = np.arange(-5, 5, 0.1)
# funcao_tempo = degrau(t + tau/2) - degrau(t - tau/2)

# plt.subplot(221)
# plt.ylabel('F(t)')
# plt.xlabel('t')
# plt.title('Função Porta F(t)')
# plt.plot(t, funcao_tempo)
# plt.grid(True)

# w = t
# funcao_frequencia = integrate.quad(lambda x: funcao_tempo*(np.exp(-1j*w*t)), -tau/2, tau/2)
# plt.subplots_adjust(hspace=.5)
# plt.show()

T = .001
t = np.range(-10, 10, 0.1)
f_t = np.zeros(len(t), 1)

for i in range(0, len(t))
    if (t[i] >= -T):
        if (t[i] <= T):
            f_t[i] = 1

plt.subplot(221)
plt.ylabel('F(t)')
plt.xlabel('t')
plt.title('Função Porta F(t)')
plt.plot(t, funcao_tempo)
plt.grid(True)

w = np.range(-10, 10, 0.1)
F = np.zeros(1, len(t))

for i in range(0, len(w)):
  if w[i] == 0: 
      F[i] = 2*T
  else  
     F[i] =  (2/w[i])*sin(w[i]*T)

plt.subplot(222)
plt.ylabel('F(w)')
plt.xlabel('freq')
plt.title('F(w)')
plt.plot(t, F)
plt.grid(True)

plt.subplot(223)
plt.title('|F(W)|')
plt.xlabel("Freq (rad/seg)")
plt.ylabel("Magnitude")
plt.plot(w, np.absolute(F))
plt.grid(True)