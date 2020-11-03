"""
• Implementar em Matlab/Python o algoritmo de identificação de sistemas .
• Utilize como sistema desconhecido (Planta) os coeficientes do média móvel.
• Na sequência utilize como planta os coeficientes de um filtro passa baixa já projetado.
• OBS: Gere no Ocenaudio um ruído branco e utilize como entrada do algoritmo.
"""
from numpy import *
from matplotlib.pyplot import *
from scipy.signal import freqz
'''
Condições para implementar o algortimo LMS:
    O filtro deve ter como entrada:
        Vetor de coeficientes, dado por w[n]
        Vetor de entrada, dado por x[n]
        Saída desejada, dada por d[n]
    O filtro deve ter como saída:
        Saída do filtro, dada por y[n]
        Vetor de coeficiente atualizado, dado por w[n + 1]

Passos para implementação do algortimo LMS:
    1. Filtragem:
        y[n] = (w**t)[n] * x[n]
    2. Estimação de erro:
        e[n] = d[n] - y[n]
    3. Adaptação do vetor de coeficientes:
        w[n+1] = w[n] + 2*u*e[n] * x[n]
'''


# Equation 16.4 + Constant K
def kernelFilter_K(k, m, fc, i):
    h = k * (sin(2 * pi * fc * (i - m / 2)) / (i - m / 2)) * (0.42 - 0.5 * cos(2 * pi * i / m) + 0.08 * cos(4 * pi * i / m))
    h = h / sum(h)
    return h

if __name__ == "__main__":
    fs = 8000
    # fs = int(input("Determine a frequência de amostragem (FS): "))
    fc = 400
    # fc = int(input("Determine a frequência de corte (FC): "))
    bw = 200
    # bw = int(input("Determine a faixa de transição (BW): "))
    k = 1
    # k = int(input("Determine a constante (K): "))

    bwN = bw / fs  # Banda de transição normalizada
    fcN = fc / fs  # Determina a frequência de corte normalizada (entre 0.0 e 0.5)
    m = 4 / bwN  # Determina o tamanho do filtro (M+1)
    i = arange(10 ** -9, m, 1.)  # de -m/2 ate m/2

    # Entrada (Ruído Branco) -> x[n]
    with open('C:\\Users\\lucas\\Desenvolvimento\\sinais_sistemas\\Processamento Digitais de Sinais\\Aula_10\\white_noise.pcm','rb') as f:
        buf = f.read ()
        x = np.frombuffer (buf, dtype = 'int16')
        Lx = x[::2]
        Rx = x[1::2]

    # Sistema Desconhecido (Planta) -> d[n]
    with open('C:\\Users\\lucas\\Desenvolvimento\\sinais_sistemas\\Processamento Digitais de Sinais\\Aula_10\\sistema_desconhecido.pcm','rb') as f:
        d = np.frombuffer (buf, dtype = 'int16')
        Ld = d[::2]
        Rd = d[1::2]

    n = len(d)
    # Filtro passa-baixa
    x = kernelFilter_K(k, m, fcN, i)

    # Filtragem
    y = zeros(n)
    y[n] = w[n] * x[n]

    # Estimação de erro
    e = zeros(n)
    e[n] = d[n] - y[n]

    # Adaptação do vetor de coeficientes
    w[n+1] = w[n] + 2 * 10**-6 * e[n] * x[n]