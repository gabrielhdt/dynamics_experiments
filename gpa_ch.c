#include "gpa_ch.h"

int main(int argc, char* argv[])
{
    int gpa_size = 1000000, c, i;
    double *points_quad = NULL;
    int *gpa_tab = NULL;
    FILE* wrote_f = NULL;
    gpa_tab = malloc(gpa_size*sizeof(int));
    points_quad = malloc(gpa_size*sizeof(double));

    // Conditions initiales et paramètres
    points_quad[0] = 0.3;
    c = 4;

    // Calcul de l'orbite
    for(i = 1 ; i <= gpa_size ; i++)
    {
        points_quad[i] = quadratic_c(c, points_quad[i - 1]);
    }

    // Génération de la suite pseudo aléatoire
    for(i = 0 ; i <= gpa_size ; i++)
    {
        gpa_tab[i] = gpa_det(points_quad[i]);
    }

    // Ecriture dans un fichier
    wrote_f = fopen("quad_gpa_bin", "w");
    // En-têtes de dieharder
    fprintf(wrote_f, "type: d\n");
    fprintf(wrote_f, "count: %d\n", gpa_size);
    fprintf(wrote_f, "numbit: 32\n");
    for(i = 0 ; i < gpa_size ; i++)
    {
        fprintf(wrote_f, "%d\n", gpa_tab[i]);
    }

/*    // Affichage
    for(i = 0; i < 30 ; i++)
    {
        printf("%d", gpa_tab[i]);
    }*/

    return 0;
}

double quadratic_c(float c, double x)
{
    return c*x*(1 - x);
}

struct vec henon(struct vec xn)
{
    float a = 1.4, b = 0.3;
    struct vec xn1 = {0, 0};
    xn1.x = 1 - a*xn.x*xn.x + xn.y;
    xn1.y = b*xn.x;
    return xn1;
}

int gpa_det(double x)
{
    return (int) 100*x;
}

int gpa_det_henon(struct vec pt)
{
    if (pt.x > pt.y)
    {
        return 1;
    }
    else if (pt.x < pt.y)
    {
        return 0;
    }
    else
    {
        return -1;
    }
}
