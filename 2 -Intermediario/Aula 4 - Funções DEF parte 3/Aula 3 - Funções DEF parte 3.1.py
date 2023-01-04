'''
    Funções DEF em python parte 3

    *args e *kwargs = ley words arguments(nomes a escolha do usuario)
'''

def func(n1, n2, n3, n4, n5, nome=None, var=None):
    print(n1, n2, n3, n4, n5, nome, var)

func(1, 2, 3, 4, 5, nome = 'Lucas', var = 'teste')

# Evoluindo o código

def func(n1, n2, n3, n4, n5, nome=None, var=None):
    print(n1, n2, n3, n4, n5, nome, var)
    return nome, var

var = func(1, 2, 3, 4, 5, nome = 'Lucas', var = 'teste')
print(var)

# Evoluindo mais

print()
def func(n1, n2, n3, n4, n5, nome=None, var=None):
    print(n1, n2, n3, n4, n5, nome, var)
    return nome, var

valores = func(1, 2, 3, 4, 5, nome = 'Lucas', var = 'teste')
print(valores[0], valores[1])
# printando somente os argumentos nome e var