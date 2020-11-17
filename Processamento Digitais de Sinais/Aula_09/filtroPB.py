"""
Projete um filtro FIR PB com FS de 8k, Fc de 800Hz e faixa de transição de 200Hz.
• Use o comando freqz e plote a resposta em frequência do filtro.
• Aplique na entrada do filtro um sweep e avalie a saída do filtro.
• Utilize na entrada uma senoide de frequencia igual a Fc e meça a atenuação na saída.
"""
from numpy import *
from matplotlib.pyplot import *
from scipy.signal import freqz

# Coeficientes
def coefficients(wc, Fl):
    a = wc / (Fl + wc)
    b = (wc - Fl) / (Fl + wc)
    return a, b

def freq_DB(h):
    return 20 * log10(abs(h))

# Equation 16.4 - windowed-sic filter kernel
def kernelFilter(M, h, fc):
    for i in range(int(M)):
        if i - M / 2 == 0:
            h[i] = 2 * pi * fc
        else:
            h[i] = sin(2 * pi * fc * (i - M / 2)) / (i - M / 2)
        h[i] = h[i] * (0.54 - 0.46 * cos(2 * pi * (i / M)))
    return h


if __name__ == "__main__":
    fs = 8000; #fs = int(input("Determine a frequência de amostragem (FS): "))
    fc = 800; #fc = int(input("Determine a frequência de corte (FC): "))
    bw = 200; #bw = int(input("Determine a faixa de transição (BW): "))
    k = 1; #k = int(input("Determine a constante (K): "))

    bwN = bw / fs   # Banda de transição normalizada
    fcN = fc / fs   # Determina a frequência de corte normalizada (entre 0.0 e 0.5)
    m = 4 / bwN     # Determina o tamanho do filtro (M+1)
    i = arange(10**-9, m, 1.)   # de -m/2 ate m/2
    # Eq. 16.4
    h1 = k * (sin(2 * pi * fcN * (i - m / 2)) / (i - m / 2)) * (0.42 - 0.5 * cos(2 * pi * i / m) + 0.08 * cos(4 * pi * i / m))
    h1 = h1 / sum(h1) # Normaliza a funcao

    h2 = zeros(int(m))
    h2 = kernelFilter(m, h2, fcN)
    h2 = h2 / sum(h2)  # Normaliza o resultado

    with open("C:\\Users\\lucas\\Desenvolvimento\\sinais_sistemas\\Processamento Digitais de Sinais\\Aula_09\\coef_pb.dat", 'w') as f:
        for d in h2:
            f.write(str(d.astype(np.float16)) + ",\n")

    # Leitura de arquivo
    with open('C:\\Users\\lucas\\Desenvolvimento\\sinais_sistemas\\Processamento Digitais de Sinais\\Aula_09\\sweep_3800.pcm','rb') as f:  # Sweep de 1 a 3.8KHz
        buf = f.read()
        inputData = frombuffer(buf, dtype='int16')
        outputData = convolve(h2, inputData)
        outputData = outputData.astype(dtype='int16') # convertendo para tipo 16bits igual ao arquivo

    t = arange(0, len(inputData)/fs, 1/fs)  # amostra de tempo para 100ms

    figure(1)
    plot(t, inputData[: len(t)], label="Entrada")
    plot(t, outputData[: len(t)], label="Saida")
    legend()
    xlabel("Tempo (s)")
    ylabel("Amplitude")

    # Utilizando comando freqz para plotar em frequencia
    w1, h1 = freqz(h1, worN=fs, fs=1)
    w2, h2 = freqz(h2, worN=fs, fs=1)
    figure(2)
    # plot(w1, freq_DB(h1), label="Blackman")
    # plot(w2, freq_DB(h2), label="Hamming")
    plot(w1, abs(h1), label="Blackman")
    plot(w2, abs(h2), label="Hamming")
    legend()
    xlabel("Frequencia (Hz)")
    ylabel("Amplitude")

    grid()
    show()

    with open('C:\\Users\\lucas\\Desenvolvimento\\sinais_sistemas\\Processamento Digitais de Sinais\\Aula_09\\filtroPB.pcm', 'wb') as f:
        for d in outputData:
            f.write(d)

    '''
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
    '''