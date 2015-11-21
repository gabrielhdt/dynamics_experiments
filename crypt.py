#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  [filename.py]
#
#  Copyright [yyyy] Gabriel Hondet <gabrielhondet@gmail.com>
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.

#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.

#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#
import numpy as np
import random


def main():
    """
    Fonction principale
    """
    message = 0.1654
    key = 0.12
    # Chiffrage :
    ciphered = message
    iteration = 5  # Nombre d'itérations
    for i in range(iteration):
        ciphered = F_1(ciphered)
    ciphered = ciphered + key - int(ciphered + key)

    # Déchiffrage
    deciphered = ciphered - key
    for i in range(iteration):
        deciphered = F(deciphered)
        print(deciphered)
    print("Différence : {}".format(deciphered - message))


def F(x):
    """
    Fonction de chiffrage chaotique
    F:[0,1]->[0,1]
    """
    return 4*x*(1 - x)


def F_1(x):
    """
    Fonction réciproque mais pas bijection, on choisit
    un des deux antécédents au hasard
    """
    bit = random.getrandbits(1)
    if bit == 1:
        return (1 + np.sqrt(1 - x))/2
    elif bit == 0:
        return (1 - np.sqrt(1 - x))/2


if __name__ == "__main__":
    main()
