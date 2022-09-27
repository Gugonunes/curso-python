"""
Criar variáveis para nome (str), idade (int),
altura(float) e peso (float) de uma pessoa
croiar variavel com o ano atual (int)
Obter o ano de nascimento da pessoa
obter o imc da pessoa com 2 casas decimais
exibir um texto com todos os valores na teal usando F string
"""
nome = 'Gustavo Alexandre'
idade = 21
altura = 1.78
peso = 77.00
ano = 2022

print(f"{nome} tem {idade} anos, pesa {peso:.2f}kg e tem {altura:.2f} de altura. \nSeu imc é {(peso / (altura ** 2)):.2f} e seu ano de nascimento é {ano-idade}")
#o ano de nascimento só fica correto se a pessoa ja fez aniversario nesse caso ( ainda nao usamos if para fazer essa validação)
