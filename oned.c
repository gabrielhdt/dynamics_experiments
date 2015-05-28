/*
*  Copyright 2015 <gabriel gabrielhondet@gmail.com>
*  
*  This program is free software; you can redistribute it and/or modify
*  it under the terms of the GNU General Public License as published by
*  the Free Software Foundation; either version 2 of the License, or
*  (at your option) any later version.
*  
*  This program is distributed in the hope that it will be useful,
*  but WITHOUT ANY WARRANTY; without even the implied warranty of
*  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
*  GNU General Public License for more details.
*  
*  You should have received a copy of the GNU General Public License
*  along with this program; if not, write to the Free Software
*  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
*  MA 02110-1301, USA.
*  
*/  
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "oned.h"

int main(int argc, char* argv[])
{
    if(argc <= 2)
    {
        printf("Orbit calculator , Copyright (C) 2015 Gabriel Hondet\n");
        printf("Orbit calculator comes with ABSOLUTELY NO WARRANTY; for details type `show w'.\n");
        printf("This is free software, and you are welcome to redistribute it\n");
        printf("under certain conditions; type `show c' for details.\n");
        printf("Missing arguments : indicate first function parameter then initial point");
        exit(0);
    }
	// Initialisation of variables
	float c = 0, x0 = 0;
	double *values = NULL;
	int i = 0, maxiter = 300;
	char *fname = NULL;
	FILE* wrote_f = NULL;
	// Creation of the array containing orbit
	values = malloc(maxiter*sizeof(double));
	if(values == NULL)
	{
		exit(0);
	}
	// Name of the file we will write : o_c-x0
	fname = malloc(13*sizeof(char));
	c = strtof(argv[1], NULL);
	x0 = strtof(argv[2], NULL);
	sprintf(fname, "o_%0.3f-%0.3f", c, x0);

	// Calculation of the orbit
	values[0] = x0;
	calculate_orbit(values, maxiter, c, quadratic_c);

	// Writing
	wrote_f = fopen(fname, "w");
	if(wrote_f == NULL)
	{
		printf("Erreur d'ouverture fichier");
	}
	else
	{
		fprintf(wrote_f,"#%f orbit", x0);
		for(i = 0 ; i <= maxiter ; i++)
		{
			fprintf(wrote_f, "%f\n", values[i]);
		}
		fclose(wrote_f);
	}
	free(values);

	return 0;
}

void calculate_orbit(double *values, int maxiter, float c, double (*F)(float, double))
{
	int i = 0;
	for(i = 1 ; i <= maxiter ; i++)
	{
		values[i] = F(c, values[i - 1]);
	}

}

double quadratic_c(float c, double x)
{
	return c*x*(1-x);
}
