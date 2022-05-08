#!/bin/env python3
"""Calculadora infix

Funcionamento:

[operação] [n1] [n2]

Operações permitidas:

sum -> +
sub -> -
mul -> *
div -> /

Uso:

$ infixcalc.py sum 5 2
10

$ infixcalc.py mul 10 5
50

$ infixcalc.py
operação: sum
n1: 5
n2: 4
9
"""
__version__ = "0.1.0"

import sys

arguments = sys.argv[1:]

operation = {
    'sum': lambda a, b: a + b,
    'sub': lambda a, b: a - b,
    'mul': lambda a, b: a * b,
    'div': lambda a, b: a / b,  # Aqui pode ocorrer o erro de divisão por zero, tem que se tratado! 
}

if arguments:
    op, n1, n2 = arguments
    op = op.strip()
    if op not in ('sum', 'sub', 'mul', 'div'):
        print('Operação inválida, ela deve ser uma das seguintes: sum, sub, mul ou div!')
        sys.exit(-1)
    
    n1 = float(n1.strip()) if '.' in n1 else int(n1.strip())
    n2 = float(n2.strip()) if '.' in n2 else int(n2.strip())
else:
    op = input('Operação: ')
    n1 = eval(input('n1: '))
    n2 = eval(input('n2: '))

if op == 'div' and n2 == 0:
    print(f'A Operação solicitada: {op}, não suporta que o segundo número seja: {n2}')
    sys.exit('ZeroDivisionError: Division by Zero!')

print(f'O resultado é: {operation[op](n1, n2)}')
