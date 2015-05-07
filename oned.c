/*
 * main.c
 *
 *  Created on: 7 mai 2015
 *      Author: gabriel
 */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "oned.h"

int main(int argc, char* argv[])
{
	// Initialisation des variables
	float c = 0, x0 = 0;
	double *values = NULL;
	int i = 0, maxiter = 300;
	FILE* wrote_f = NULL;
	values = malloc(maxiter*sizeof(double));
	if(values == NULL)
	{
		exit(0);
	}
	c = strtof(argv[1], NULL);
	x0 = strtof(argv[2], NULL);

	// Calcul de l'orbite
	values[0] = x0;
	for(i = 1 ; i <= maxiter ; i++)
	{
		values[i] = quadratic_c(c, values[i - 1]);
	}

	// Ecriture dans le fichier
	wrote_f = fopen("orbit", "w");
	if(wrote_f == NULL)
	{
		printf("Erreur d'ouverture fichier");
	}
	else
	{
		fprintf(wrote_f,"#orbite de %f, fonction quadratique %fx(1-x)\n", x0, c);
		for(i = 0 ; i <= 300 ; i++)
		{
			fprintf(wrote_f, "%f\n", values[i]);
		}
		fclose(wrote_f);
	}
	free(values);


	return 0;
}

double quadratic_c(float c, double x)
{
	return c*x*(1-x);
}


