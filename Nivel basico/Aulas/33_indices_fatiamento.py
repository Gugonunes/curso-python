"""
-> String indices
-> Fatiamento de strings [inicio:fim:passo]
-> Funções built-in len, abs, type, print, etc...
"""
texto = 'Python s2'
#positivos 
#       [012345678]
#negativos
#      -[987654321]
print(texto[2])
url = 'www.google.bom.br/'
print(url[:-1])

nova_string = texto[2:6]
nova_string_comeco = texto[:6]
print(nova_string, nova_string_comeco)

# texto[0:6:2] -> pula de 2 em 2
# texto[0::3]  -> do inicio ao fim, pulando de 3 em 3



