#include "gpa_ch.h"

int main(int argc, char* argv[])
{
    int gpa_size = 10000, c, i;
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
    wrote_f = fopen("quad_gpa_bin", "bw");
    fwrite(gpa_tab, sizeof(int), gpa_size - 1, wrote_f);
/*    for(i = 0 ; i < gpa_size ; i++)
    {
        fprintf(wrote_f, "%d\n", gpa_tab[i]);
    }*/

    // Affichage
    for(i = 0; i < 30 ; i++)
    {
//        printf("%f", points_quad[i]);
        printf("%d", gpa_tab[i]);
    }

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
    return (int) 10*x;
}

