
# *args pode ser usado quando não sabemos a quantidade argumentos da função
def func(*args):
    print(args)

lista = [1,2,3,4,5]
# Desempacotando os valores, e empacotando o restante da lista em uma variavel com *n
n1, n2, *n = lista
print(n1,n2, *n)

print('----------------')
def func(*args):
    print(args)

lista = [1,2,3,4,5]

# printando a lista empacotada
print(lista)
# printando a lista desempacotada (com um separador)
print(*lista, sep='-')

print('----------------')

def func(*args):
    print(args)

# printando valores argumentados na função entre parentesis (usando o args)
func(1,2,3,4,5)

