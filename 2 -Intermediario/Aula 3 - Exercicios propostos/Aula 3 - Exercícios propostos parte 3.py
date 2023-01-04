'''
    3 - Crie uma função receba 2 numeros. O primeiro é um valor e o segundo
    um percentual (ex: 10%). Retorne o valor do primeiro número somado do
    aumento do percentual do mesmo


'''

def funcao(n1 = 50, n2 = 20):
    return n1 + ((n1 * n2) / 100)

var = funcao()
print(var)

print('--------------')

def funcao(n1, n2):
    print(n1 + (n1 * n2) / 100)

funcao(50, 20)
funcao(100, 30)
funcao(33, 44)
