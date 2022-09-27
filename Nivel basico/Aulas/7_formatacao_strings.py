nome = 'Gustavo'
idade = 21
altura = 1.78
e_maior = idade > 18
peso = 77
imc = peso / (altura ** 2)

print(nome, 'tem', idade, 'anos de idade e seu imc é', imc)

print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')
print('{} tem {} anos de idade e seu imc é {:.2f}'.format(nome, idade, imc))
print('{0} tem {1} anos de idade e seu imc é {2} {0} {0} {1}'.format(nome, idade, imc))  #com os numeros dentro das chaves da pra repetir a variavel
print('{n} tem {i} anos de idade e seu imc é {im} '.format(n=nome, i=idade, im=imc))  #da para usar nomes tambem