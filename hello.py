#!/usr/bin/env python3
"""Hello World mult linguage

Depending on the language configured in the environment, the message will 
change

Usage:

Have the LANG variable properly configure, ex:

    export LANG=pt_BRutf8
    ou
    set LANG=pt_BR.utf8

Execution:

    python3 hello.py
    ou
    hello.py
"""
__version__ = "0.1.2"
__author__ = "Arthur Araujo"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANG", "en_US")[:5]

msg = {
    "en_US": "Hello World!",
    "pt_BR": "Ola Mundo!",
    "it_IT": "Ciao, Mundo!",
    "es_SP": "Hola Mundo!",
    "fr_FR": "Bonjour Monde",
}

print (msg[current_language])