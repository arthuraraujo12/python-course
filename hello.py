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
__version__ = "0.1.3"
__author__ = "Arthur Araujo"
__license__ = "Unlicense"

import os
import sys

arguments = {
    "lang": None,
    "count": 1,
}
for arg in sys.argv[1:]:
    # TODO: Tartar ValueError anm
    key, value = arg.split("=")
    key = key.lstrip("-").strip()
    value = value.lstrip("-").strip()
    if key not in arguments:
        print(f"Invalid Option {key}")
        sys.exit()
    arguments[key] = value

current_language = arguments["lang"]
if current_language is None:
#TODO: Usar repetição
    if "LANG" in os.environ:
     current_language =  os.getenv("LANG"),
    else: 
        current_language = input("Choose a language:")

current_language = current_language[:5]

msg = {
    "en_US": "Hello World!",
    "pt_BR": "Ola Mundo!",
    "it_IT": "Ciao, Mundo!",
    "es_SP": "Hola Mundo!",
    "fr_FR": "Bonjour Monde",
}

print (
    msg[current_language] * int(arguments["count"])
    )