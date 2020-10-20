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

if __name__ == "__main__":
    inputData = 5000
    outputData = 0
    filterKernel = zeros(100)
    Fc = 1000
    M = len(filterKernel)

    for i in range(M):
        if i - M/2 == 0:
            filterKernel[i] = 2 * pi * Fc
        elif i - M/2 < 0 or i - M/2 > 0:
            sin(2 * pi * Fc * (i - M/2)) / (i - M/2)
        filterKernel[i] = filterKernel[i] * (0.54 - 0.46 * cos(2 * pi * i/M))
    
    aux = 0
    for i in range(M):
        aux = aux + filterKernel[i]
  