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

int main()
{
	// Initialisation des variables
	double c = 4, x0 = 0.321;
	double result[300] = {0};
	int i = 0;
	FILE* wrote_f = NULL;

	// Calcul de l'orbite
	result[0] = x0;
	for(i = 1 ; i <= 300 ; i++)
	{
		result[i] = quadratic_c(c, result[i - 1]);
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
			fprintf(wrote_f, "%f\n", result[i]);
		}
		fclose(wrote_f);
	}

	return 0;
}

double quadratic_c(double c, double x)
{
	return c*x*(1-x);
}


