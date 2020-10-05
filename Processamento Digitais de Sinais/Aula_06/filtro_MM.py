"""
Implementar o filtro MM para os seguintes tamanhos de média 8, 16, 32. Usar como entrada 
o sweep e comparar as saídas com as do Matlab.
"""
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    with open ('sweep_100_2k.pcm', 'rb') as input_file:   # Le o arquivo em binario
        buf = input_file.read ()
        input_data = np.frombuffer (buf, dtype = 'int16') # Dado é inteiro de 16 bits
        L = input_data [:: 2]     # Canal de audio esquerdo
        R = input_data [1 :: 2]   # Canal de audio direito

    with open ('sai_sweep_mm_4.pcm', 'rb') as output_file:   # Le o arquivo em binario
        buf = output_file.read ()
        output_data = np.frombuffer (buf, dtype = 'int16') # Dado é inteiro de 16 bits
        L = output_data [:: 2]     # Canal de audio esquerdo
        R = output_data [1 :: 2]   # Canal de audio direito
    
    plt.figure(figsize=[15, 10])
    plt.grid(True)
    plt.plot(input_data, label='Entrada')
    plt.legend(loc = 2)
    
    plt.figure(figsize=[15, 10])
    plt.grid(True)
    plt.plot(output_data, label='Saida')
    plt.legend(loc = 2)

    plt.show()