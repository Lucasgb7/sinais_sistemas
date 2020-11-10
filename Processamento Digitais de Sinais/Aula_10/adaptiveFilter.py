"""
• Implementar em Matlab/Python o algoritmo de identificação de sistemas .
• Utilize como sistema desconhecido (Planta) os coeficientes do média móvel.
• Na sequência utilize como planta os coeficientes de um filtro passa baixa já projetado.
• OBS: Gere no Ocenaudio um ruído branco e utilize como entrada do algoritmo.
"""
from numpy import *
from matplotlib.pyplot import *
from scipy.signal import freqz

'''
Condições para implementar o algortimo LMS:
    O filtro deve ter como entrada:
        Vetor de coeficientes, dado por w[n]
        Vetor de entrada, dado por x[n]
        Saída desejada, dada por d[n]
    O filtro deve ter como saída:
        Saída do filtro, dada por y[n]
        Vetor de coeficiente atualizado, dado por w[n + 1]

Passos para implementação do algortimo LMS:
    1. Filtragem:
        y[n] = (w**t)[n] * x[n]
    2. Estimação de erro:
        e[n] = d[n] - y[n]
    3. Adaptação do vetor de coeficientes:
        w[n+1] = w[n] + 2*u*e[n] * x[n]
'''

if __name__ == "__main__":
    fs = 8000
    n = 160         # tamanho dos coeficientes
    w = zeros(n)

    # Entrada (Ruído Branco) -> x[n]
    with open(
            'C:\\Users\\lucas\\Desenvolvimento\\sinais_sistemas\\Processamento Digitais de Sinais\\Aula_10\\white_noise.pcm',
            'rb') as f:
        buf = f.read()
        x = np.frombuffer(buf, dtype='int16')
        xn = x[0:n]  # Garante que tenham os valores de entrada tenham mesmo tamanho

    # Coeficientes de entrada
    with open(
            "C:\\Users\\lucas\\Desenvolvimento\\sinais_sistemas\\Processamento Digitais de Sinais\\Aula_10\\coeficientes_pb.dat",
            'r') as f:
        cof = f.read().replace("\n", "").split(",")
        cof.remove('')

        c = np.asarray(cof, dtype=np.float16)

    d = c.T * xn  # saída desejada (ideal) [utiliza coeficientes e entrada]
    p = 1000  # periodos que fará a aprendizagem (numero de interações)
    ta = 10 ** -6  # taxa de aprendizagem do sistema LMS
    for i in range(p):
        y = w.T * xn  # realiza calculo do FIR
        e = d - y  # taxa de erro (compara sistema ideal, com o sistema obtido até então)
        e = e / abs(sum(e))  # normalizar o erro
        w = w + 2 * ta * e * xn  # atualiza o sistema obtido para realizar novamente o cálculo

    t = arange(0, n/fs, 1/fs)
    figure(1)
    plot(xn, label="Entrada", color='cyan')
    legend()
    title("Ruído Branco")
    xlabel("n")
    ylabel("x(n)")

    figure(2)
    subplot(211)
    plot(c, label="Coeficientes", color='green')
    legend()
    title("Coeficientes Filtro PB")
    xlabel("n")
    ylabel("w(n)")
    subplot(212)
    plot(w, label="Vetor de coeficientes atualizado", color='red')
    legend()
    title("Coenficientes aprendidos (w[n])")
    xlabel("n")
    ylabel("w(n)")

    figure(3)
    subplot(211)
    plot(d, label="Saída desejada", color='green')
    legend()
    title("Saída ideal (d[n])")
    xlabel("n")
    ylabel("d(n)")
    subplot(212)
    plot(y, label="Saída do filtro", color='red')
    legend()
    title("Saída do filtro (y[n])")
    xlabel("n")
    ylabel("y(n)")

    figure(4)
    plot(e, label="Erro", color='magenta')
    legend()
    title("Estimação do erro (e[n])")
    xlabel("Nº de Amostras")
    ylabel("e(n)")

    grid()
    show()