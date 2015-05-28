/*
 * main.h
 *
 *  Created on: 7 mai 2015
 *      Author: gabriel
 */

#ifndef MAIN_H_
#define MAIN_H_
#define ITER_BIF 500
#define BIF_PLOT 400
#define MAXITER 300

void calculate_orbit(double *values, int maxiter, float c, double (*F)(float, double));
double quadratic_c(float, double);

#endif /* MAIN_H_ */
