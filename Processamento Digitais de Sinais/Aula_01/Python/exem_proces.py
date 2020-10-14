'''
*** Programa exemplo para PDS:
** Ler um arquivo de entrada, processar a amostra lida multiplicando por uma constante e escrever o resultado em um vetor de saida.
* Desenvolvido por: Lucas José da Cunha
* Aula_01
'''
import numpy as np
import matplotlib.pyplot as plt
import pickle
import os

with open ('C:\\Users\\lucas\\Desenvolvimento\\sinais_sistemas\\Processamento Digitais de Sinais\\Aula_01\\Python\\alo.pcm', 'rb') as f:   # Le o arquivo em binario
    buf = f.read ()
    data = np.frombuffer (buf, dtype = 'int16') # Dado é inteiro de 16 bits
    L = data [:: 2]     # Canal de audio esquerdo
    R = data [1 :: 2]   # Canal de audio direito

# Desenha o grafico do sinal de entrada
plt.subplot(211)
plt.plot(data)
plt.grid(True)
plt.title('Sinal de Entrada')
plt.ylabel('Amplitude')
plt.xlabel('Número de Amostras')
plt.show()

data_length = len(data) # Tamanho do sinal de entrada
values = np.zeros(data_length) # Valores intermediarios
gain = 0.5  # Ganho a ser multiplicado

for i in range(data_length):
    values[i] = data[i] * gain # Le as amostras e multiplica cada uma pelo ganho

# Desenha o grafico do sinal de saida
plt.subplot(212)
plt.plot(values)
plt.grid(True)
plt.title('Sinal de Saída')
plt.ylabel('Amplitude')
plt.xlabel('Número de Amostras')
plt.show()

with open('C:\\Users\\lucas\\Desenvolvimento\\sinais_sistemas\\Processamento Digitais de Sinais\\Aula_01\\Audio\\sinal_saida.pcm', 'wb') as f:   # Escrever no arquivo de saída
    for v in values:
        f.write(v)
