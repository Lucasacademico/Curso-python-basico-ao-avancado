


def func1():
    outra_variavel = 'valor'
    return outra_variavel

def func2(arg):
    print(arg)

var = func1()
func2(var)

'''
    Func 2 recebe o retorno da func1
    
    Importante, não podemos transferir simplesmente uma variavel de uma func1 para uma func2
    porém, podemos criar um argumento na func2, gerar um retorno de valor da func1, e passar
    para a func2 através de uma variavel.
'''