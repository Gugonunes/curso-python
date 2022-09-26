num1 = input("Digite um numero: ")
num2 = input("digite outro numero: ")

"""
num1 = int(num1)
num2 = int(num2)
"""

#isnumeric isdigit isdecimal
#números e positivos
print(num1.isdecimal())
print(num2.isdecimal())


print(num1+num2)

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)

    print(num1+num2)
else:
    print("Nao pode converter os numeros pra conta")

#introdução ao try
try:
    num1 = int(num1)
    num2 = int(num2)

    print("----------------\n")
    print(num1+num2)
except:
    print("error")
