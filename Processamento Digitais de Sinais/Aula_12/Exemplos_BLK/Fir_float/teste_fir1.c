/* Implementação de um filtro FIR 
Lê um arquivo binário com amostras em 16bits
Salva arquivo filtrado também em 16 bits
Walter versão 1.0 
 */
#include <stdio.h>
//#include <fcntl.h>
//#include <io.h>
#include <cycles.h>


#define NSAMPLES       58

int main()
{
  	cycle_stats_t stats;
	FILE *in_file, *out_file;
   int i, n, n_amost;
  
   short entrada, saida;
   short sample[NSAMPLES] = {0x0};

   float y=0;

   //filtro passa-baixas fc=200Hz
   
   float coef[NSAMPLES]={
   -0.0055,
  -0.0020,
  -0.0085,
  -0.0114,
  -0.0083,
  -0.0008,
   0.0083,
   0.0166,
   0.0216,
   0.0217,
   0.0164,
   0.0076,
  -0.0008,
  -0.0047,
  -0.0019,
   0.0063,
   0.0153,
   0.0182,
   0.0096,
  -0.0122,
  -0.0433,
  -0.0742,
  -0.0933,
  -0.0902,
  -0.0610,
  -0.0099,
   0.0509,
   0.1051,
   0.1368,
   0.1368,
   0.1051,
   0.0509,
  -0.0099,
  -0.0610,
  -0.0902,
  -0.0933,
  -0.0742,
  -0.0433,
  -0.0122,
   0.0096,
   0.0182,
   0.0153,
   0.0063,
  -0.0019,
  -0.0047,
  -0.0008,
   0.0076,
   0.0164,
   0.0217,
   0.0216,
   0.0166,
   0.0083,
  -0.0008,
  -0.0083,
  -0.0114,
  -0.0085,
  -0.0020,
  -0.0055};
  
 
  // inicializando a estrutura de cycles
  CYCLES_INIT(stats);
   /* abre os arquivos de entrada e saida */
  if ((in_file = fopen("..//sweep_100_2k.pcm","rb"))==NULL)
  {
    printf("\nErro: Nao abriu o arquivo de entrada\n");
    return 0;
  }
  if ((out_file = fopen("..//sai_sweep.pcm","wb"))==NULL)
  {
    printf("\nErro: Nao abriu o arquivo de saida\n");
    return 0;
  }

   // zera vetor de amostras
   for (i=0; i<NSAMPLES; i++)
        {
        sample[i]=0;
        }

   // execução do filtro
 do {
        
 		
	   //zera saída do filtro
        y=0;

        //lê dado do arquivo
        n_amost = fread(&entrada,sizeof(short),1,in_file);
		CYCLES_START(stats);
        sample[0] = entrada;

        //Convolução e acumulação
        for (n=0; n<NSAMPLES; n++)
                {
                y += coef[n]*sample[n];
                }

        //desloca amostra
        for (n=NSAMPLES-1; n>0; n--)
                {
                sample[n]=sample[n-1];
                }

		saida = (short) y;
		CYCLES_STOP(stats);

        //escreve no arquivo de saída
        fwrite(&saida,sizeof(short),1,out_file);

 } while (n_amost);
 
 	CYCLES_PRINT(stats);


   //fecha os arquivos de entrada de saída
   fclose(out_file);
   fclose(in_file);
   return 0;
}
