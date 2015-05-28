#include "bif_diag.h"

int main(int argc, char* argv[])
{
    double **array_bif = NULL;
    //double *array_bif = NULL;
    double *orbit = NULL;
    int i = 0 ,j = 0,n_iter = 0;
    float c = 0;
    double x0 = 0.23748;
    char *fname = NULL;
    FILE* wrote_f = NULL;
    orbit = malloc(ITER_BIF*sizeof(double));
    if(orbit == NULL)
    {
        printf("Error initializing orbit\n");
        exit(0);
    }
    printf("Init OK\n");
    /* On essaie d'abord la fonction
     * quadratique avec 0<c<4 */
    // On définit le pas
    n_iter = (int)(4 - 0)/0.5;
    printf("%d", n_iter);
    array_bif = malloc(n_iter*ITER_BIF*sizeof(double));
    if(array_bif == NULL)
    {
        printf("Error initializing array\n");
        exit(0);
    }
    printf("Array OK\n");
    for(i = 0 ; i <= n_iter ; i++)
    {
        memset(orbit, 0, ITER_BIF*sizeof(double));
        orbit[0] = x0;
        calculate_orbit(orbit, c, quadratic_c);
        array_bif[i] = orbit;
        c = c + (4 - 0)/0.5;
    }
    printf("Calcul OK\n");
    // Writing file
    fname = malloc(12*sizeof(char));
    sprintf(fname, "bif_diag_%0.3f", x0);
    wrote_f = fopen(fname, "w");
    printf("Ouverture OK\n");
    if(wrote_f == NULL)
    {
        printf("Error opening file");
        exit(0);
    }
    else
    {
        fprintf(wrote_f, "#Diagramme de bifurcation\n");
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
