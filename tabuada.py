#!/usr/bin/env python3

#Taboada
__version__ = "0.0.1"
__author__ = "Marciano Priebe"
__licence__ = "Unlicense"


numeros = list(range(1,11))


for numero in numeros:
    print("Tabuada do:", numero)
    for outro_numero in numeros:
        print(numero * outro_numero)
    print("----------------------------------------")
