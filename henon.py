#!/usr/bin/python
# -*- coding: utf-8 -*-

from sympy.abc import x, y
from sympy.utilities.lambdify import lambdify
import numpy as np
import matplotlib.pyplot as plt


def main():
    N = 600

    # Fonction de Hénon, paramètres et définition
    a, b = 1.4, 0.3
    H = lambdify((x, y), (1 - a*x**2 + y, b*x))

    # Tableau de valeurs et condition initiale
    points = np.zeros((2, N))
    points[:, 0] = [.5, .2]

    # Calcul des points successifs
    for i in range(1, N):
        points[:, i] = H(points[0, i - 1], points[1, i - 1])

    # Résultats et graphs
    plt.plot(points[0, :], points[1, :], '.')
    plt.show()
    plt.plot([i for i in range(N)], points[0, :])
    plt.show()


if __name__ == "__main__":
    main()
