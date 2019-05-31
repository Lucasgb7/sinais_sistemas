import numpy as np
import matplotlib.pyplot as plt

fs = 1600
ts = 1/fs
t = np.arange(0, 2, 0.1)
fim = 0
resultado = 0

while (fim != 1) :
    print("Qual a funcao deseja verificar? Entre com: ")
    print(" 1, para f_1(t)")
    print(" 2, para f_2(t)")
    print(" 3, para sair do programa")
    opcao = int(input("Opção: "))

    if (opcao == 1):
        f1_t = np.cos(((2*np.pi)*200)*t)+ np.cos(((2*np.pi)*400)*t)
        plt.plot(t, f1_t)
        plt.ylabel('f_1t)')
        plt.xlabel('t')
        plt.title('f1_t')
        plt.grid(True)
        plt.show()

    if (opcao == 2):
        print("Opcao digitada foi: " + str(opcao))
    if (opcao == 3): 
        fim = 1
        resultado = 0
        print("Fim do programa")

print(resultado)