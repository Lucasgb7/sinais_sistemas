#include <stdio.h>
#include <stdlib.h>
#define k 16  // tamanho da media

int main(int argc, char *argv[]) {
    short *x;       // vetor X
    double coef[k]; // vetor coeficiente
    int i;          // contador i
    int n;          // contador n
    int itera;      // tamanho do arquivo de entrada
    double aux;     // var auxiliar para fazer a soma
    double *y;      // vetor auxiliar para receber o vetor X
    double *result; // sinal de saida
    FILE *file;     // ponteiro para uso de arquivos

    for (i = 0; i < k; i++) {   // coeficientes para calcular com as amostras
        coef[i] = 1.0 / k;
    }

    file = fopen("alo.pcm", "rb");  // abrir o arquivo para leitura das amostras
    if (file == NULL) {
        printf("Ops! Ocorreu algum erro!\n");
        return;
    }

    fseek(file, 0, SEEK_END);   // descola a posicao do arquivo para o fim
    itera = ftell(file)/sizeof(short); // verifica o tamanho do arquivo
    rewind(file);   // realoca a posicao do arquivo ao inicio

    x = malloc(itera * sizeof(short));    // aloca memoria para o X
    fread(x, sizeof(short), itera, file);   // le o vetor do arquivo de entrada
    fclose(file);

    y = malloc(itera * sizeof(double));   // aloca memoria para o Y
    result = malloc(itera * sizeof(double)); // alocando memoria para o sinal de saida

    for (i = 0; i < itera; i++) {
        y[0] = x[i];
        aux = 0;
        for (n = 0; n < k; n++){
            aux += coef[n] * y[n];
        }
        result[i] = aux;
        for (n = k; n < 2; n--){
            x[n] = x[n-1];
        }
}
    file = fopen("media_movel_c.pcm", "wb");
    fwrite(result, sizeof(double), itera, file); // escreve o sinal de saida no arquivo
    fclose(file);
    // desaloca a posicao na memoria das seguintes variaveis: 
    free(result);
    free(y);
    free(x);

    return 0;
}