"""
Projeto e implementação do filtro FIR
Capítulo 16: Mttp://www.dspguide.com/ch16.htm
• Faça um programa para plotar a função Sinc.
• Faça um programa para plotar as janelas Hamming(Eq 16-1) e a Blackman(Eq 16-2).
• Descreva em detalhes as etapas mostradas na Fig 16-1
• Faça um programa para plotar a Eq 16-4 para diferentes tamanhos
• Faça um programa para projetar um filtro PB. Siga os passos mostrados na tabela 16-1.
• Utilize os coeficientes obtidos e o comando freqz para plotar a resposta em frequencia do filtro.
• Salve os coeficientes em arquivo e execute o filtro .
• Utilize como exemplo o programa da média móvel.
"""
"""
Função sinc:

       sin(2*pi*Fc*i)
h[i] = --------------
            i*pi
"""
from numpy import *
from matplotlib.pyplot import *
from scipy.signal import freqz

def plotSignal(data, xLabel, yLabel, titulo, color):
    title(titulo)
    xlabel(xLabel)
    ylabel(yLabel)
    grid(1)
    legend(titulo)
    plot(data, color)
    tight_layout()


def plotWindow(data1, data2, color1, color2, yLabel, xLabel, titulo, l1, l2):
    title(titulo)
    xlabel(xLabel)
    ylabel(yLabel)
    grid(1)
    h, = plot(data1, color1, label=l1)
    b, = plot(data2, color2, label=l2)
    legend([h, b], [l1, l2])


def kernelFilter(i, M, h, Fc):
    for i in range(M):
        if i - M / 2 == 0:
            h[i] = 2 * pi * Fc
        else:
            h[i] = sin(2 * pi * Fc * (i - M / 2)) / (i - M / 2)
        h[i] = h[i] * (0.54 - 0.46 * cos(2 * pi * (i / M)))


if __name__ == "__main__":
    # Valores de referência
    sample = 8000       # Amostra de 8KHz
    Fc = 100            # Frequência de corte
    M = 0.5             # Tamanho do filtro

    """ • Faça um programa para plotar a função Sinc.. """
    i = arange(-M/2, M/2, 1/sample)
    sincFunction = sin(2*pi*Fc*i) / i*pi    # sinc(i)
    figure(1)
    plotSignal(sincFunction, "Nº de Amostras", "Amplitude", "Sinc Function", 'b')
    show()

    """ • Faça um programa para plotar as janelas Hamming(Eq 16-1) e a Blackman(Eq 16-2). """
    i = arange(0, M, 1 / sample)
    wBlackman = 0.54 - 0.46 * cos(2 * pi * i / M)   # blackman(i)
    wHamming = 0.42 - 0.5 * cos(2 * pi * i / M) + 0.08 * cos(4 * pi * i / M)    # hamming(i)
    figure(2)
    plotWindow(wHamming, wBlackman, 'b', 'g', "Amplitude", "Nº de Amostras", "Janela Hamming e Blackman", "Hamming", "Blackman")
    show()

    """ • Faça um programa para plotar a Eq 16-4 para diferentes tamanhos """
    M = 500
    Fc = 0.015
    k = 1
    # M = int(input("Determine o valor de M: "))
    # Fc = float(input("Determine o valor de Fc: "))
    i = arange(0, M, 1/sample)
    h = zeros(M)
    # h = k*(sin(2*pi*Fc*(i-M/2))/i-M/2) * (0.42 - 0.5*cos((2*pi*i)/M) + 0.08*cos((4*pi*i)/M))
    kernelFilter(i, M, h, Fc)

    figure(3)
    plotSignal(h, "Nº de Amostras", "Amplitude", "Filtro Kernel", 'b')
    show()

    """ • Faça um programa para projetar um filtro PB. Siga os passos mostrados na tabela 16-1. """
    Fs = 8000
    bw = 400
    Fc = 600
    Fc = Fc / Fs
    bw = bw / Fs
    M = 4 / bw
    Fl = 2 * Fs
    wc = 2 * pi * Fc

    y = zeros(int(M))
    j = arange(1, M, 1/Fs)

    y = (sin(2 * pi * Fc * (j - M / 2)) / (j - M / 2)) * (0.54 - 0.46 * cos(2 * pi * j / M))
    for i in range(len(y)):
        if y[i] == M/2:
            y[i] = 2 * pi * Fc

    # h = h / sum(h)  # Normaliza o resultado
    soma = 0
    for i in range(1, int(M)):
        soma = soma + y[i]

    soma = 0
    for i in range(1, int(M)):
        y[i] = y[i]/soma


    figure(4)
    num_mag = [Fl, -Fl]
    den_mag = [Fl + wc, wc - Fl]
    [w, h] = freqz(num_mag, den_mag, worN=Fs, fs=Fs)
    xlabel("Tempo (s)")
    ylabel("Amplitude")
    title("PB - Magnitude")
    plot(w, 20 * log10(abs(h)), 'r')
    show()