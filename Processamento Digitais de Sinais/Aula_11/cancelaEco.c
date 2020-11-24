#include <stdio.h>

#define NSAMPLE 320     // Nº de Amostras

int main()
{
    FILE *Far, *Near, *Output;

    if ((Far = fopen("far.pcm", "rb")) == NULL)
    {

        printf("\nO arquivo FAR nao abriu");
        return 0;
    }

    if ((Near = fopen("near.pcm", "rb")) == NULL)
    {

        printf("\nO arquivo NEAR nao abriu");
        return 0;
    }

    if ((Output = fopen("output_eco.pcm", "wb")) == NULL)
    {

        printf("\nO arquivo de saida nao abriu");
        return 0;
    }

    int samples, i, j = 0;
    float u = 0.000000000005;    // Taxa de aprendizado

    short x[NSAMPLE] = {0x0};   // Entrada do sitema (x[n])
    short w[NSAMPLE] = {0x0};   // Coeficientes (w[n])
    // Entradas FAR e NEAR, Taxa de erro, Saida do filtro
    short inputFar, inputNear, error, y, short_output;

    for (i = 0; i < NSAMPLE; i++)
    {
        x[i] = 0;
        w[i] = 0;
    }
    // Caminha no tamanho das amostras geradas
    do{
        y = 0;
        samples = fread(&inputFar, sizeof(short), 1, Far);
        x[0] = inputFar;

        // Amostra FAR convolui com o filtro adaptativo 
        for (i = 0; i < NSAMPLE; i++)
        {
            y += w[i] * x[i];   // Filtragem: y[n] = w[n] * x[n]
        }
        fread(&inputNear, sizeof(short), 1, Near);  // Planta já conhecida
        error = inputNear - y;

        /*
        if(j % 30 == 0)
        {
            printf("Amostra[%d]\t->\t", j);
            printf("e: %f\n", error);
        }
        j++;
        */

        // Atualiza novos valores de coeficientes
        for (i = 0; i < NSAMPLE; i++)
        {
            w[i] += 2 * u * error * x[i];
        }
        // Deslocamento da amostra
        for (i = NSAMPLE; i >= 1; i--)
        {
            x[i] = x[i - 1];
        }
        short_output = (short) error;   // Caso não seja feito, o valor não é lido corretamente   
        fwrite(&short_output, sizeof(short), 1, Output);


    }while(samples);

    /*
    while (fread(&inputFar, sizeof(short), 1, Far) == 1) // equanto não acabar as amostras
    {   
        x[0] = inputFar;    // amostra inicial
        y = 0;              // inicializa saida FIR = 0 
        // atualiza a saida do FIR
        for (i = 0; i < NSAMPLE; i++)
        {
            y += w[i] * x[i];   // Filtragem: y[n] = w[n] * x[n]
        }
        // começa leitura do arquivo NEAR
        fread(&inputNear, sizeof(short), 1, Near);

        error = inputNear - y; // atualiza erro
        short_output = (short) error;

        if(j % 30 == 0)
        {
            printf("Amostra[%d]\t->\t", j);
            printf("e: %f\n", error);
        }
        
        for (i = 0; i < NSAMPLE; i++)
        {
            w[i] += 2 * u * error * x[i];
        }
        // Deslocamento da amostra
        for (i = NSAMPLE; i >= 1; i--)
        {
            x[i] = x[i - 1];
        }
        fwrite(&short_output, sizeof(short), 1, Output);
        j++;
    }
    
    printf("\n---------- RESULTADO ----------\n");
    for (i = 0; i < NSAMPLE; i++)
    {
        printf("W[%d]: %f\n", i, w[i]);
    }
    */
    fclose(Far);
    fclose(Near);
    fclose(Output);

    return 0;
}