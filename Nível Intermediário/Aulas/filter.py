def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.00},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.00},
    {'nome': 'Produto 4', 'preco': 69.00},
]

novos_produtos = filter(
    lambda p: p['preco'] > 10,
    produtos
)

print_iter(novos_produtos)