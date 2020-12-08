

short proc_file( short *sample, short *coef, int NSAMPLES )
{
    int n;
    
    int y;	// Variável de 32 bits
    
    short saida_filtr;
    
    
    y =0;
   

    //Convolução e acumulação
        for (n=0; n<NSAMPLES; n++)
        {
         	y += coef[n]*sample[n];
         }

        //desloca o vetor de amostras
        for (n=NSAMPLES-1; n>0; n--)
        {
         	sample[n]=sample[n-1];
         }

		saida_filtr = y>>15;

    return saida_filtr;
}



		
