/*
*  Copyright 2015 Gabriel Hondet <gabrielhondet@gmail.com>
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
/*
 * Ce programme crée le diagramme de bifurcation, illustrant la
 * period doubling route to chaos de la fonction quadratique.
 * Il calcule l'orbite d'un x0 (500 premiers points) en faisant
 * varier le paramètre c de la fonction Qc(x) = cx(1-x)
 */
#include "bif_diag.h"
int main(int argc, char* argv[])
{
    double *orbit = NULL;
    int i = 0 ,j = 0,n_iter = 0, n_c = 100;
    float c = 0, c_min = 0, c_max = 4, pas = 0;
    double x0 = 0.23748;
    char *fname = NULL;
    FILE* wrote_f = NULL;
    orbit = malloc(ITER_BIF*sizeof(double));
    if(orbit == NULL)
    {
        printf("Error initializing orbit\n");
        exit(0);
    }
    fname = malloc(12*sizeof(char));
    sprintf(fname, "bif_diag_%0.3f", x0);
    wrote_f = fopen(fname, "w");
    if(wrote_f == NULL)
        exit(0);
    else
        fprintf(wrote_f, "#Diagramme de bifurcation");

    /* On essaie d'abord la fonction
     * quadratique avec 0<c<4
     * On définit le nombre de valeurs de c
     * pas = étendue/ nombre de valeurs*/
    pas = fabsf(c_max - c_min)/n_c;
    printf("%f\n", pas);
    n_iter = 100;
    for(i = 0 ; i <= n_iter ; i++)
    {
        memset(orbit, 0, ITER_BIF*sizeof(double));
        orbit[0] = x0;
        calculate_orbit(orbit, c, quadratic_c);
        fprintf(wrote_f, "\n%0.3f:", c);
        // We don't plot the first 100 points
        for(j = 100 ; j <= ITER_BIF ; j++)
        {
            fprintf(wrote_f, "%f;", orbit[j]);
        }
        c += pas;
    }
    free(orbit);
    fclose(wrote_f);

    return 0;
}

void calculate_orbit(double *values, float c, double (*F)(float, double))
{
    int i = 0;
    for(i = 1 ; i <= ITER_BIF ; i++)
    {
        values[i] = F(c, values[i - 1]);
    }

}

double quadratic_c(float c, double x)
{
    return c*x*(1 - x);
}
