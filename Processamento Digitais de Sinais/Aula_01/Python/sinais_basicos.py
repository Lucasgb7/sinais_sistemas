# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 16:00:52 2020

Sinais básicos para DSP
Obs.: Alterar os valores da linha 55 caso queira utilizar uma sequência diferente na parte exponencial.

@author: lucas
"""
import numpy as np
import matplotlib.pyplot as plt

# Degrau unitario
def degrau_unitario():
    n = np.arange(-10, 10)  # Vetor de valores de -10 a 20
    length = np.size(n)
    s = np.zeros(length)    # Zerando os valores
    index = np.where(n>=0)
    s[index] = 1
    
    plt.stem(n, s, use_line_collection = True) # Plota a parte unitaria do vetor
    plt.title('Degrau Unitario')
    plt.xlabel('n')
    plt.grid(True)

# Impulsto unitario
def impulso_unitario():
    n = np.arange(-10, 10)  # Vetor de valores de -10 a 20
    length = np.size(n)
    s = np.zeros(length)    # Zerando os valores
    index = np.where(n==0)
    s[index] = 1
    
    plt.stem(n, s, use_line_collection = True) # Plota a partir do valor definido
    plt.title('Impulso Unitario')
    plt.xlabel('n')
    plt.grid(True)

# Sequencia Sinusoidal
def sinusoidal():
    n = np.arange(-20, 20, 1)
    f = 100
    Fs = 8000
    
    s = np.sin(2*np.pi*n*(f/Fs))
    
    plt.stem(n, s, use_line_collection = True)
    plt.title('Sinusoidal (Fo=100Hz e Fs=8kHz)')
    plt.ylabel('Y')
    plt.grid(True)

# Sequencia Exponencial
def exponencial():
    n = np.arange(0, 30, 1)
    A = 1   
    a = .5  # valor a ser alterado
    
    s = A*a**n
    
    plt.stem(n, s, use_line_collection = True)
    plt.title('Exponencial (a = 2)')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    
    
if __name__ == "__main__":
    plt.close('all')
    print("Selecione uma das seguintes opções: ")
    option = input("'D': Degrau Unitario \n'I': Impulso Unitario \n'S': Sequencia Sinusoidal \n'E': Sequencia Exponencial\n\n")
    inf option == 'D' : degrau_unitario()
    elif option == 'I': impulso_unitario()
    elif option == 'S': sinusoidal()
    elif option == 'E': exponencial()
    else:
        exit()
   