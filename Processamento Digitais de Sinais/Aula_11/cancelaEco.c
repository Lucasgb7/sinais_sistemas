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
    float u = 0.0000000000005;    // Taxa de aprendizado

    short x[NSAMPLE] = {0x0};   // Entrada do sitema (x[n])
    double w[NSAMPLE] = {0x0};   // Coeficientes (w[n])
    // Entradas FAR e NEAR, Taxa de erro, Saida do filtro
    short inputFar, inputNear, short_output;
    double y = 0.0, error = 0.0;

    for (i = 0; i < NSAMPLE; i++)
    {
        x[i] = 0.0;
        w[i] = 0.0;
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
        for (i = NSAMPLE-1; i > 0; i--)
        {
            x[i] = x[i - 1];
        }
        short_output = (short) error;   // Caso não seja feito, o valor não é lido corretamente   
        fwrite(&short_output, sizeof(short), 1, Output);


    }while(samples);
    printf("\nFinalizado");
    fclose(Far);
    fclose(Near);
    fclose(Output);

    return 0;
}