"""
Entrada de dados
a função input sempre retorna uma string, deve-se fazer cast se for necessario
"""
nome = input('Qual o seu nome? ')
idade = input('Qual a sua idade? ')

ano_nascimento = 2022 - int(idade)

print(f'\n{nome} tem {idade} anos e nasceu em {ano_nascimento}.\n\n')

