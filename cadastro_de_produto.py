#!/usr/bin/env python
"""Cadastro de produtos"""
__version__ = '0.1.0'

produto = {
    'nome': 'Caneta',
    'cores': ['azul', 'preta', 'vermelha'],
    'preco': 1.50,
    'dimensaos': {
        'altura': 12.1,
        'largura': 0.8,
    },
    'em_estoque': True,
    'codigo': 45678,
    'codebar': None
}

cliente = {
    'nome': 'Bruno'
}

compra = {
    'cliente': cliente,
    'produto': produto,
    'quantidade': 3,
}

total_compra = compra['quantidade'] * compra['produto']['preco']

print(
    f'O cliente: {compra["cliente"]["nome"]} comprou {compra["quantidade"]} {compra["produto"]["nome"]} '
    f'por R$ {total_compra:.2f}'
)
