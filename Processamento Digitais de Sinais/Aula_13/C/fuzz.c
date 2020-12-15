#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define N 107972

// Equivalente a função sign() do MATLAB
short sign(short x)
{
    if (x > 0)
    {
        return 1;
    } else if (x == 0)
    {
        return 0;
    } else
    {
        return -1;
    }   
}

// Pega o valor máximo da array
short getMax(short x[N])
{
    short max = 0;
    for (int i = 0; i < N; i++)
    {
        if (abs(x[i]) > max)
        {
            max = abs(x[i]);
        }
    }
    return max;
}

// Pega o valor máximo da array (float)
float getMaxFloat(float x[N])
{
    float max = 0;
    for (int i = 0; i < N; i++)
    {
        if (fabsf(x[i]) > max)
        {
            max = fabsf(x[i]);
        }
    }
    return max;
}

/* Funcao nao linear:
f(x) = (x / |x|) (1 - e ^ (g * x^2 / |x|))
    - x: amostra
    - g: ganho
*/
void fuzzexp(short x[N], short y[N], float gain, float mix)
{
    float q[N], z[N];
    int i;
    short max_x = getMax(x);
    for (i = 0; i < N; i++)
    {
        q[i] = 0;
        q[i] = (float) (x[i] * gain / max_x);
        z[i] = sign(-q[i]) * (1 - exp(sign(-q[i]) * q[i]));
        if (i == 0){
            printf("\nQ[0]: %f = \t%d * %f / %d", q[i], x[i], gain, max_x);
            printf("\nZ[%d]: %f", i, z[i]);
        }
        if (i % 10000 == 0)
        {
            printf("\nZ[%d]: %f", i, z[i]);
        }
    }
    float max_z = getMaxFloat(z);
    for (i = 0; i< N; i++)
    {
        y[i] = mix * z[i] * max_x / max_z + (1 - mix) * x[i];
        if (i == 0){
            printf("\nY[0]: %d : \t %f * %f * %d / %f + (1 - %f) * %d", y[i], mix, z[i], max_x, max_z, mix, x[i]);
        }
    }
    short max_y = getMax(y);
    for (i = 0; i< N; i++)
    {
        y[i] = y[i] * max_x/max_y;
        if (i % 10000 == 0){
           printf("\ny[%d]: %d", i, y[i]);
        }
    }
}

/*
void fuzzexp1(short x[N], short y[N], float gain, float mix)
{
    float q[N], z[N];
    int i;
    short max_x = getMax(x);
    printf("\nmax_x: %d", max_x);
    for (i = 0; i < N; i++)
    {
        q[i] = 0;
        q[i] = (float) (x[i] / abs(x[i]));
        
        if (i == 1){
            printf("\nQ[i]: %d = \t%d * %f / %d", i, q[i], x[i], gain, max_x);
            printf("\nZ[%d]: %d", i, z[i]);
        }
    }
    float max_z = getMaxFloat(z);
    for (i = 0; i< N; i++)
    {
        y[i] = q[i] * (1 - exp(gain*(q[i] * x[i])));
    }
    short max_y = getMax(y);
    for (i = 0; i< N; i++)
    {
        y[i] = (short) (mix * y[i] + (1 - mix)*x[i]);
    }
}
*/


int main(){

    FILE *Data_in, *Data_out;

    if((Data_in = fopen("acoustic.pcm", "rb")) == NULL){
        printf("O arquivo de entrada nao abriu\n");
        return 0;
    }

    if((Data_out = fopen("out_fuzzexp1.pcm", "wb")) == NULL){

        printf("O arquivo de saida nao abriu\n");
        return 0;
    }
    float gain = 11;
    float mix = 1;
    short input[N], output[N];
    short sample[N];
    int sampleN;
    short inputShort;

    for (int i = 0; i < N; i++)
    {
        input[i] = 0.0;
        output[i] = 0.0;
        sample[i] = 0.0;
    }

    int j = 0;
    do{
        sampleN = fread(&inputShort, sizeof(short), 1, Data_in);
        sample[j] = inputShort;
        if (j % 10000 == 0){
            printf("\nAmostra[%d]: %d", j, sample[j]);
        }
        j++;
    }while(sampleN);

    printf("\nMe mata");
    fuzzexp(sample, output, gain, mix);

    for (int i = 0; i < N; i++)
    {
        if (i % 10000 == 0){
           printf("\ny[%d]: %d", i, output[i]);
        }
        fwrite(&output[i], sizeof(short), 1 , Data_out);
    }

    fclose(Data_in);
    fclose(Data_out);
    return 0;
}