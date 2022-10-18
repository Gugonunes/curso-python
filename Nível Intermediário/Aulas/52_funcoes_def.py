"""
Funções - def em Python (pt1)
"""
from statistics import variance


def saudacao(msg='Olá', nome='Usuário'):
    nome = nome.replace('e', '3')
    msg = msg.replace('e', '3')
    return f'{msg} {nome}'

"""msg='Olá' é um valor padrão, caso a função seja chamada
sem parametros, terá 'Olá' como padrão"""

#saudacao('Olá', 'Luiz Otávio')
variavel = saudacao()
print(variavel)