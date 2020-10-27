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


def plotWindow(data1, data2, color1, color2, yLabel, xLabel, titulo):
    title(titulo)
    xlabel(xLabel)
    ylabel(yLabel)
    grid(1)
    plot(data1, color1)
    plot(data2, color2)


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
    i = arange(-M / 2, M / 2, 1 / sample)
    sincFunction = sin(2 * pi * Fc * i) / i * pi    # sinc(i)
    figure(1)
    plotSignal(sincFunction, "Nº de Amostras", "Amplitude", "Sinc Function", 'b')
    show()

    """ • Faça um programa para plotar as janelas Hamming(Eq 16-1) e a Blackman(Eq 16-2). """
    i = arange(0, M, 1 / sample)
    wBlackman = 0.54 - 0.46 * cos(2 * pi * i / M)   # blackman(i)
    wHamming = 0.42 - 0.5 * cos(2 * pi * i / M) + 0.08 * cos(4 * pi * i / M)    # hamming(i)
    figure(2)
    plotWindow(wHamming, wBlackman, 'b', 'g', "Amplitude", "Nº de Amostras", "Hamming e Blackman")
    show()

    """ • Faça um programa para plotar a Eq 16-4 para diferentes tamanhos """
    M = 500
    Fc = 0.015
    k = 1
    M = int(input("Determine o valor de M: "))
    Fc = float(input("Determine o valor de Fc: "))
    i = arange(0, M, 1/sample)
    h = zeros(M)
    # h = k*(sin(2*pi*Fc*(i-M/2))/i-M/2) * (0.42 - 0.5*cos((2*pi*i)/M) + 0.08*cos((4*pi*i)/M))
    kernelFilter(i, M, h, Fc)

    figure(3)
    plotSignal(h, "Nº de Amostras", "Amplitude", "Filtro Kernel", 'b')
    show()

    """ • Faça um programa para projetar um filtro PB. Siga os passos mostrados na tabela 16-1. """
    x = zeros(4999)
    y = zeros(4999)
    h = zeros(100)
    Fc = 0.14
    M = 100
    kernelFilter(i, M, h, Fc)
    aux = 0
    for i in range(M):
        aux = aux + h[i]

    for i in range(M):
        h[i] = h[i] / aux

    for j in range(100, len(x)):
        y[i] = 0
        for i in range(M):
            y[j] = y[j] + x[j-i] * h[i]

    figure(4)
    plotSignal(y, "Número de Amostras", "Amplitude", "Filtro PB", 'b')