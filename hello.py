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
__version__ = '0.0.2'
__author__ = 'Vicente Marçal'
__license__ = 'GPLv3+'

import os

current_local = os.getenv('LANG')[:5]

msg = {
    'pt_BR': 'Olá, Mundo!',
    'es_ES': '¡Hola, Mundo!',
    'fr_FR': 'Bonjour, le monde!',
    'it_IT': 'Ciao, mondo!'
}.get(current_local, 'Hello, World!')

print(msg)

