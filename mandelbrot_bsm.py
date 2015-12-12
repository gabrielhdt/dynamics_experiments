#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#  mandelbrot_bsm.py
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
    dim = (600,600)
    xydim = pl.array([[-2, -2],[2,2]])
    iterate = 20 # Nombre de points de chaque orbite à calculer
    
    im = bsm_mandelbrot(dim, xydim, F, iterate)
    pl.imshow(im, cmap = "Greys")
    pl.show()
    return 0

def F(z, c):
    return z**2 + c

def orbit_boundary(F, c, iterate):
    i = 0
    z = 0j
    while i < iterate and abs(z) < 2:
        z = F(z,c)
        i += 1
    return i

def pix2cplx(dim, xint, yint, pix):
    a = xint[0] + (xint[1] - xint[0])*pix[1]/(dim[1] - 1)
    b = yint[0] + (yint[1] - yint[0])*pix[0]/(dim[0] - 1)
    return complex(a, b)

def bsm_mandelbrot(dim, xydim, F, iterate):
    im = pl.zeros(dim)
    for i0 in range(dim[0]):
        for i1 in range(dim[1]):
            if i0*i1 == 0 or i1 == dim[1] or i0 == dim[0]:
                pass
            c = pix2cplx(dim, xydim[:,0], xydim[:,1], (i0,i1))
            i = orbit_boundary(F, c, iterate)
            if i < iterate: # Si orbite diverge
                im[i0, i1] = 0
            elif i == iterate: # Si orbite ne diverge pas
                escaped = False
                pixs = ((i0+1, i1),(i0-1, i1),(i0, i1-1),(i0, i1+1))
                p = 0
                while not escaped and p < 4:
                    c = pix2cplx(dim, xydim[:,0], xydim[:,1], pixs[p])
                    z = 0j
                    i = orbit_boundary(F, c, iterate)
                    if i < iterate: # Si une orbite a divergé, on sort
                        escaped = True
                    else:
                        p += 1
                if p < 4: # Si on est sorti avant la fin, une orbite a
                    im[i0, i1] = 1 # divergé
    return im

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
