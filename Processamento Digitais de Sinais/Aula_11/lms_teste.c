#include <stdio.h>
//#define N 4
#define N 160

int main(){

    FILE *Data_in, *Data_out;

    if((Data_in = fopen("white_noise.pcm", "rb")) == NULL){

        printf("O arquivo de entrada nao abriu\n");
        return 0;
    }

    if((Data_out = fopen("saida_lms.pcm", "wb")) == NULL){

        printf("O arquivo de saida nao abriu\n");
        return 0;
    }

    double u = 0.000000000005; // Taxa de aprendizado
    int i, sampleN;             // Contador, Nº de amostras
    double wn[N];               // Coeficiente adaptados
    double y = 0.0;             // Saída do filtro adaptativo
    double d = 0.0;             // Coeficientes desejados
    double error;               // Erro 
    // Amostras, entrada, saida e erro em short
    short sample[N], input, output, shortError;

    for(i = 0; i < N; i++)
    {
        wn[i] = 0.0;
        sample[i] = 0.0;
    }

    // Definindo a planta

/*     float Wo[]={
   				#include "coef_pb.dat"
    }; */

    
    float Wo[]={
   				#include "coef_pa.dat"
    };
    
    /* double Wo[] = {0.5, 0.3, -0.5, 0.8}; */

    do{
        d = 0;
        y = 0;
        // Lendo a amostra de entrada
        sampleN = fread(&input, sizeof(short), 1, Data_in);
        sample[0] = input;   // Entrada

        // Convolução de y(n) da entrada com o vetor de coeficientes atualizados
        for(i = 0; i < N; i++)
        {
            y += sample[i] * wn[i];
        }

        // d(n) = convolução da entrada com o sistema desconhecido
        for(i = 0; i < N; i++)
        {
            d += sample[i] * Wo[i];
        }

        // Calculo do erro e(n) = d(n) - y(n)
        // Diferença entre saída do sistema desconhecido e o filtro adaptativo
        error = d - y;

        // Atualizando os coeficientes do filtro usando LMS
        for(i = 0; i < N; i++)
        {
            wn[i] += 2 * u * error * sample[i];   // Sinal de erro retorna ao filtro, e calcula novos coeficientes
        }
        // Atualizando o vetor x_linhan (DESLOCAMENTO)
        for(i = N; i >= 1; i--)
        {
            sample[i] = sample[i-1];
        }

        shortError = (short) error;
        //shortError = (short) y;

        fwrite(&shortError, sizeof(short), 1, Data_out);
        //printf("\t e: %f\n", ee);

    }while(sampleN);

    printf("\n---------- RESULTADO ----------\n");
    for(i = 0; i < N; i++)
    {
        printf("W[%d]: %f\n", i, wn[i]);
    }

    fclose(Data_in);
    fclose(Data_out);

    return 0;
}
