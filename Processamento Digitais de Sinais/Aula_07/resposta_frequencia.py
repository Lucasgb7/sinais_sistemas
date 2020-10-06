import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import math

if __name__ == "__main__":
    step = np.pi/1000
    w = np.arange(0, np.pi, step)
    L = 8
    Fs = 8000

    num = np.sin(w*L/2)
    den = np.sin(w/2)
    temp = num/den
    frequencia_rad = (1/L) *(np.absolute(temp))

    plt.plot(w, frequencia_rad)
    plt.title('Frequencia (RAD)')
    plt.xlabel('Frequencia')
    plt.grid(True)

    frequencia_hz = (w/np.pi)*(Fs/2)
    plt.plot(frequencia_hz, frequencia_rad)
    plt.title('Frequencia (HZ)')
    plt.xlabel('Frequencia')
    plt.grid(True)

    atenuacao_db = 20 * math.log10(frequencia_rad)
    plt.plot(frequencia_hz, np.vectorize(atenuacao_db))
    plt.title('Frequencia (HZ)')
    plt.xlabel('Frequencia')
    plt.ylabel('Atenuacao em DB')
    plt.grid(True)
    axes = plt.gca()
    axes.set_xlim([0, 4000])
    axes.set_ylim([-70, 0])
    
    plt.show()
    """
    num = np.full(4, 1/4)
    den = 1
    plt.title('Magnitude em Frequencia')

    figure(2)
    % Usando freqz para obter a resposta em frequencia
    %num = [ .25 .25 .25 .25];
    num = zeros(1,L);
    num(1,:) = 1/L;
    den = [1];
    [H, Freq] = freqz(num,den,Fs);
    plot(Freq*Fs/(2*pi), 20*log10(abs(H)));
    title('Magnitude da resposta em frequencia')
    grid on;
    """