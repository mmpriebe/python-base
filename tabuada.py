#!/usr/bin/env python3

#Taboada
__version__ = "0.0.1"
__author__ = "Marciano Priebe"
__licence__ = "Unlicense"


numeros = list(range(1,11))


for n1 in numeros:
    print("{:-^18}".format(f"Tabuada do {n1}"))
    print()
    for n2  in numeros:
        resultado = n1 * n2
        print("{:^18}".format(f"{n1} x {n2} = {resultado}"))
    print("#" * 18)
