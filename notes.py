#!/usr/bin/env python
"""Bloco de notas simples.

Uso:
    $ notes.py new "Minha nota"
    tag: TECH
    text: Aqui vem o texto da nota.

    $ notes.py read TECH
    ...
    ...
    ...
"""

__version__ = '0.1.0'
__author__ = 'Vicente Marçal'
__license__ = 'GPLv3+'

import sys
from pathlib import Path

# Definitions
arguments = sys.argv[1:]

if not arguments:
    print('Command missing, the commands allowed are: new, read')
    sys.exit(1)

if len(arguments) < 2:
    print('Parameter missing, you need to pass a title for the note or the tag that you want to read.')
    print('Example:\n$ python notes.py new "My note"')
    print('Example:\n$ python notes.py read TECH')
    sys.exit(1)

command, parameter = arguments
commands_allowed = ['new', 'read']
file_path = Path().cwd() / 'notes.txt'


# Check if the command is allowed.
if command not in commands_allowed:
    print('Command not allowed, the commands allowed are: new, read')
    sys.exit(1)

if command == 'new':
    title = parameter
    text = [f'{title}', input('tag: ').strip(), input('text: ').strip()]
    with open(file_path, 'a') as file:
        file.write('\t'.join(text) + '\n')

if command == 'read':
    for line in open(file_path):
        title, tag, text = line.split('\t')
        if tag.lower() == parameter.lower():
            print(f'Title: {title}')
            print(f'Text: {text}')
            print('-' * 20)
