#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#  julia1.py
#
#  Copyright 2015 Gabriel Hondet <gabrielhondet@gmail.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#

import pylab as pl


def main(args):
    """
    DocString
    """
    dim = (1000, 1000)  # Dimensions de l'image de sortie
    xint = (-3, 3)  # Intervalle des parties réelles
    yint = (-3, 3)  # Intervalle des parties imaginaires
    iterate = 30  # Nombre d'itérations
    c = 1 + .1j  # Paramètre

    im = julia_build(dim, xint, yint, iterate, c)
    pl.imshow(im, cmap="nipy_spectral", origin="lower")
    pl.imsave("julia.png", im, cmap="nipy_spectral", format="png")
    pl.show()

    vertex = None
    i_image = 0
    while vertex != "exit":
        vertex = complex(input("Vertex supérieur gauche sous la forme\
                                x+yj (pixels) : "))
        size_int = float(input("Intervalle de pixels : "))
        xint = (remap(dim[1], xint[0], xint[1], vertex.real),
                remap(dim[1], xint[0], xint[1], vertex.real + size_int))
        yint = (remap(dim[0], yint[0], yint[1], vertex.imag),
                remap(dim[0], yint[0], yint[1], vertex.imag + size_int))
        im = julia_build(dim, xint, yint, iterate, c)
        pl.imshow(im, cmap="gnuplot")
        pl.imsave("julia{}.png".format(i_image), im,
                  cmap="nipy_spectral", format="png")
        pl.show()
        i_image += 1
    return 0


def Q(x, c):
    """
    Fonction itérée
    """
    # return x**2 + c
    return c*pl.sin(x)


def remap(s, m, M, i):
    """
    Convertit le numéro de pixel en grandeur utilisable
    s : hauteur ou largeur image (pixels),
    m : minimum grandeur,
    M : maximum grandeur,
    i : itéré vérifiant m < i < M (numéro de l'elt du vecteur)
    """
    return m + (M - m)*i/(s-1)


def pix2cplx(dim, xint, yint, pix):
    """
    Convertit une coordonnée de l'écran (pixel) en complexe
    """
    a = xint[0] + (xint[1] - xint[0])*pix[1]/(dim[1] - 1)
    b = yint[0] + (yint[1] - yint[0])*pix[0]/(dim[0] - 1)
    return complex(a, b)


def julia_build(dim, xint, yint, iterate, c):
    """
    dim dimensions de l'image en pixels (tuple);
    xint intervalle d'abscisses (tuple);
    yint intervalle d'ordonnées (tuple);
    iterate nombre d'itérations (int);
    c paramètre (complex).
    """
    im = pl.zeros(dim)
    for i1 in range(dim[0]):
        for i2 in range(dim[1]):
            x = complex(remap(dim[1], xint[0], xint[1], i2),
                        remap(dim[0], yint[0], yint[1], i1))
            i = 0
            # while i < iterate and abs(x) < 2:
            while i < iterate and abs(x.imag) < 50:
                x = Q(x, c)
                i += 1
            if i == iterate:
                im[i1, i2] = 0
            else:
                im[i1, i2] = iterate - i
    return im


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
