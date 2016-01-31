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

    # Ecriture des fichiers
    write_to_file(points)
    
    # GPA
    GPAtab1 = gpa1(points[0,:])
    with open('henon_gpa1.csv', 'w') as f:
        f.write("a,b\n")
        for i in GPAtab1:
            f.write("{}\n".format(i))
    with open('henon_bin', 'w') as f:
            f.write(bytearray(GPAtab1))

    # Résultats et graphs
    #plt.plot(points[0, :], points[1, :], '.')
    #plt.show()
    #plt.plot([i for i in range(N)], points[0, :])
    #plt.show()

    # Cryptage
    mesb = str_to_bin("le fond de l'air est frais")
    ciphered = xor_tat(mesb, GPAtab1)
    print(GPAtab1)
    print(ciphered)
    
    # Décryptage
    deciphered = xor_tat(ciphered, GPAtab1)
    print(mesb)
    print(deciphered)


def write_to_file(points):
    N = points.shape[1]
    with open('henon.csv', 'w') as f:
        f.write("a,b,c\n")
        for i in range(N):
            f.write("{},{},{}\n".format(i, points[0, i], points[1, i]))

def gpa1(points):
    """
    Fonction de création du pseudo aléa 1. Si x > 0.7, renvoit 1, 0 sinon
    """
    pa = []
    for i in points:
        if i > 0.7:
            pa.append(1)
        else:
            pa.append(0)
    return pa


def xor_tat(mesb, gpa):
    assert len(mesb) <= gpa
    ciphered = []
    for i, elt in enumerate(mesb):
        ciphered.append(int(elt)^int(gpa[i]))
    return ciphered


def str_to_bin(mes):
    return ''.join(format(ord(x), 'b') for x in mes)



if __name__ == "__main__":
    main()
