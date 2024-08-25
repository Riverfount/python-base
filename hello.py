#!/usr/bin/env python3
"""Hello, World! A multilingual program.

This program prints out "Hello, World!" in multiple languages using the environment's variable to  encoding.

Example:
    Set the language by envinronment variable:
    export LANG=es_ES.UTF-8

    Or by CLI argument:
    python hello.py --lang=es_ES

    Or the user needs to choose the languag.e

    ./hello.py
    Hello, World!
"""

__version__ = '0.1.3'
__author__ = 'Vicente Marçal'
__license__ = 'GPLv3+'

import os
import sys

arguments = {'lang': None, 'count': 1}

for arg in sys.argv[1:]:
    # TODO: Tratar ValueError
    key, value = arg.split('=')
    key = key.lstrip('-').strip()
    value = value.strip()
    if key not in arguments:
        print(f'Argument "{key}" not recognized.')
        sys.exit(1)
    arguments[key] = value

current_language = arguments['lang'] or os.getenv('LANG')

if not current_language:
    current_language = input('No language set. Choose a language: ')

current_language = current_language[:5]

msg = {
    'pt_BR': 'Olá, Mundo! ',
    'es_ES': '¡Hola, Mundo! ',
    'fr_FR': 'Bonjour, le monde! ',
    'it_IT': 'Ciao, mondo! ',
}.get(current_language, 'Hello, World! ')

print(msg * int(arguments['count']))
