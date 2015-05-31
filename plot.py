#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  plot.py
#  
#  Copyright 2015 gabriel <gabriel@p8h77-m>
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
import pygal

def main():
    plot_orbit()
    return 0

def plot_orbit():
    i = 0
    x = []
    y = []
    coordinates = []
    chart = pygal.XY(stroke=False)
    chart.title = u'Orbite'
    chart.x_title = u'Itérations'
    chart.y_title = u'Images'
    with open('orbit', 'r') as f:
        for line in f:
            if line[0] == '#':
                pass
            else:
                x.append(i)
                y.append(float(line.rstrip()))
                coordinates.append((i,float(line.rstrip())))
                i += 1
        f.close()
    chart.add('A', coordinates)
    chart.render_to_file('orbit_chart.svg')
    pl.plot(x,y, '-o')
    pl.xlabel('Iterations')
    pl.ylabel('Image')
    pl.show()
    return 0

def plot_bif_diag():
    i = 0
    y = []
    x = 0. # Corresponds to the value of the parameter
    chart = pygal.XY(stroke=False)
    chart.title = 'Diagramme de bifurcation'
    with open('bif_diag', 'r') as f:
        for line in f:
            if line[0] == '#':
                pass
            else:
                sep_param = line.index(':')
                c = float(line[0:sep_param-1])
                y = line[sep_param+1:-1].rstrip().split(';')
if __name__ == '__main__':
    main()

