"""
Desempacotamento de lista em python
"""
lista = ['Joao', 'Luiz', 'Maria',1,2,3,4,5]

n1, n2, *outra_lista, ultimo = lista

#*outra_lista recebe o restante dos valores da lista
# *_ -> convenção de sinalização
print(n1, n2, ultimo)