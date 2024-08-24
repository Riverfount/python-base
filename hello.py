#!/usr/bin/env python3
"""Hello, World! A multilingual program.

This program prints out "Hello, World!" in multiple languages using the environment's variable to  encoding.

Example:
    export LANG=es_ES.UTF-8
    python hello.py
    or
    ./hello.py
    Hello, World!
"""
__version__ = '0.0.1'
__author__ = 'Vicente Marçal'
__license__ = 'GPLv3+'

import os

current_local = os.getenv('LANG')[:5]

msg = 'Hello, World!'

if current_local == 'pt_BR':
    msg = 'Olá, Mundo!'
elif current_local == 'es_ES':
    msg = '¡Hola, Mundo!'
elif current_local == 'fr_FR':
    msg = 'Bonjour, le monde!'
elif current_local == 'it_IT':
    msg = 'Ciao, mondo!'

print(msg)

