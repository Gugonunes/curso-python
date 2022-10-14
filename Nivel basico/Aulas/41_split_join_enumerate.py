"""
Split   ->Dividir uma string # str
Join    ->Juntar uma lista # str
Enumerate -> Enumerar elementos da lista #iteráveis
"""

####Split
string = "O Brasil é o país do futebol, o Brasil é penta."
lista_1 = string.split(' ')
lista_2 = string.split(',')

palavra = ''
contagem = 0

for valor in lista_1:
    #print(valor.strip().capitalize())
    print(f'A palavra {valor} apareeceu {lista_1.count(valor)}x na frase ')
    qtd_vezes = lista_1.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f'A palavra que mais apareceu foi {palavra} ({contagem}x)')
print('----------')
####Join
print(string)
print(lista_1)
string2 = ','.join(lista_1)
print(string2)
print('----------')
####Enumerate
for indice, valor in enumerate(lista_1):
    print(indice, valor, lista_1[indice])
    #valor é igual a lista_1[indice]

lista = [
    [0,'gustavo'],
    [1,'joao'],
    [2,'maria'],
]
print('----------')
lista_3 = ['gustavo', 'joao', 'natalia']
for indice, nome in enumerate(lista_3):
    print(indice, nome)

for indice, nome in lista:
    print(indice, nome)




