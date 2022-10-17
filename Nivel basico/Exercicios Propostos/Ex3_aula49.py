"""
CPF = 168.995.350-09
1 * 10 = 10                 #   1 * 11 = 11 <-
6 * 9 = 54                  #   6 * 10 = 60
...                         #   ...
5 * 3 = 15                  #   0 * 3 = 0
0 * 2 = 0                   # ->0 * 2 = 0
                            # Esse 0 é o res anterior
TOTAL: 297                  # TOTAL: 343
11 - (297 % 11) = 11        # 11 - (343 % 11) = 9
11 > 9 = 0
Digito 1 = 0                # Digito 2 = 9
"""
from functools import total_ordering
from re import I


CPF = input('Informe o seu CPF: ')
CPF = CPF.replace('.', '')

TotalDig1 = 0

for i, v in enumerate(range(10, 1, -1)):
    sum1 = int(CPF[i]) * v
    print(f'{CPF[i]} * {v} = {sum}')
    TotalDig1 += sum1
    Dig1 = 0 if (11 - (TotalDig1 % 11 > 9)) else (TotalDig1 % 11)
print(f'Total Digito 1: {TotalDig1}')
print('------------------------------------')
TotalDig2 = 0
for i, v in enumerate(range(11, 1, -1)):
    if v == 2:
        sum2 = Dig1 * v
        print(f'{Dig1} * {v} = {sum2}')
    else:
        sum2 = int(CPF[i]) * v
        print(f'{CPF[i]} * {v} = {sum2}')
    
    TotalDig2 += sum2
    Dig2 = 11 - (TotalDig2 % 11 )

print(f'Total Digito 2: {TotalDig2}')
print(f'Digitos finais: {Dig1}, {Dig2}')

CPF = str(CPF)
Novo_Cpf = ''
for i in range(0, 9):
    if(i%3 == 0 and i!=0):
        Novo_Cpf += '.'
    Novo_Cpf += CPF[i]

Novo_Cpf += (f'-{Dig1}{Dig2}')
print(Novo_Cpf)
