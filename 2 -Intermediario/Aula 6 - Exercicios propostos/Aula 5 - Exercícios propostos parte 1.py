
'''
    1  - Crie uma função1 que recebe uma função como parâmetro e retorne o valor da função2
    executando
'''

def func1(*args):
    print(args)

def func2():
    var = 'valor'
    return var

variavel = func2()
func1(variavel)

print('------------------------')

def ola_mundo():
    return 'olá mundo'

def mestre(funcao):
    return funcao()

executando = mestre(ola_mundo)
print(executando)