
# Modos de imprimir args
def func(*args):
    print(args)
    print(args[0])
    print(args[-1])
    print(len(args))

func(1, 2, 3, 4, 5, 6)

print('----------------')
# Não podemos alterar itens de uma tupla (argumentos do args), porém podemos mudar o tipo de args para list
def func(*args):
    # Transformando o args para list
    args = list(args)
    # mudando o valor da lista (antigo args)
    args[0] = 20
    print(args)

func(1,2,3,4,5)

print('----------------')
# printando valores em args usando o for
def func(*args):
    for v in args:
        print(v)

func(1,2,3,4,5)
