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
    return 20 * log10(abs(h))


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
    # fs = int(input("Determine a frequência de amostragem (FS): "))
    fc1 = 600
    # fc1 = int(input("Determine a frequência de corte 1(FC1): "))
    fc2 = 3000
    # fc2 = int(input("Determine a frequência de corte 2(FC2): "))
    bw = 200
    # bw = int(input("Determine a faixa de transição (BW): "))
    k = 1
    # k = int(input("Determine a constante (K): "))

    bwN = bw / fs   # Banda de transição normalizada
    # fcN = fc / fs   # Determina a frequência de corte normalizada (entre 0.0 e 0.5)
    fc1 = fc1 / fs
    fc2 = fc2 / fs
    m = 4 / bwN     # Determina o tamanho do filtro (M+1)
    i = arange(10**-9, m, 1.)   # de -m/2 ate m/2

    # Filtro passa-alta
    h1 = k * (sin(2 * pi * fc1 * (i - m / 2)) / (i - m / 2)) * (0.42 - 0.5 * cos(2 * pi * i / m) + 0.08 * cos(4 * pi * i / m))
    h1 = h1 / sum(h1) # Normaliza a funcao
    h1 = -h1          # Inversão
    h1[int(m/2)] += 1

    # Filtro passa-baixa
    # Eq. 16.4
    h2 = k * (sin(2 * pi * fc2 * (i - m / 2)) / (i - m / 2)) * (0.42 - 0.5 * cos(2 * pi * i / m) + 0.08 * cos(4 * pi * i / m))
    h2 = h2 / sum(h2) # Normaliza a funcao

    h = convolve(h2, h1, 'same')
    with open("C:\\Users\\lucas\\Desenvolvimento\\sinais_sistemas\\Processamento Digitais de Sinais\\Aula_09\\coef_pf.dat", 'w') as f:
        for d in h:
            f.write(str(d.astype(np.float16)) + ",\n")

    # Leitura de arquivo
    with open('C:\\Users\\lucas\\Desenvolvimento\\sinais_sistemas\\Processamento Digitais de Sinais\\Aula_09\\sweep_3800.pcm','rb') as f:  # Sweep de 1 a 3.8KHz
        buf = f.read()
        inputData = frombuffer(buf, dtype='int16')
        # Convolução: PB * PA = PF
        outputData = convolve(h1, inputData)
        outputData = convolve(h2, outputData)
        outputData = outputData.astype(dtype='int16') # convertendo para tipo 16bits igual ao arquivo

    t = arange(0, len(inputData)/fs, 1/fs)  # amostra de tempo para 100ms

    figure(1)
    plot(t, inputData[: len(t)], label="Entrada")
    plot(t, outputData[: len(t)], label="Saida")
    legend()
    xlabel("Tempo (s)")
    ylabel("Amplitude")

    # Utilizando comando freqz para plotar em frequencia
    w1, h1 = freqz(h1, worN=fs, fs=fs)
    w2, h2 = freqz(h2, worN=fs, fs=fs)
    figure(2)
    plot(w1, freq_DB(h1), label="freqz1")
    plot(w2, freq_DB(h2), label="freqz2")
    # plot(w1, abs(h1), label="Filtro passa-baixa")
    # plot(w2, abs(h2), label="Filtro passa-alta")
    legend()
    xlabel("Frequencia (Hz)")
    ylabel("Amplitude (dB)")

    grid()
    show()

    with open('C:\\Users\\lucas\\Desenvolvimento\\sinais_sistemas\\Processamento Digitais de Sinais\\Aula_09\\filtroPF.pcm', 'wb') as f:
        for d in outputData:
            f.write(d)