void proc_file( short *sai, short *entr, int N )
{
    int i;
   

    for( i=0; i<N; i++ ) 
    {
		sai[i] = entr[i]/2;	
	}

    return;
}