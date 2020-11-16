from numpy import *
from matplotlib.pyplot import *
from scipy.signal import freqz


# Equation 16.4 - windowed-sic filter kernel
def kernelFilter(M, h, fc):
    for i in range(int(M)):
        if i - M / 2 == 0:
            h[i] = 2 * pi * fc
        else:
            h[i] = sin(2 * pi * fc * (i - M / 2)) / (i - M / 2)
        h[i] = h[i] * (0.54 - 0.46 * cos(2 * pi * (i / M)))
    return h


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
    bwN = bw / fs   # Banda de transição normalizada
    fcN = fc / fs   # Determina a frequência de corte normalizada (entre 0.0 e 0.5)
    m = 4 / bwN     # Determina o tamanho do filtro (M+1)
    i = arange(10 ** -9, m, 1.)  # de -m/2 ate m/2

    coeficientes = kernelFilter_K(m, m, fcN, i)
    # Salva coeficientes em um arquivo .dat
    with open("C:\\Users\\lucas\\Desenvolvimento\\sinais_sistemas\\Processamento Digitais de Sinais\\Aula_09\\coeficientes_pb.dat", 'w') as f:
        for d in coeficientes:
            f.write(str(d.astype(np.float16)) + ",\n")