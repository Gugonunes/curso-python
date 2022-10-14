"""
For/ else em python
""" 

variavel = ['Gustavo Alexandre', 'Joao', 'Maria']

for valor in variavel:
    if valor.lower().startswith('g'):
        break

else:
    print('Nao existe uma palavra que começa com G')