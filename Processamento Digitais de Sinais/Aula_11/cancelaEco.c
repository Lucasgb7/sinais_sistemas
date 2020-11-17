#include <stdio.h>

#define NSAMPLE 900000     // Nº de Amostras

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

    int i, j = 0;
    float u = 0.002;    // taxa de aprendizado

    short x[NSAMPLE] = {0x0};   // Entrada do sitema (x[n])
    float w[NSAMPLE] = {0x0};  // Coeficientes (w[n])
    // Entradas FAR e NEAR, Taxa de erro, Saida do filtro
    short inputFar, inputNear, error, y;

    for (i = 0; i < NSAMPLE; i++)
    {
        x[i] = 0;
        w[i] = 0;
    }
    // Caminha no tamanho das amostras geradas
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

        fwrite(&error, sizeof(short), 1, Output);

        if(j % 100000 == 0)
        {
            printf("Amostra[%d]\t->\t", j);
            printf("e: %f\n", error);
        }
        
        for (i = 0; i < NSAMPLE; i++)
        {
            w[i] += u * error * x[i];
        }

        for (i = NSAMPLE; i >= 1; i--)
        {
            x[i] = x[i - 1];
        }
        j++;
    }
    /*
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