import numpy as np
from scipy.io import wavfile

def sign(x):
    x = x*-1
    aux = np.zeros_like(x, dtype="short")
    for i in range(len(x)):
        if x[i] > 0:

            aux[i] = 1

        elif x[i] == 0:

            aux[i] = 0
        else:

            aux[i] = -1

    return aux


def fuzz(input, ganho, mix):
    q = input * ganho / np.max(abs(input))
    print("Q: ", q)
    z = sign(q) * (1-np.exp(sign(q)*q))
    print("Z: ", z)
    y = mix * z * (np.max(abs(input)) / np.max(abs(z))) + (1-mix) * input
    print("Y: ", y)
    output = y * np.max(abs(input)) / np.max(abs(y))
    print("out: ", output)
    return output


if __name__ == "__main__":

    # Le o arquivo
    sample, data = wavfile.read("C:\\Users\\lucas\\Desenvolvimento\\sinais_sistemas\\Processamento Digitais de Sinais\\Aula_13\\Python\\acoustic.wav")

    ganho = 5
    mix = 1

    print("Original wave: ", data)

    output_data = fuzz(data/32768, ganho, mix)

    # Escreve no arquivo
    wavfile.write("C:\\Users\\lucas\\Desenvolvimento\\sinais_sistemas\\Processamento Digitais de Sinais\\Aula_13\\Python\\fuzz_acoustic.wav", sample, output_data)
