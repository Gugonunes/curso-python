"""
For in em python
Iterando strings com for
Função range(start=0, stop, step=1)
"""
texto = 'python'

#for letra in texto:
#    print(letra)

for numero in range(0, 100, 8):
    print(numero)

for n in range(100):
    if n % 8 == 0:
        print(n)

nova_string = ''

for letra in texto:
    if letra == 't':
        continue
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
    else:
        nova_string += letra

print(nova_string)