from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Gustavo', 'nota': 'B'},
    {'nome': 'Luana', 'nota': 'A'},
    {'nome': 'Joao', 'nota': 'C'},
    {'nome': 'Natalia', 'nota': 'D'},
    {'nome': 'Evandro', 'nota': 'A'},
    {'nome': 'Ana', 'nota': 'B'},
    {'nome': 'Jorge', 'nota': 'A'},
    {'nome': 'Carlos', 'nota': 'C'},
]

def ordena(aluno):
    return aluno['nota']

alunos_agrupados = sorted(alunos, key=ordena)
grupos = groupby(alunos_agrupados, key=ordena)

for chave, grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno)
