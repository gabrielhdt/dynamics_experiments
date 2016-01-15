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
import random
import math


def main():
    """
    Fonction principale
    """
    m = 0.5674
    k = 0.4326

    crypted = cipher(m, k, 20)
    decrypted = decipher(crypted, k, 20)
    print(crypted, decrypted)
    print("Différence :{}".format(decrypted - m))


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
        return (1 + math.sqrt(1 - x))/2
    elif bit == 0:
        return (1 - math.sqrt(1 - x))/2


def add_key(message, key):
    """
    Ajoute la clef de la manière suivante:
    return (message + key)/2 de manière à avoir
    phi:[0,1]x[0,1]->[0,1]
    """
    return (message + key)/2


def cipher(message, key, rounds):
    """
    Chiffre le message à l'aide de tous les programmes définis
    précédemment
    Crée une sous clef puis passe dans la fonction chaotique
    message + sous clef
    On utilise les notations suivantes:
    message = mk,
    message après la fonction: fk;
    message chiffré avec clef ajoutée: ck.
    """
    for i in range(rounds):
        key = F(key)
        message = F_1(message)
        message = add_key(message, key)
    return message


def remove_key(cipher, key):
    """
    Enlève la sous clef
    """
    return 2*cipher - key


def decipher(cipher, key, rounds):
    """
    Déchiffre le message. On crée d'abord la liste de sous clefs, puis on
    déchiffre le message
    """
    list_subkeys = []
    for i in range(rounds):
        key = F(key)
        list_subkeys.append(key)

    for i in range(rounds):
        cipher = remove_key(cipher, list_subkeys.pop())
        cipher = F(cipher)
    return cipher

if __name__ == "__main__":
    main()
