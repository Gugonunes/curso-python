#Índices

#012345.....33
frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
contador = 0
nova_string = ''

input_do_usuario = input('Qual letra deseja colocar maiúscula: ')

while contador < tamanho_frase:
    #print(frase[contador], contador)
    letra  = frase[contador]
    if letra == input_do_usuario:
        nova_string += input_do_usuario.upper()
    else:
        nova_string += frase[contador]
    contador += 1

print(nova_string)