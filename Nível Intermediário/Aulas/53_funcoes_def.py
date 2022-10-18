"""
Funções - def em Python (pt2)
"""
def funcao(var):
    return var

variavel = funcao('Valor que eu quero')

if variavel:
    print(variavel)
else:
    print('Nenhum valor.')

def divisao(n1, n2):
    if n2 == 0:
        return
    return n1 / n2

divide = divisao(8,2)
if divide:
    print(divide)
else:
    print('Conta inválida')

def dumb():
    return 'Luiz', 'Otavio'

print(dumb(), type(dumb()))