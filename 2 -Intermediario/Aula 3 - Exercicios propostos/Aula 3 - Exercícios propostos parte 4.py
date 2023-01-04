'''
    4 - Fizz Buzz - Se o parâmetro da função for divisível por 2, retorne fizz
    se o parâmetro for divisível por 5. Retorne buzz. Se o parâmeto da função for
    divisivel por 5 e por 3, retorne FizzBuzz, caso contrario, retorne o numero
    enviado.
'''

def funcao(val = 5):
    if val % 5 == 0 and val % 3 == 0:
        return 'FizzBuzz'
    elif val % 5 == 0:
        return 'Buzz'
    elif val % 2 == 0:
        return 'Fizz'
    else:
        return val

variavel = funcao()
print(variavel)

print('-------------')

def funcao(val):
    if val % 5 == 0 and val % 3 == 0:
        return 'FizzBuzz'
    elif val % 5 == 0:
        return 'Buzz'
    elif val % 2 == 0:
        return 'Fizz'
    else:
        return val

print(funcao(15))