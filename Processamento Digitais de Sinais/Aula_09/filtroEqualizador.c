/* Implementação de um filtro Média Móvel 
Lê um arquivo binário com amostras em 16bits
Salva arquivo filtrado também em 16 bits
Walter versão 1.0 
 */
#include <stdio.h>
#include <fcntl.h>
#include <io.h>


#define NSAMPLES 160    // Coef passa-baixa e passa-alta
//#define NSAMPLES 319    // Coef passa-faixa

int main()
{
   FILE *in_file, *out_file;
   int i, n, n_amost;
  
   short entrada, saida;
   short sample[NSAMPLES] = {0x0};

   float ouputPF=0, ouputPA = 0, ouputPB = 0, ouput_aux = 0; 
   float gPB = 0.7 , gPA = 0.5, gPF = 0.6;
/*
   printf("Qual o Ganho para o Passa Baixa?\n");
   scanf("%f", &fatorPassaBaixa);

   printf("Qual o Ganho para o Passa Alta?\n");
   scanf("%f", &fatorPassaAlta);

   
   printf("Qual o Ganho para o Passa Faixa?\n");
   scanf("%f", &fatorPassaFaixa);
*/
   //Carregando os coeficientes do filtro média móvel
   
   float coef_PF[NSAMPLES]={
   				#include "coef_pf.dat"
   };

   float coef_PA[NSAMPLES] ={
                #include "coef_pa.dat"
   };

   float coef_PB[NSAMPLES]={
                #include "coef_pb.dat"
   };
  
 
    /* abre os arquivos de entrada e saida */
  if ((in_file = fopen("sweep_3800.pcm","rb"))==NULL)
  {
    printf("\nErro: Nao abriu o arquivo de entrada\n");
    return 0;
  }
  if ((out_file = fopen("equalizador_mm.pcm","wb"))==NULL)
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
        ouput_aux = 0;
        ouputPF = 0;
        ouputPA = 0;
        ouputPB = 0;

        //lê dado do arquivo
        n_amost = fread(&entrada,sizeof(short),1,in_file);
				sample[0] = entrada;

            //Convolução e acumulação do Filtro Passa Faixa
            for (n=0; n<NSAMPLES; n++)
            {
                ouputPF += coef_PF[n]*sample[n];
            }
            
            //Convolução e acumulação do Filtro Passa Alta
            for (n=0; n<NSAMPLES; n++)
            {
                ouputPA += coef_PA[n]*sample[n];
            }
        
            //Convolução e acumulação do Filtro Passa Baixa
            for (n=0; n<NSAMPLES; n++)
            {
                ouputPB += coef_PB[n]*sample[n];
            }

        //desloca amostra
        for (n=NSAMPLES-1; n>0; n--)
                {
                sample[n]=sample[n-1];
                }

                ouput_aux = (ouputPB * gPB) + (ouputPA * gPA) + (ouputPF * gPF);
				saida = (short) ouput_aux;

        //escreve no arquivo de saída
        fwrite(&saida,sizeof(short),1,out_file);

 } while (n_amost);


   //fecha os arquivos de entrada de saída
   fclose(out_file);
   fclose(in_file);
   return 0;
}