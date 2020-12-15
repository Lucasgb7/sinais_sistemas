
import numpy as np

def sign(x):
    aux = np.zeros_like(x, dtype="int16")
    for i in range(len(x)):
        if x[i] > 0:

            aux[i] = 1

        elif x[i] == 0:

            aux[i] = 0
        else:

            aux[i] = -1

    return aux


def fuzz(input, ganho, mix):
    q = input * ganho / max(abs(input))
    z = sign(-q) * (1-np.exp(sign(q)*q))
    y = mix * z * max(abs(input)) / max(abs(z)) + (1-mix) * input
    output = y * max(abs(input)) / max(abs(y))
    return output




if __name__ == "__main__":

    # Le o arquivo
    with open ("C:\\Users\\lucas\\Desenvolvimento\\sinais_sistemas\\Processamento Digitais de Sinais\\Aula_13\\Python\\acoustic.pcm", "rb") as input_f:
        buf = input_f.read ()
        data = np.frombuffer (buf, dtype = 'int16') 


    ganho = 1.5
    mix = 1

    output_data = fuzz(data, ganho, mix)
    print(output_data)

    # Escreve no arquivo
    with open("C:\\Users\\lucas\\Desenvolvimento\\sinais_sistemas\\Processamento Digitais de Sinais\\Aula_13\\Python\\fuzz_out.pcm", "wb") as output:
        for x in output_data:
            output.write(x)
    output.close()