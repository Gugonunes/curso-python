"""
Operadores relacionais
== > >= < <= !=
"""
print(2 == 2)

num_1 = 2
num_2 = 2

exp = (num_1 > num_2)
print(exp)

var1 = 'Gustavo'
var2 = 'Luana'

exp2 = (var1 == var2)
print(exp2)

#exemplo aplicado
nome = input('Qual seu nome? ')
idade = input('Qual a sua idade?')
idade = int(idade)

idade_limite = 18

if idade >= idade_limite and idade <=30:
    print(f'{nome} pode pegar emprestimo')

else:
    print(f'{nome} não pode pegar emprestimo')