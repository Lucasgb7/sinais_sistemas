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


# Equation 16.4 + Constant K
def kernelFilter_K(k, m, fc, i):
    h = k * (sin(2 * pi * fc * (i - m / 2)) / (i - m / 2)) * (0.42 - 0.5 * cos(2 * pi * i / m) + 0.08 * cos(4 * pi * i / m))
    h = h / sum(h)
    return h

if __name__ == "__main__":
    fs = 8000
    # fs = int(input("Determine a frequência de amostragem (FS): "))
    fcPB = 600
    # fcPB = int(input("Determine a frequência de corte PB(fcPB): "))
    fcPA = 3000
    # fcPA = int(input("Determine a frequência de corte PA(fcPA): "))
    fcPF1 = 600
    # fcPF1 = int(input("Determine a frequência de corte FC1(fcPF1): "))
    fcPF2 = 3000
    # fcPF2 = int(input("Determine a frequência de corte FC2(fcPF2): "))
    bw = 200
    # bw = int(input("Determine a faixa de transição (BW): "))
    k = 1
    # k = int(input("Determine a constante (K): "))

    bwN = bw / fs   # Banda de transição normalizada
    # fcN = fc / fs   # Determina a frequência de corte normalizada (entre 0.0 e 0.5)
    fcPB = fcPB / fs
    fcPA = fcPA / fs
    fcPF1 = fcPF1 / fs
    fcPF2 = fcPF2 / fs
    m = 4 / bwN                 # Determina o tamanho do filtro (M+1)
    i = arange(10**-9, m, 1.)   # de -m/2 ate m/2

    # Filtro passa-baixa
    hPB = kernelFilter_K(k, m, fcPB, i)

    # Filtro passa-alta
    hPA = kernelFilter_K(k, m, fcPA, i)
    hPA = -hPA
    hPA[int(m/2)] += 1

    # Filtro passa-faixa
    hPF1 = kernelFilter_K(k, m, fcPF2, i)   # Passa-Baixa (passa frequencia mais alta)
    hPF2 = kernelFilter_K(k, m, fcPF1, i)
    hPF2 = -hPF2
    hPF2[int(m/2)] += 1                   # Passa-Alta (passa frequencia mais baixa)
    hPF = convolve(hPF2, hPF1)  # PA * PB = PF

    gb = .7
    # gb = float(input("Defina o ganho do filtro passa-baixa (GB): "))
    gf = .6
    # gf = float(input("Defina o ganho do filtro passa-faixa (GF): "))
    ga = .5
    # ga = float(input("Defina o ganho do filtro passa-alta (GA): "))
    # Leitura de arquivo
    with open('C:\\Users\\lucas\\Desenvolvimento\\sinais_sistemas\\Processamento Digitais de Sinais\\Aula_09\\sweep_3800.pcm','rb') as f:  # Sweep de 1 a 3.8KHz
        buf = f.read()
        inputData = frombuffer(buf, dtype='int16')

        # Realizando cálculos com os ganhos de verificação
        outputPB = gb * convolve(hPB, inputData, 'same')
        outputPF = gf * convolve(hPF, inputData, 'same')
        outputPA = ga * convolve(hPA, inputData, 'same')
        outputData = outputPB + outputPA + outputPF
        outputData = outputData.astype(dtype='int16') # convertendo para tipo 16bits igual ao arquivo

    t = arange(0, len(inputData)/fs, 1/fs)  # amostra de tempo para 100ms

    figure(1)
    plot(t, inputData[: len(t)], label="Entrada")
    plot(t, outputData[: len(t)], label="Saida")
    legend()
    xlabel("Tempo (s)")
    ylabel("Amplitude")

    # Utilizando comando freqz para plotar em frequencia
    w1, h1 = freqz(hPA, worN=fs, fs=1)
    w2, h2 = freqz(hPB, worN=fs, fs=1)
    w3, h3 = freqz(hPF, worN=fs, fs=1)
    figure(2)
    # plot(w1, freq_DB(h1), label="freqz1")
    # plot(w2, freq_DB(h2), label="freqz2")
    plot(w1, abs(h1), label="Filtro passa-alta")
    plot(w2, abs(h2), label="Filtro passa-baixa")
    plot(w3, abs(h3), label="Filtro passa-faixa")
    legend()
    xlabel("Frequencia (Hz)")
    ylabel("Amplitude")

    grid()
    show()

    with open('C:\\Users\\lucas\\Desenvolvimento\\sinais_sistemas\\Processamento Digitais de Sinais\\Aula_09\\equalizador.pcm', 'wb') as f:
        for d in outputData:
            f.write(d)

    grid()
    show()