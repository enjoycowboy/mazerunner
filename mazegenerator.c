#include <stdio.h>
#include <math.h>
#include <stdlib.h>

//declaração explícita

int runMaze(char mazeItself)
;ngisnt generateMaze(int seed);
void main (void);

// fluxo de execução: 
// gera numero aleatório de seed, gera o maze 
// spawna o thread, corre o maze, repete

char main (char mazeItself){
	int rndm = rand();
	int seed = rndm % 1000;
	printf ("seed generated = %d \n", seed);
	printf ("################################# \n");
	generateMaze(seed);
	printf ("generating maze");

	for (int i = 0; i<= seed; i++)
	{
		for (int j=0; j<=seed; i++)
		{
			printf ("|%d|", mazeItself[i][j]);
		}
		printf("\n");
	}

}

int generateMaze(int seed){
	char mazeItself[seed][seed];

	
	for (int i = 0; i<= seed; i++)	//primeiro enche o labirinto de ~parede
	{
		for (int j=0; j<=seed; i++)
		{
			mazeItself[i][j] = "X";
		}
	}

	return mazeItself[][];
	/*
	Legenda para geração do maze
	X = parede
	O = caminho não visitado
	P = caminho visitado
	Y = entrada
	Z = saída
	*/

}
