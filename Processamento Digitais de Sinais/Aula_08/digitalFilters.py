"""
Projeto e implementação do filtro FIR
Capítulo 14: http://www.dspguide.com/ch14/1.htm
• Apresente as principais caractéristicas que são desejáveis em um filtro digital.
• Apresente os procedimentos para se obter a partir de um filtro PB o PA, PF e RF. 
"""
from numpy import *
from matplotlib.pyplot import *

def return_db(a, b):
    return 20 * log10(b/a)

if __name__ == "__main__":
    Fs = 8000   # Frequência do sistema = 8KHz
    Fc = 1000   # Frequência de corte = 1KHz
    Fl = 2 * Fs  # F linha = 2Fs = 16KHz
    wc = 2 * pi * Fc    # Magnitude: wc = 2piFc = 6280

    # Coeficientes para equação
    a = wc / (Fl + wc)      
    b = (wc - Fl) / (Fl + wc) 

    print("Coeficiente A:", a)
    print("Coeficiente B:", b)

    # Leitura de arquivo
    with open("sweep_3800.pcm", 'rb') as f: # Sweep de 1 a 3.8KHz     
        buf = f.read()
        inputData = np.frombuffer(buf, dtype='int16')

        # Arquivo cópia para salvar o resultado lido
        outputData = np.zeros_like(inputData)
        aux = zeros(2)  # Variavel auxiliar para receber cada amostra da entrada 
        previousOutput = 0  # Definindo a variavel de saida anterior como 0
        for i in range(len(inputData)):
            aux[0] = inputData[i]   # Recebe a amostra no momento (i)
            y = (a * aux[0]) + (a * aux[1]) - (b * previousOutput)
            previousOutput = y  # Salva a saída anterior
            outputData[i] = y
            aux[1:2] = aux[0:1] # Iguala o começo da array com o final

    # 100ms
    t = np.arange(0, len(inputData)/Fs, 1 / Fs)

    # Plot
    stem(t, inputData[: len(t)], "k-", "ko", "k-", label="Input")
    plot(t, outputData[: len(t)], label="Output")
    legend()
    xlabel("Tempo (s)")
    ylabel("Amplitude")
    show()

    # Escreve resultado em outro arquivo .pcm
    file_name = "output_digitalFilters.pcm"
    with open(file_name, 'wb') as f:
        for d in outputData:
            f.write(d)
