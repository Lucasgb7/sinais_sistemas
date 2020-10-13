import numpy as np
import matplotlib.pyplot as plt
"""
Projeto e implementação do filtro IIR
Obter a função de transferencia H[z]de um filtro passa-alta.
• Plotar os pólos e zeros
• Implementar um programa para executar a equação diferença do filtro.
• Validar essa implementação com um sinal de entrada de sweep.
"""
input_buf = np.zeros(3)
out_buf = np.zeros(2)
Fc = 1000
Fs = 8000   # Amostra

wc = 2*np.pi*Fc

# F' (F linha)
F1 = 2 * Fs

# Coeficientes para equação
a = F1 / (F1 + wc)
b = (2 * wc) / (F1 + wc)
c = (F1 - wc) / (F1 + wc)

print("Coeficiente A:", a)
print("Coeficiente B:", b)

with open('C:\\Users\\lucas\\Desenvolvimento\\sinais_sistemas\\Processamento Digitais de Sinais\\Aula_07\\Sweep10_3600.pcm', 'rb') as f:
    buf = f.read()
    data_i = np.frombuffer(buf, dtype='int16')
    data_len = len(data_i)

    # Arquivo cópia para salvar o resultado lido
    data_o = np.zeros_like(data_i)

    for i in range(data_len):
        input_buf[0] = data_i[i]

        m = (a * input_buf[0]) - (a * input_buf[2]) - (b * out_buf[0]) + (c * out_buf[1])

        out_buf[1:len(out_buf)] = out_buf[0:len(out_buf)-1]
        out_buf[0] = m

        data_o[i] = m
        input_buf[1:len(input_buf)] = input_buf[0:len(input_buf) - 1]

# 100ms
t = np.arange(0, data_len/Fs, 1 / Fs)

plt.stem(t, data_i[: len(t)], "k-", "ko", "k-", label="Input")
plt.plot(t, data_o[: len(t)], label="Output")
plt.legend()
plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude")
plt.show()


file_name = "C:\\Users\\lucas\\Desenvolvimento\\sinais_sistemas\\Processamento Digitais de Sinais\\Aula_07\\passaAlta_output.pcm"
with open(file_name, 'wb') as f:
    for d in data_o:
        f.write(d)