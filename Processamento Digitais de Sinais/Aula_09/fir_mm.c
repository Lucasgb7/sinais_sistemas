/*
Implementação de um filtro Média Móvel
Lê um arquivo binário com amostras em 16bits
Salva arquivo filtrado também em 16 bits
Walter versão 1.0
 */
#include <stdio.h>
#include <fcntl.h>
#include <io.h>

//#define NSAMPLES 160    // Coef passa-baixa e passa-alta
//#define NSAMPLES 319    // Coef passa-faixa
#define NSAMPLES 637    // Coef equalizador
int main()
{
    FILE *in_file, *out_file;
    int i, n, n_amost;

    short entrada, saida;
    short sample[NSAMPLES] = {0x0};

    float y = 0;

    // Carregando os coeficientes do filtro média móvel
    float coef[NSAMPLES] = {
        //#include "coef_pb.dat"
        //#define SV_FILE_NAME "filtroPB_mm.pcm"
        //#include "coef_pa.dat"
        //#define SV_FILE_NAME "filtroPA_mm.pcm"
        //#include "coef_pf.dat"
        //#define SV_FILE_NAME "filtroPF_mm.pcm"
        #include "equalizador.dat"
        #define SV_FILE_NAME "equalizador_mm.pcm"
    };

    
    /* abre os arquivos de entrada e saida */
    if ((in_file = fopen("white_noise.pcm", "rb")) == NULL)
    {
        printf("\nErro: Nao abriu o arquivo de entrada\n");
        return 0;
    }
    if ((out_file = fopen(SV_FILE_NAME, "wb")) == NULL)
    {
        printf("\nErro: Nao abriu o arquivo de saida\n");
        return 0;
    }

    // zera vetor de amostras
    for (i = 0; i < NSAMPLES; i++)
    {
        sample[i] = 0;
    }

    // execução do filtro
    do
    {

        //zera saída do filtro
        y = 0;

        //lê dado do arquivo
        n_amost = fread(&entrada, sizeof(short), 1, in_file);
        sample[0] = entrada;

        //Convolução e acumulação
        for (n = 0; n < NSAMPLES; n++)
        {
            y += coef[n] * sample[n];
        }

        //desloca amostra
        for (n = NSAMPLES - 1; n > 0; n--)
        {
            sample[n] = sample[n - 1];
        }

        saida = (short)y;

        //escreve no arquivo de saída
        fwrite(&saida, sizeof(short), 1, out_file);

    } while (n_amost);

    //fecha os arquivos de entrada de saída
    fclose(out_file);
    fclose(in_file);
    return 0;
}