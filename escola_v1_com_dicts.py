#!/usr/bin/env python
"""Exibe relatório de crianças por atividade

Imprimir a lista de criaças agrupadas por sala que frequentam cada uma das atividades.
"""

__version__ = '0.1.2'

# Dados
salas = {
    1: ['Erik', 'Maia', 'Gustavo', 'Manuel', 'Sofia', 'Joana'],
    2: ['João', 'Antonio', 'Carlos', 'Maria', 'Isolda'],
}

disciplinas = {
    'Ingles': ['Erik', 'Maia', 'Joana', 'Carlos', 'Antonio'],
    'Musica': ['Erik', 'Carlos', 'Maria'],
    'Danca': ['Gustavo', 'Sofia', 'Joana', 'Antonio'],
}

atividades = (
    ('Ingles', disciplinas['Ingles']),
    ('Musica', disciplinas['Musica']),
    ('Danca', disciplinas['Danca']),
)


for disciplina, alunos in disciplinas.items():
    print(f'Alunos na disciplina {disciplina}')
    print('-' * 40)
    disciplina_sala1 = set(salas[1]) & set(alunos)
    disciplina_sala2 = set(salas[2]) & set(alunos)
    print('Sala 1:', disciplina_sala1)
    print('Sala 2:', disciplina_sala2)
    print()
    print('#' * 40)
