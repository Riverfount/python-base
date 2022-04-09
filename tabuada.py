#!/usr/bin/env python
"""Imprime a tabuada do 1 ao 10.

Tabuada do 1
1 x 1 = 1
1 x 2 = 2
1 x 3 = 3
...

Tabuada do 2
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
...

"""
__version__ = '0.0.1'
__author__ = 'Vicente Marçal'
__license__ = 'GPLv3+'

# numeros de 1 a 10
numbers = list(range(1, 11))

# Iterable (percorríveis)

for n1 in numbers:
    print(f'Tabuada do: {n1}')
    for n2 in numbers:
        print(f'{n1} x {n2} = {n1 * n2}')
    print('\n-----------------\n')
