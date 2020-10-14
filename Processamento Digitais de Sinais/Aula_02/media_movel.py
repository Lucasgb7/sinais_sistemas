# -*- coding: utf-8 -*-
"""
Implementação de media movel em Python.
    Usar como entrada um sinal de ruido branco gerado no OceanAudio
    Testar com diferentes tamanhos de media e salvar o arquivo de saida
    por exemplo: k = 4, k = 8, k = 16, k = 32, etc.
"""
import numpy as np
import matplotlib.pyplot as plt

# Funcao de media movel (dado, tamanho de media)
def moving_average(a, n) : 
    ret = np.cumsum(a, dtype=float) # np.cumsum() retorna a soma cumulativa dos elementos ao longo do eixo
    ret[n:] = ret[n:] - ret[:-n] 
    return ret[n - 1:] / n # divide os valores pelo tamanho de media

if __name__ == "__main__":
    with open ('C:\\Users\\lucas\\Desenvolvimento\\sinais_sistemas\\Processamento Digitais de Sinais\\Aula_02\\swip.pcm', 'rb') as f:   # Le o arquivo em binario
        buf = f.read ()
        data = np.frombuffer (buf, dtype = 'int16') # Dado é inteiro de 16 bits
        L = data [:: 2]     # Canal de audio esquerdo
        R = data [1 :: 2]   # Canal de audio direito
    
    allowed_keys = [4, 8, 16, 32, 64, 128, 256, 512, 1024]  # Tamanhos de media
    k = 0
    
    while(k not in allowed_keys): # Garante que o usuario vai digitar os valores corretos
        k = int(input("Digite o tamanho de média (k): "))
        if (k not in allowed_keys):
            print("Valores permitidos: 4, 8, 16, 32, 64, 128, 256, 512, 1024.")

    new_data = moving_average(data, k) # Media movel
    
    plt.figure("Figura 1",figsize=(15,8))

    plt.subplot(211)
    plt.title("Sinal de entrada")
    plt.xlabel("Número de amostras")
    plt.ylabel("Amplitude da saída")
    plt.grid(1)
    plt.plot(data)
    
    plt.subplot(212)
    plt.title("Sinal de saída")
    plt.xlabel("Número de amostras")
    plt.ylabel("Amplitude da saída")
    plt.grid(1)
    plt.plot(new_data,color='red')
    
    
    with open("C:\\Users\\lucas\\Desenvolvimento\\sinais_sistemas\\Processamento Digitais de Sinais\\Aula_02\\media_movel.pcm", "wb") as new_file: # escreve no arquivo de saida
        for x in new_data:
            new_file.write(x)
    new_file.close()
