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
__version__ = "0.0.1"
__author__ = "Arthur Araujo"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANG", "en_US")[:5]
msg = "Hello, World!"
if current_language == "pt_BR":
    msg="Ola Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mundo!"
elif current_language == "es_SP":
    msg = "Hola. Mundo!"
elif current_language == "fr_FR":
    msg = "Bonjour Monde!"

print (msg)