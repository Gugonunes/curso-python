"""
Funçoes (def) em python - *args **kwargs -
"""

def func(a1, a2, a3, a4, a5, nome = None, a6 = None):
    print(a1, a2, a3, a4, a5, a6)
    #return nome, a6

var = func(1,2,3,4,5, nome='Luiz', a6='5')
#print(var[0], var[1])

def func2(*args, **kwargs):
    print(args)
    print(args[0])
    args = list(args)
    args[0] = 20
    print(args[0])
    print(kwargs['nome'])
    nome = kwargs.get('nome')
    print(nome)

func2(1,2,3,4,5)
lista = [1,2,3,4,5]
func2(*lista, nome='Gustavo')    #enviar desempacotada, para que os elementos sejam enviados um a um