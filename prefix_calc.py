#!/usr/bin/env python3
"""Prefix Calculator.

This program calculates the result of a prefix expression.
Example of usage:
    python prefix_calc.py sum 1 2
    3
    python prefix_calc.py sub 1 2
    -1
    python prefix_calc.py mul 2 3
    6
    python prefix_calc.py div 4 2
    2
"""
__version__ = '0.1.0'
__author__ = 'Vicente Marçal'
__license__ = 'GPLv3+'

import sys


def sum_(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if b == 0:
        print('Division by zero is not allowed.')
        sys.exit(1)
    return a / b


arguments = sys.argv[1:]

if len(arguments) != 3:
    print(
        'Invalid number of arguments.'
        '\nExample of usage: \n$ python prefix_calc.py sum 1 2'
    )
    sys.exit(1)

if not arguments:
    operation = input('Enter the operation: ')
    operand1 = input('Enter the first operand: ')
    operand2 = input('Enter the second operand: ')
    arguments = [operation, operand1, operand2]

operation, *nums = arguments

valid_nums = []

operations = {
    'sum': sum_,
    'sub': sub,
    'mul': mul,
    'div': div
}

if operation not in operations:
    print(
        f'"{operation}" is not recognized as a valid Operation.'
        '\nAvailable operations are: `sum`, `sub`, `mul`, and `div`.'
        '\nExample of usage: \n$ python prefix_calc.py sum 1 2'
    )
    sys.exit(1)

for num in nums:
    if not num.replace('.', '').isdigit():
        print(f'"{num}" is not a valid number.')
        sys.exit(1)
    if '.' in num:
        num = float(num)
    else:
        num = int(num)
    valid_nums.append(num)

operand1, operand2 = valid_nums


result = operations[operation](operand1, operand2)


print(f'The result of {operation} {operand1} {operand2} is {result}')
