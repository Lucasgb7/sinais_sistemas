"""
Projete um filtro FIR PB com FS de 8k, Fc de 800Hz e faixa de transição de 200Hz.
• Use o comando freqz e plote a resposta em frequência do filtro.
• Aplique na entrada do filtro um sweep e avalie a saída do filtro.
• Utilize na entrada uma senoide de frequencia igual a Fc e meça a atenuação na saída.
"""
from numpy import *
from matplotlib.pyplot import *
from scipy.signal import freqz


def plotSignal(data, titulo, xLabel, yLabel, color):
    title(titulo)
    xlabel(xLabel)
    ylabel(yLabel)
    grid(1)
    plot(data, color)


# Coeficientes
def coefficients(wc, Fl):
    a = wc / (Fl + wc)
    b = (wc - Fl) / (Fl + wc)
    return a, b


# Filtro passa-baixa
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
        aux[1:2] = aux[0:1]  # Iguala o final da array com o começo

    return outputData


# Equation 16.4 - windowed-sic filter kernel
def kernelFilter(M, h, fc):
    for i in range(M):
        if i - M / 2 == 0:
            h[i] = 2 * pi * fc
        else:
            h[i] = sin(2 * pi * fc * (i - M / 2)) / (i - M / 2)
        h[i] = h[i] * (0.54 - 0.46 * cos(2 * pi * (i / M)))
    return h


if __name__ == "__main__":
    fs = 8000; fs = int(input("Determine a frequência de amostragem (FS): "))
    fc = 800; fc = int(input("Determine a frequência de corte (FC): "))
    bw = 200; bw = int(input("Determine a faixa de transição (BW): "))

    bwN = bw / fs   # Banda de transição normalizada
    fcN = fc / fs   # Determina a frequência de corte normalizada (entre 0.0 e 0.5)
    m = 4 / bwN     # Determina o tamanho do filtro (M+1)

    h = zeros(m)
    h = kernelFilter(m, h, fc)

    # Leitura de arquivo
    with open('C:\\Users\\lucas\\Desenvolvimento\\sinais_sistemas\\Processamento Digitais de Sinais\\Aula_08\\sweep_3800.pcm','rb') as f:  # Sweep de 1 a 3.8KHz
        buf = f.read()
        inputData = frombuffer(buf, dtype='int16')

    wc = 2 * pi * fc                # Omega: Magnitude
    fl = 2 * fs                     # F'
    a, b = coefficients(wc, fl)     # Calculo dos coeficientes
    outputPB = low_pass(inputData, 0, 0, a, b)

    num = [fl, -fl]
    den = [fl + wc, wc - fl]
    w, h = freqz(num, den)
    # Plotar a resposta da magnitude
    title("Magnitude da resposta em frequência")
    grid(1)
    plot(w, 20*log10(abs(h)), 'g')