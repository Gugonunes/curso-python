"""
1 - Crie uma função que exibe uma saudação com os parâmetros saudacao e nome.
"""
from unittest import result


def saudacoes(saudacao, nome):
    print(saudacao, nome)

saudacoes('Olá', 'Gustavo')

print('--------------------------------------------')
"""
2 - Crie uma função que recebe 3 números como parâmetros e exiba a soma entre eles.
"""
def soma_3(n1, n2, n3):
    print(n1+n2+n3)

soma_3(1,2,3)

print('--------------------------------------------')
"""
3 - Crie uma função que receba 2 números. O primeiro é um valor e o segundo um percentual
(ex. 10%). Retorne (return) o valor do primeiro número somado do aumento percentual
do mesmo.
"""
def aumento(valor, percentual):
    return(valor + valor*(percentual/100))

resultado3 = aumento(100, 10)
print(resultado3)

print('--------------------------------------------')
"""
4 - Fizz Buzz - Se o parâmetro da função for divisível por 3, retorne fizz, se o parâmetro
da função for divisível por 5, retorn buzz. Se o parametro da função for divisível por 5 e 3, 
retorne FizzBuzz, caso contrário, retorne o número enviado.
"""
def FizzBuzz(num):
    if (num % 3 == 0) and (num % 5 == 0):
        return 'FizzBuzz'
    if num % 3 == 0:      #Caso o primeiro if seja false, irá sempre ir pro próximo, portando
        return 'Fizz'     #nao é necessário usar elif
    if num % 5 == 0:
        return 'Buzz'
    return num            #Pelo mesmo motivo, não é necessário um else, afinal se todos os ifs
                          #forem false, ele sempre irá cair nessa opção  
resultado4 = FizzBuzz(15)
print(resultado4)

print('--------------------------------------------')