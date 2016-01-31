# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 19:08:56 2016

@author: gabriel
"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#def chua_diode(x):
#    if x < -1:
#        return -.1*x + 3.9
#    elif x >= -1 and x <= 1:
#        return -4*x
#    else:
#        return .1*x - 4.1


def main():
    # Conditions initiales et temps
    Y0 = np.array([.7, 0, 0])
    t = np.arange(0.0, 80.0, 0.01)
    
    # Résolution
    y = odeint(Chua, Y0, t)
    print(y.shape)

    # Ecriture
    write_to_file(y)

    # Figures
    fig=plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot(y[:,0], y[:,1], y[:,2], linewidth=0.3)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    plt.show()
    plt.plot(t,y[:,0])
    plt.show()


def Chua_diode(x):
    m0, m1 = -1.143, -0.714  # Pentes avant et après coupure
    return m1*x+0.5*(m0-m1)*(abs(x+1)-abs(x-1))

def Chua(y, t):
    """ y array"""
    # Constantes
    alpha = 15.6
    beta = 28
   
    # Dérivées
    xd = alpha*(y[1] - y[0] - Chua_diode(y[0]))
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


if __name__ == "__main__":
    main()
