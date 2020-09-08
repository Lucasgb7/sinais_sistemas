# -*- coding: utf-8 -*-
"""
Exemplo do calculo de convolucao
    Considere o filtro media movel com k = 8.
    A saida do filtro para as seguintes entradas:
        Impulso uniatario;
        Degrau unitario;
        x[n] = [1, 0.5, 0.25, 0.125]
        
@author: lucas
"""
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    x = np.full(6, 1)   # vetor 1x6, apenas com 1
    h = [1, 0.5, 0.25, 0.125]
    
    y = np.convolve(x, h)   # retorna a convolucao linear e discreta dos dois vetores
    
    plt.grid(True)
    plt.title("Convolução entre x e h")
    plt.xlabel("n")
    plt.ylabel("x[n]")
    plt.stem(y)