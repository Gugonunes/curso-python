"""
while em python
"""
#while condicao:
#   pass

##Comandos:
"""
break    -> finaliza a execução, sai do loop
continue -> Pula para proxima execução
"""

"""while True:
    nome = input("Qual seu nome? ")
    print(f"Olá {nome}")
"""

x = 0
while x < 10:
    if x == 3:
        x = x + 1
        continue #pula o resto do código e vai pra próxima execução do while

    print(x)
    x = x + 1

print("Acabou")


x = 0 # coluna
y = 0 # linha
while(x < 10):
    y = 0
    while( y < 5):
        print(f"({x},{y})")
        y +=1

    x += 1 # x = x + 1

while True:
    print()
    num_1 = input("Digite um número: ")
    num_2 = input("Digite outro número: ")
    operador = input("Digite um operador: ")
    sair = input("Deseja sair? [s] ou [n]")

    if sair == 's':
        break

    if not num_1.isnumeric():
        print("Numero 1 invalido")
        continue
    
    if not num_2.isnumeric():
        print("Numero 2 invalido")
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    # + - * /
    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '*':
        print(num_1 * num_2)
    elif operador == '/':
        print(num_1 / num_2)
    else:
        print("Operador inválido")

