#ifndef GPA_CH_H_
#define GPA_CH_H_
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

struct vec
{
    double x;
    double y;
};
double quadratic_c(float, double);
struct vec henon(struct vec);
int gpa_det(double);
int gpa_det_henon(struct vec);
#endif
