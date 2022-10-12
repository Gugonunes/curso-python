"""
Aula apenas de dúvidas, explicando as iterações da aula 38.
"""

from unicodedata import digit


secreto = 'python'
secreto_temporatio = ''

digitadas = ['t']

for letra_secreta in secreto:
    print(f'Iteração para a letra {letra_secreta}')

    if letra_secreta in digitadas:
         print(f'Eba, a letra que eu queria {letra_secreta}')
         secreto_temporatio += letra_secreta
    else:
        print(f'Essa letra eu não queria {letra_secreta}')
        secreto_temporatio += '*'

print()
print(secreto_temporatio)

if secreto_temporatio == secreto_temporatio:
    print('Você ganhou!')