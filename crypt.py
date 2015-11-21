#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  crypt.py
#
#  Copyright 2015 Gabriel Hondet <gabrielhondet@gmail.com>
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
    iterations = 5

    # Chiffrage
    pre_ciphered = pre_cipher(message, F_1, iterations)
    key, ciphered = add_key(pre_ciphered, create_key)
    print(ciphered)
    deciphered = decipher(ciphered, iterations, key)
    print(deciphered)
    deciphered_wrong_key = decipher(ciphered, iterations, key - .01)
    print(deciphered_wrong_key)


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


def pre_cipher(message, F_1, iterations):
    """
    Fonction de chiffrage du message, avec F la fonction itérée iterations
    fois. La fonction n'ajoute pas la clef, on n'obtient donc pas le message
    chiffré final.
    """
    pre_ciphered = message
    for i in range(iterations):
        pre_ciphered = F_1(pre_ciphered)
    return pre_ciphered


def create_key(pre_ciphered):
    """
    Fonction de création de la clef. La clef doit respecter certaines
    contraintes, ici k < 1 - c (c le flottant chiffré)
    """
    return (1 - pre_ciphered)/3


def add_key(pre_ciphered, calculate_key):
    """
    Fonction d'addition de la clef. Renvoit le message chiffré
    """
    key = create_key(pre_ciphered)
    return key, pre_ciphered + key - int(pre_ciphered + key)


def decipher(ciphered, iterations, key):
    """
    Fonction de déchiffrage.
    """
    deciphered = ciphered - key
    for i in range(iterations):
        deciphered = F(deciphered)
    return deciphered


if __name__ == "__main__":
    main()
