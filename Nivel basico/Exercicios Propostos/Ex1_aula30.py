"""
Faça um programa que peça ao usuário para digitar um numero inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um
número inteiro, informe que não é um número inteiro.
"""
num1 = input("Informe um numero inteiro: ")

if num1.isdigit():
    num1 = int(num1)
    if (num1%2)==0:
        print(f"{num1} é um numero par.")
    else:
        print(f"{num1} é um numero impar")
else:
    print(f"{num1} Não é um numero inteiro")

print("--------------------------------------------------")

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se
no horário descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noitee 18-23.
"""
hora = input("Informe a hora atual: ")

if hora.isdigit():
    hora = int(hora)
    if(hora>=0 and hora<=11):
        print("Bom dia!")
    elif(hora>=12 and hora<=17):
        print("Boa tarde!")
    elif(hora>=18 and hora<=23):
        print("Boa noite!")
    else:
        print("Hora informada é inválida no formato 0-24")
else:
    print("Valor informado não é válido")

print("--------------------------------------------------")

"""
Faça um programa que peça o primeiro nome do usuário.
Se o nome tiver 4 letras ou menos escreva "Seu nome é curto";
Se tiver entre 5 e 6 letras escreva "Seu nome é normal";
Maior que 6 escreva "Seu nome é muito grande".
"""

nome = input("Informe seu nome: ")

if not nome.isdigit():
    if (len(nome) <= 4):
        print(f"{nome}, seu nome é curto")
    elif (len(nome) >4 and len(nome)<=6):
        print(f"{nome}, seu nome é normal")
    else:
        print(f"{nome}, seu nome é muito grande")
else:
    print("Por favor informe um nome válido")

print("--------------------------------------------------")