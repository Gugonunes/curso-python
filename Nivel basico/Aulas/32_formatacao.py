"""
Formatos:
:s    -> String
:d    -> Int
:f    -> Float
:.(numero)f    -> Quantidade de casas decimais float
:(caractere)(> ou < ou ^)(quantidade)(tipo - s, d ou f)  -> 

>   -> Esquerda
<   -> Direita
^   -> Centro
"""
num1 = 1
num2 = 3
divisao = num1/num2
print(divisao)
print("{:.2f}".format(divisao))
print(f"{divisao:.2f}")

print(f"{num1:0>10}")

num3 = 1250
print(f"{num3:0^10}")

print(f"{num3:.2f}")

print(f"{num3:0>10.2f}")

nome = 'Gustavo Alexandre'
print(f"{nome:#^50}")

nome_formatado = '{:@>50}'.format(nome)
print(nome_formatado)

sobrenome = 'Tuchlinowicz Nunes'
nome2_formatado = '{0:@<30} {1:#^50}'.format(nome, sobrenome)
print(nome2_formatado)
