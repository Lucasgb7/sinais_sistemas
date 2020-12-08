"""
Projete um filtro FIR PA com FS de 8k, Fc de 800Hz e faixa de transição de 200Hz.
• Use o comando freqz e plote a resposta em frequência do filtro.
• Aplique na entrada do filtro um sweep e avalie a saída do filtro.
• Utilize na entrada uma senoide de frequencia igual a Fc e meça a atenuação na saída.
"""
from numpy import *
from matplotlib.pyplot import *
from scipy.signal import freqz


# Coeficientes
def coefficients(wc, Fl):
    a = wc / (Fl + wc)
    b = (wc - Fl) / (Fl + wc)
    return a, b


# Retorna resposta em Decibeis (DB)
def freq_DB(h):
    return 10 * log10(abs(h))


# Equation 16.4 - windowed-sic filter kernel
def kernelFilter(M, h, fc):
    for i in range(int(M)):
        if i - M / 2 == 0:
            h[i] = 2 * pi * fc
        else:
            h[i] = sin(2 * pi * fc * (i - M / 2)) / (i - M / 2)
        h[i] = h[i] * (0.54 - 0.46 * cos(2 * pi * (i / M)))
    return h


if __name__ == "__main__":
    fs = 8000
    #fs = int(input("Determine a frequência de amostragem (FS): "))
    fc = 3000
    #fc = int(input("Determine a frequência de corte (FC): "))
    bw = 200
    #bw = int(input("Determine a faixa de transição (BW): "))
    k = 1
    #k = int(input("Determine a constante (K): "))

    bwN = bw / fs   # Banda de transição normalizada
    fcN = fc / fs   # Determina a frequência de corte normalizada (entre 0.0 e 0.5)
    m = 4 / bwN     # Determina o tamanho do filtro (M+1)
    i = arange(10**-9, m, 1.)   # de -m/2 ate m/2
    # Eq. 16.4
    h1 = k * (sin(2 * pi * fcN * (i - m / 2)) / (i - m / 2)) * (0.42 - 0.5 * cos(2 * pi * i / m) + 0.08 * cos(4 * pi * i / m))
    h1 = h1 / sum(h1) # Normaliza a funcao

    h2 = zeros(int(m))
    h2 = kernelFilter(m, h2, fcN)
    h2 = h2 / sum(h2)  # Normaliza o resultado

    # Inversão espectral (através do FIR PB)
    h1, h2 = -h1, -h2
    # Soma +1 no coeficiente central
    h1[int(m/2)] += 1
    h2[int(m/2)] += 1
    
    with open("C:\\Users\\lucas\\Desenvolvimento\\sinais_sistemas\\Processamento Digitais de Sinais\\Aula_12\\Tarefas\\Filtro_PA\\coef_pa.dat", 'w') as f:
        for d in h1:
            f.write(str(d.astype(np.float16) * 32768) + ",\n")
