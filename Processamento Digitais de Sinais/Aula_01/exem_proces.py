'''
*** Programa exemplo para PDS:
** Ler um arquivo de entrada, processar a amostra lida multiplicando por uma constante e escrever o resultado em um vetor de saida.
* Desenvolvido por: Lucas José da Cunha
* Aula_01
'''
import numpy as np
import matplotlib.pyplot as plt

with open ('alo.pcm', 'rb') as f:   # Le o arquivo em binario
    buf = f.read ()
    data = np.frombuffer (buf, dtype = 'int16') # Dado é inteiro de 16 bits
    L = data [:: 2]     # Canal de audio esquerdo
    R = data [1 :: 2]   # Canal de audio direito

# Desenha o grafico do sinal de entrada
plt.subplot(221)
plt.plot(data)
plt.grid(True)
plt.title('Sinal de Entrada')
plt.ylabel('Amplitude')
plt.xlabel('Número de Amostras')
plt.show()

data_length = len(data) # Tamanho do sinal de entrada
values = np.zeros((data_length, 1)) # Valores intermediarios
gain = 0.5  # Ganho a ser multiplicado

for i in range(data_length):
    values = data[i] * gain # Le as amostras e multiplica cada uma pelo ganho

# Desenha o grafico do sinal de saida
plt.subplot(222)
plt.plot(values)
plt.grid(True)
plt.title('Sinal de Saída')
plt.ylabel('Amplitude')
plt.xlabel('Número de Amostras')
plt.show()

"""
f = open('sinal_saida.pcm', 'wb') 
for sample in f:
    for channel in channels:
        f.write(the_bytes_in_the_right_endianness)
        """