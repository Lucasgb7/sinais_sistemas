# -*- coding: utf-8 -*-
"""
Exemplo do calculo de convolucao
       
@author: lucas
"""
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    v = [np.full(8, 1), [1, 0, 0, 0, 0, 0, 0, 0], [1, 0.5, 0.25, 0.125]]
    x = 0
    while x is 0:
        print("0-Degrau Unitario \n1-Impulso Unitario \n2-x[n]=[1, 0.5, 0.25, 0.125]")
        a = int(input("Selecione uma das opções: "))
        if 0 <= a <= 2:
            x = v[a]
    
    h = [1, 0.5, 0.25, 0.125]
    y = np.convolve(x, h)   # retorna a convolucao linear e discreta dos dois vetores
    
    plt.grid(True)
    plt.title("Convolução entre x e h")
    plt.xlabel("n")
    plt.ylabel("x[n]")
    plt.stem(y)