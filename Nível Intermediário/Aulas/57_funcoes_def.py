variavel = 'valor'

print(variavel)

def func():
    print(variavel)

def func2():
    global variavel   #altera o valor da variavel global
    variavel = 'outro valor'
    print(variavel)

def func3(arg = None):
    arg = arg.replace('v', 'c')
    return arg

func()
func2()
outra_variavel = func(arg = variavel)
print(variavel)
print(outra_variavel)
