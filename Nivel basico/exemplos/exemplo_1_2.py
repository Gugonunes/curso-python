"""
Operadores lógicos
and or not
in e not in
"""
a = 2
b = 3

if not a>b:
    print('B é maior do que A')

nome = 'Gustavo'

if 'x' in nome:
    print('Existe a letra U no seu nome')
elif 'x' not in nome:
    print('Nao esta')
else:
    print('Nao existe')

usuario = input('Nome do usuario: ')
senha = input('Senha do usuario: ')

usuario_bd = 'gustavo'
senhha_bd = '12345'

if usuario_bd == usuario and senhha_bd == senha:
    print('Voce esta logado')
else:
    print('senha ou usuario invalidos')