#include <stdio.h>

#define NSAMPLE 100

int main() {

    FILE *Far, *Near, *Output;

    if((Far = fopen("far.pcm", "rb")) == NULL){

        printf("\nO arquivo FAR nao abriu");
        return 0;
    }

    if((Near = fopen("near.pcm", "rb")) == NULL){

        printf("\nO arquivo NEAR nao abriu");
        return 0;
    }

    if((Output = fopen("output_eco.pcm", "wb")) == NULL){

        printf("\nO arquivo de saida nao abriu");
        return 0;
    }

    int i;
    float u = 0.002;

    short x_linhan[NSAMPLE] = {0x0};
    float wn[NSAMPLE] = {0x0};
    short Read_Far, Read_Near, ee, y;

    for(i = 0; i < NSAMPLE; i++){

        x_linhan[i] = 0;
        wn[i] = 0;
    }
    // Caminha no tamanho das amostras geradas
    while (fread(&Read_Far, sizeof(short), 1, Far) == 1) {
        
        x_linhan[0] = Read_Far; // amostra inicial
        y = 0;
        // atualiza a saida do FIR
        for (i = 0; i <NSAMPLE; i++) {
            y += x_linhan[i] * wn[i];
        }
        // lê o arquivo NEAR    
        fread(&Read_Near, sizeof(short), 1, Near);

        ee = Read_Near - y; // atualiza erro

        fwrite(&ee, sizeof(short), 1, Output);
        //printf("\t e: %f\n", ee);
        for (i = 0; i < NSAMPLE; i++) {
            wn[i] += u * ee * x_linhan[i];
        }

        for (i = NSAMPLE; i >= 1; i--) {
            x_linhan[i] = x_linhan[i - 1];
        }
    }
    printf("\n---------- RESULTADO ----------\n");
    for(i = 0; i < NSAMPLE; i++)
    {
        printf("W[%d]: %f\n", i, wn[i]);
    }

    fclose(Far);
    fclose(Near);
    fclose(Output);

    return 0;
}