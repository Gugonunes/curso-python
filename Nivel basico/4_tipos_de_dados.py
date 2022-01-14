"""
Tipos de dados
str - string  -  textos 'assim' ou "assim"
int - inteiro  -  123456 0 -1323
float - numero real/flutuante  -  10.2  -20.2  0.0
bool - booleano/lógico  -  True ou False  10 == 10
"""

print("Gustavo", type("Gustavo"))
print(10, type(10))
print(10.2, type(10.2))
print('l' == 'l', type('l' == 'l'))
print(bool(''))

print('10', type('10'), type(int('10')))

#Exemplo de cadastro com cada tipo de dado
#Nome - str
print("Gustavo Alexandre", type("Gustavo Alexandre"))
#Idade - int
print(21, type(21))
#Altura - float
print(1.78, type(1.78))
#É maior de idade - bool
print(21>=18, type(21>=18))
