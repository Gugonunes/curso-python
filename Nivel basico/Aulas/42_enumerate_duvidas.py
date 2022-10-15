lista = [
['Edu', 'Joao', 'Luiz'],
['Maria', 'Aline', 'Joana'],
['helena', 'ed', 'Lu'],
]
print(lista[1][2])

enumerada = list(enumerate(lista))
print(enumerada[1][1][1])

for v1 in enumerate(lista):
    valor_enumerado, minha_lista = v1
    nome1, nome2, nome3 = minha_lista
    print(nome1)