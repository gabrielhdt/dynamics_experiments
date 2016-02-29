# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 19:08:56 2016

@author: gabriel
"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def main():
    # Conditions initiales et temps
    Y0 = np.array([.7, 0, 0])
    tmin, tmax, h = 0.0, 500.0, 0.01
    t = np.arange(tmin, tmax, h)

    # Résolution
    m0, m1 = -1/7, 2/7
    alpha, beta = 9.85, 14.3
    y_full = odeint(Chua, Y0, t, args=(alpha, beta, m0, m1))

    # Soustraction du régime transitoire
    ttrans = 200
    y = y_full[ttrans:, ].copy()

    # Diagramme y_{n+1} = f(x_n)
    poincare_val = poincare_map(y)
    plt.scatter(poincare_val[:-1], poincare_val[1:])
    plt.show()

    # Diagramme de Feigenbaum (arbre de doublement de période)
    beta = 15
    alpha = np.arange(8.43, 8.8, 0.01)
    for a in alpha:
        y_perdbl = odeint(Chua, Y0, t, args=(a, beta, m0, m1))
        poincare_perdbl = poincare_map(y_perdbl[ttrans:, ])
        plt.scatter([a for i in poincare_perdbl], poincare_perdbl)
    plt.show()
    # Ecriture
#    write_to_file(y)

    # Figures
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot(y[:, 0], y[:, 1], y[:, 2], linewidth=0.3)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    plt.show()


def Chua_diode(x, m0, m1):
    """
    x variable (tension), m0 pente avant et après la coupure, m1 pente entre
    les coupures
    """
    return m1*x+0.5*(m0 - m1)*(abs(x + 1) - abs(x - 1))


def Chua(y, t, alpha, beta, m0, m1):
    """
    y array, renvoit un array de taille(len(t), len(y0))
    """
    # Dérivées
    xd = alpha*(y[1] - Chua_diode(y[0], m0, m1))
    yd = y[0] - y[1] + y[2]
    zd = -beta*y[1]
    return [xd, yd, zd]


def see_char(function):
    k = np.arange(-5, 5, .01)
    plt.plot(k, [Chua_diode(i) for i in k])
    plt.show()


def write_to_file(points):
    N = points.shape[0]
    with open('chua.csv', 'w') as f:
        f.write("a,b,c,d\n")
        for i in range(N):
            f.write("{},{},{},{}\n".format(i, points[i, 0], points[i, 1],
                                           points[i, 2]))


def intersect_plan(epsilon, y):
    """
    renvoit les indices tel que y[i] < epsilon et y[i + 1] > epsilon
    dans un array de forme (n, 2) avec n le nombre d'intersections avec
    epsilon
    On ne prend que les intersections allant de sous le plan vers au-dessus
    """
    intersect = np.zeros((1, 2), dtype=int)
    y_shifted = y - epsilon  # Soustraction terme à terme pour pouvoir
    for i in range(1, len(y)):  # comparer à zéro
        if y_shifted[i] == 0:
            intersect = np.vstack((intersect, [i, i])).copy()
        elif y_shifted[i] < 0 and y_shifted[i - 1] > 0:
            intersect = np.vstack((intersect, [i - 1, i])).copy()
        else:
            continue
    return intersect


def poincare_map(y):
    """
    Fonction de Poincaré, renvoit un array de vecteurs (len(y),2)
    La section de Poincaré est le plan U_1 x=1
    La vectorialisation entrainant des erreurs, on se limite à la suite des
    (y_n)_n
    """
    # Recherche des intersections de la courbe avec le plan x = 1
    indices = intersect_plan(1, y[:, 0])
    # Valeurs (vectorielles) des points de la fonction de Poincaré
    # i.e. point avant le passage à travers U_1 (plan x=1)
    # signées négativement pour les rendre positives
#    values = np.array([[-y[i, 1] for i in indices[:, 0]],
#                       [-y[i, 2] for i in indices[:, 0]]]).transpose()
#    return values
    # \'Etonnemment, la vectorialisation entraîne des erreurs (points décalés)
    return [-y[i, 1] for i in indices[:, 0]]

if __name__ == "__main__":
    main()
