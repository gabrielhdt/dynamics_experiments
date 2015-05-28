#include "bif_diag.h"

int main(int argc, char* argv[])
{
    double **array_bif = NULL;
    double orbit[ITER_BIF];
    int i = 0 ,j = 0,n_iter = 0;
    float c = 0, x0 = 0.324543;
    char *fname = NULL;
    FILE* wrote_f = NULL;
    if(orbit == NULL)
    {
        exit(0);
    }
    /* On essaie d'abord la fonction
     * quadratique avec 0<c<4 */
    n_iter = (int)(4 - 0)/200;
    array_bif = malloc(n_iter*ITER_BIF*sizeof(double));
    for(i = 0 ; i <= n_iter ; i)
    {
        calculate_orbit(array_bif[i], c, quadratic_c);
    }
    // Writing file
    sprintf(fname, "bif_diag_%0.3f", x0);
    wrote_f = fopen(fname, "w");
    if(wrote_f = NULL)
    {
        printf("Error opening file");
        exit(0);
    }
    else
    {
        fprintf(wrote_f, "#Diagramme de bifurcation");
        for(i = 0 ; i <= n_iter; i++)
        {
           for(j = 0; j <= ITER_BIF ; j++)
           {
              fprintf(wrote_f, "%f/", array_bif[i][j]);
           }
          fprintf(wrote_f, "\n");
        }
    }
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
