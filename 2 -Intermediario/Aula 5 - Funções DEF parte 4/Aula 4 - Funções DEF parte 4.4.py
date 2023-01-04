
variavel = 'valor'

def func():
    print(variavel)

# Criando um arg para alterarmos o valor da variavel global somente localmente
def func2(arg=None):
    arg = arg.replace('v', 'c')
    retun arg

func()

# variavel criada para alterar a variavel global dentro da função
outra_variavel = func2(arg=variavel)

print(variavel)

# imprimindo a variavel global alterada dentro da função
print(outra_variavel)