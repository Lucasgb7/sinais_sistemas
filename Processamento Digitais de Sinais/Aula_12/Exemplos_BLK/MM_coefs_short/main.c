/* programa para testes com arquivos
-- Lendo arquivo de entrada
-- Processa
-- Gera arquivo de saida
-- walter 1.0 
*/

#include <stdio.h>
#include <string.h>





#define NSAMPLES       8	// Tamanho da média




extern short proc_file( short *, short *, int);

int main(int argc,char *argv[])
{
    
	FILE *fin,*fout;

  	short entrada;
  	short saida;
  
  	short sample[NSAMPLES] = {0x0}; //  Vetor de amostras
  	
  	 //Carregando os coeficientes do filtro média móvel
   
   	short coef[NSAMPLES]={
   				#include "coefs_mm_8.dat"
   };
	
	int i;
	
	printf("***************************************************************\n");
	printf("* TESTE COM ARQUIVOS					           		      *\n");
	printf("*                                                             *\n");
	printf("***************************************************************\n");
	printf("\n");
	
	
	fin = fopen("..\\sweep_100_2k.pcm","rb");
    	if ((fin)==NULL)
  	{
    		printf("\nErro: nao abriu o arquivo de Entrada\n");
    		return 0;
  	}
    fout = fopen("..\\sai_MM_tst.pcm","wb");
    	if ((fout)==NULL)
  	{
    		printf("\nErro: nao abriu o arquivo de Saida\n");
    		return 0;
  	}

  	
  printf("Processando ... ");

  while (fread(&entrada,sizeof(short),1,fin) == 1) 
  {
  	
  		sample[0] = entrada;

		saida = proc_file( sample, coef, NSAMPLES);

		
		fwrite(&saida,sizeof(short),1,fout);	
	
	
	}

    printf("terminado!\n");
		
    
	
		fclose(fin);
		fclose(fout);
		
    return 0;
}


