#!/usr/bin/env python
"""Exibe relatório de crianças por atividade

Imprimir a lista de criaças agrupadas por sala que frequentam cada uma das atividades.
"""

__version__ = '0.1.1'

# Dados
sala1 = ['Erik', 'Maia', 'Gustavo', 'Manuel', 'Sofia', 'Joana']
sala2 = ['João', 'Antonio', 'Carlos', 'Maria', 'Isolda']

aula_ingles = ['Erik', 'Maia', 'Joana', 'Carlos', 'Antonio']
aula_musica = ['Erik', 'Carlos', 'Maria']
aula_danca = ['Gustavo', 'Sofia', 'Joana', 'Antonio']

atividades = (
    ('Ingles', aula_ingles),
    ('Musica', aula_musica),
    ('Danca', aula_danca),
)

for nome_atividade, atividade in atividades:
    print(f'Alunos na atividade {nome_atividade}')
    print('-' * 40)
    # Listar aulnos em cada atividade por sala
    atividade_sala1 = set(sala1) & set(atividade)  # Interseção entre sala1 e atividade
    atividade_sala2 = set(sala2).intersection(atividade)  # Interseção entre sala2 e atividade

    print('Sala 1:', atividade_sala1)
    print('Sala 2:', atividade_sala2)

    print()
    print('#' * 40)
