#!/bin/env python

email_tmpl = """
Olá, %(nome)s
 
Tem interesse em comprar %(produto)s?

Este produto é ótimo para resover
%(texto)s

Clique agora em %(link)s

Apenas %(quantidade)d disponíveis!

Preço promocional %(preco).2f
"""

clientes = ['Maria', 'João', 'Bruno']

for cliente in clientes:
    print(
        email_tmpl % (
            {"nome": cliente,
            "produto": "caneta",
            "texto": "ajuda a escrever bem",
            "link":"https://canetaslegais.com",
            "quantidade": 1,
            "preco":50.5}
            )
         )
    print('-' * 50)
