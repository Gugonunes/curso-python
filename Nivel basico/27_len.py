usuario = input('Digite seu usuario: ')

qtd_caracteres = len(usuario)

print(usuario, qtd_caracteres, type(qtd_caracteres))

if qtd_caracteres < 6:
    print('Voce precisa digitar ao menos 6 caracteres')
else:
    print('Voce foi cadastrado no sistema')

string1 = input('Digite alguma coisa: ')
string2 = input('Digite outra coisa: ')

print(f'Qtd total de caracteres: {len(string1) + len(string2)}')