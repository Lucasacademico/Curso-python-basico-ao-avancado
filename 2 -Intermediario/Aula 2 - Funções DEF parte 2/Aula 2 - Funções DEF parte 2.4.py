
# Verificando o tipo da função
def dumb():
    return 1.1

print(dumb(), type(dumb()))
'''
    No exemplo acima, o tipo da função vai ser de acordo com o valor inputado nela,
    logo:
    
    se return 1
        1 <class 'int'>
    
    se return 1.1
        1.1 <class 'float'>
    ...
'''

# Verificando o tipo da função de um modo diferente
def dumb():
    return [1, 2, 3, 4, 5]

var = dumb()
print(var, type(dumb()))