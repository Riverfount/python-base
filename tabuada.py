#!/usr/bin/env python3
"""Print the multiplication table of numbers 1 to 10.

This script demonstrates the use of nested loops to print the multiplication."""
__author__ = 'Vicente Marçal'
__version__ = '0.0.1'
__license__ = 'GPLv3+'

numbers = range(1, 11)
for i in numbers:
    for j in numbers:
        print(f'{i} * {j} = {i * j}')
    print('-' * 12)
