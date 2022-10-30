"""
1- Crie uma função1 que recebe uma função2 como parametro e retorne o valor da função dois executada
"""
def func1(func_aux):
    return (func_aux())

def func2():
    print('oi')

func1(func2)

print('----------------------------------------')
"""
2- Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da função2 executada. Faça a função1 executar duas funções
que recebam um número diferente de argumentos
"""
def func2_1(func_aux2, func_aux2_2):
    return (func_aux2('gustavo', 'ola'), func_aux2_2('22'))

def func2_2(nome, saudacao):
    print(f'{saudacao} {nome}')

def func2_3(idade):
    print(f'Voce tem {idade} anos!')

func2_1(func2_2, func2_3)
