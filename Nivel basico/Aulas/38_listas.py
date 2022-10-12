"""
Listas em python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""
#lista = [1, 2, 3, 4, 'Gustavo A', True, 10.5]
from unicodedata import digit


lista = ['A', 'B', 'C', 'D', 'E', 10.5]
print(lista[::2])

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = l1 + l2

l1.extend('a') #junta
l2.append('b') #insere no final
l2.insert(0, 'banana') #insere na posição desejada

print(l2)
l2.pop() #remove o ultimo item da lista 
print(l2)

del(l2[1:3]) #deleta os itens desejados
print(l2)

print(max(l3))
print(min(l3))

l4 = list(range(1, 10)) #A função list torna objetos iteráveis em listas
print(l4)

soma = 0
for valor in l4:
    soma = soma + valor
    print(soma)

l5 = ['string', True, 10, -20.5]
for elem in l5:
    print(f'O tipo do elem é {type(elem)} e seu valor é {elem}')

secreto = 'perfume'
digitadas = []
chances = 3
while True:
    if chances <= 0:
        print('Voce perdeu!')
        break

    letra = input('Digite uma letra: ')
    if len(letra) > 1:
        print('Digite apenas uma letra')
        continue
    digitadas.append(letra)
    
    if letra in secreto:
        print(f'A letra "{letra}" pertence à palavra secreta.')
    else:
        print(f'A letra {letra} Não pertence à palavra')
        digitadas.pop()
    
    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'
    
    if secreto_temporario == secreto:
        print(f'Parabéns, você venceu! A palavra era {secreto}')
        break
    else:
        print(f'Palavra atual: {secreto_temporario}')

    if letra not in secreto:
        chances -= 1

    print(f'Voce ainda tem {chances} chances.')
    print()
