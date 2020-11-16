"""
Projeto e implementação do filtro FIR
Capítulo 14: http://www.dspguide.com/ch14/1.htm
• Apresente as principais caractéristicas que são desejáveis em um filtro digital.
• Apresente os procedimentos para se obter a partir de um filtro PB o PA, PF e RF. 
"""
from numpy import *
from matplotlib.pyplot import *


# Aplicando filtro rejeita-faixa
def band_reject(data_lowPass, data_highPass):
    return data_lowPass + data_highPass


# Aplicando filtro passa-faixa
def band_pass(data_lowPass, data_highPass):
    return convolve(data_lowPass, data_highPass)


# Aplicando filtro passa-alta
def high_pass(inputData, outputData, y, a, b):
    hp = low_pass(inputData, outputData, y, a, b)
    return inputData - hp


# Aplicando filtro passa-baixa
def low_pass(inputData, outputData, y, a, b):
    # Arquivo cópia para salvar o resultado lido
    outputData = zeros_like(inputData)
    aux = zeros(2)  # Variavel auxiliar para receber cada amostra da entrada
    previousOutput = 0  # Definindo a variavel de saida anterior como 0
    for i in range(len(inputData)):
        aux[0] = inputData[i]  # Recebe a amostra no momento (i)
        y = (a * aux[0]) + (a * aux[1]) - (b * previousOutput)
        previousOutput = y  # Salva a saída anterior
        outputData[i] = y
        aux[1:2] = aux[0:1]  # Iguala o começo da array com o final

    return outputData


def plotSignal(i, data, xLabel, yLabel, titulo):
    subplot(i)
    title(titulo)
    xlabel(xLabel)
    ylabel(yLabel)
    grid(1)
    plot(data)
    tight_layout()


def omega_cutoff(Fc):
    return 2 * pi * Fc


def coefficients(wc, Fl):
    a = wc / (Fl + wc)
    b = (wc - Fl) / (Fl + wc)
    return a, b


if __name__ == "__main__":
    y = 0               # Media do buffer
    outputData = 0      # Saida
    Fs = 8000           # Frequência do sistema = 8KHz
    Fc = 1000           # Frequência de corte = 1KHz
    Fl = 2 * Fs         # F linha = 2Fs = 16KHz
    wc = omega_cutoff(Fc)    # Magnitude: wc = 2piFc = 6280

    # Coeficientes para equação
    a, b = coefficients(wc, Fl)

    print("Coeficiente A:", a)
    print("Coeficiente B:", b)

    # Leitura de arquivo
    with open(
            'C:\\Users\\lucas\\Desenvolvimento\\sinais_sistemas\\Processamento Digitais de Sinais\\Aula_08\\sweep_3800.pcm',
            'rb') as f:  # Sweep de 1 a 3.8KHz
        buf = f.read()
        inputData = frombuffer(buf, dtype='int16')

    # t = np.arange(0, len(inputData)/Fs, 1 / Fs)     # 100ms
    # stem(t, inputData[: len(t)], "k-", "ko", "k-", label="Input")
    # plot(t, outputData[: len(t)], label="Output")

    outputData = low_pass(inputData, outputData, y, a, b)
    data_lowPass = outputData
    figure(1)
    plotSignal(211, inputData, "Nº de Amostras", "Amplitude", "Entrada")
    plotSignal(212, data_lowPass, "Nº de Amostras", "Amplitude", "Filtro passa-baixa")
    outputData = 0
    show()

    outputData = high_pass(inputData, outputData, y, a, b)
    data_highPass = outputData
    figure(2)
    plotSignal(211, data_lowPass, "Nº de Amostras", "Amplitude", "Filtro passa-baixa")
    plotSignal(212, data_highPass, "Nº de Amostras", "Amplitude", "Filtro passa-alta")
    outputData = 0
    show()

    Fc_A = 3000
    Fc_A = Fc_A / Fs
    Fc_B = 1000
    Fc_B = Fc_B / Fs
    wc_A = omega_cutoff(Fc_A)   # wc = 2piFc
    wc_B = omega_cutoff(Fc_B)   # wc = 2piFc
    # Adquirindo os coeficientes
    A1, A2 = coefficients(wc_A, Fl)
    B1, B2 = coefficients(wc_B, Fl)
    print("Coeficiente A1 e A2:", A1, A2)
    print("Coeficiente B1 e B2:", B1, B2)

    pb_band_pass = low_pass(inputData, outputData, y, A1, A2)
    pa_band_pass = high_pass(pb_band_pass, outputData, y, B1, B2)
    outputData = band_pass(pb_band_pass, pa_band_pass)
    data_bandPass = outputData
    figure(3)
    plotSignal(211, data_bandPass, "Nº de Amostras", "Amplitude", "Filtro passa-faixa")
    outputData = 0

    Fc_A = 400
    Fc_B = 800
    wc_A = omega_cutoff(Fc_A)
    wc_B = omega_cutoff(Fc_B)
    # Adquirindo os coeficientes
    A1, A2 = coefficients(wc_A, Fl)
    B1, B2 = coefficients(wc_B, Fl)
    print("Coeficiente A1 e A2:", A1, A2)
    print("Coeficiente B1 e B2:", B1, B2)

    pb_aux = low_pass(inputData, outputData, y, A1, A2)
    pa_aux = high_pass(pb_aux, outputData, y, B1, B2)
    outputData = band_reject(pb_aux, pa_aux)
    data_bandReject = outputData
    plotSignal(212, data_bandReject, "Nº de Amostras", "Amplitude", "Filtro rejeita-faixa")
    show()

    """
    # Escreve resultado em outro arquivo .pcm
    file_name = "output_digitalFilters.pcm"
    with open(file_name, 'wb') as f:
        for d in outputData:
            f.write(d)
    """
