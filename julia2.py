#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#  julia2.py
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
    dim = (300,300) # Dimensions de l'image de sortie
    xint = (-2,2) # Intervalle des parties réelles
    yint = (-2,2) # Intervalle des parties imaginaires
    iterate = 15000 # Nombre de racines à calculer
    threshold = 50 # Racines à ne pas tracer
    c = -.8 + .4j
    w0 = 1+1.6j # Point initial
    im = pl.zeros(dim)
    
    l = backward_orbit(w0,c,iterate,threshold)
    im = plot_orbit(l, dim, xint, yint)
    pl.imshow(im, cmap="Greys", origin="lower")
    pl.show()
    
    return 0

def cart2pol(z):
    """
    Convertit les coordonnées cartésiennes en coordonées polaires
    """
    if z.real < 0:
        return (abs(z), pl.pi + pl.arctan(z.imag/z.real))
    elif z.real > 0:
        return (abs(z), pl.arctan(z.imag/z.real))
    elif z.real == 0:
        return (abs(z), pl.pi/2)

def pol2cart(r, theta):
    """
    Convertit les coordonées polaires en cartésiennes
    """
    return complex(r*pl.cos(theta), r*pl.sin(theta))

def F(z, c):
    return z**2 + c

def sqr_cplx(z):
    """
    Fonction racine d'un complexe. Prend aléatoirement la racine
    positive ou négative
    """
    r, theta = cart2pol(z)
    r = pl.sqrt(r)
    theta = theta/2 + int(2*pl.random())*pl.pi
    return pol2cart(r, theta)

def cplx2pix(dim, xint, yint, z):
    """
    Associe à un complexe un pixel
    dim dimension de l'image
    x,yint intervalles partie réelle (x) et partie im (y)
    z complexe
    """
    x = (-xint[0] + z.real)*dim[1]/(xint[1] - xint[0])
    y = (-yint[0] + z.imag)*dim[0]/(yint[1] - yint[0])
    return (x,y)

def backward_orbit(w0, c, iterate, threshold):
    """
    Calcule l'orbite précédent z
    """
    wn = pl.zeros(iterate - threshold, dtype="complex")
    for i in range(iterate):
        w0 = sqr_cplx(w0 - c)
        if i >= threshold:
            wn[i - threshold] = w0
    return wn

def plot_orbit(wn, dim, xint, yint):
    im = pl.zeros(dim)
    for z in wn:
        x,y = cplx2pix(dim, xint, yint, z)
        im[x, y] = 1
    return im

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
