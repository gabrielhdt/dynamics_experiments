#ifndef BIF_DIAG_H_
#define BIF_DIAG_H_
#define ITER_BIF 500
#define BIF_PLOT 400
#include <stdio.h>
#include <stdlib.h>

void calculate_orbit(double *values, float c, double (*F)(float, double));
double quadratic_c(float c, double x);

#endif /*BIF_DIAG_H_*/
