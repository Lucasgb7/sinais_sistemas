#include <stdio.h>
#include <fcntl.h>
#include <io.h>

int main()
{
    int tam = 0, i;
    int d1 = 3200; //distancia 1
    int d2 = 4800; //distancia 2
    short entrada, saida;

    float p0 = 0.6; //peso principal
    float p1 = 0.3; //peso do 1 eco
    float p2 = 0.1; //peso do 2 eco
    
    FILE *in_file, out_file; 
    if ((in_file = fopen("sweep_100_2k.pcm", "rb")) == NULL) // Abrindo o arquivo de entrada
    {
        printf("\nErro: Nao abriu o arquivo de entrada\n");
        return 0;
    }

    if ((out_file = fopen("resultado_eco.pcm", "wb")) == NULL) // Criando o arquivo de saida com o nome alterado
    {
        printf("\nErro: Nao abriu o arquivo de saida\n");
        return 0;
    }

    while (fread(&entrada, sizeof(short), 1, in_file) > 0) // Calculando o tamanho do arquivo
    {
        tam++;
    }
    rewind(in_file); // Enviando cursor para o inicio do arquivo

    short Value = 0;
    float data[tam];

    for (i = 0; i < tam; i++)
    {

        fread(&entrada, sizeof(short), 1, in_file); // entrada recebe dado na posicao do cursor
        data[i] = entrada;                          //dado = entrada
        Value = data[i] p0;                         //eco recebe datapeso

        if (i >= d1 && i >= d2)
            Value = data[i] p0 + (data[i - d1] p1) + (data[i - d2] p2);

        fwrite(&Value, sizeof(short), 1, out_file);
        Value = 0;
    }

    fclose(out_file); // Fechando os arquivos
    fclose(in_file);  // Fechando os arquivos
    return 0;
}