#!/usr/bin/env python3
"""Hello World Multi Linguas.

Dependendo da lingua configurada no ambiente o programa exibe a mensagem 
correspondente.

Como usar:

Tenha a variável LANG devidamente configurada ex:

    export LANG=pt_BR

Execução:

    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.0.1"
__author__ = "Marciano Priebe"
__licence__ = "Unlicense"

current_language = "en_US"

msg = "Hello, World"


if current_language == "pt_BR":
    msg = "Olá, Mundo!"

print(msg)



