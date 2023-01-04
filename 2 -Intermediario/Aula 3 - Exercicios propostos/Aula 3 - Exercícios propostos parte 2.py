'''
    2 - Crie uma função que recebe 3 numeros como parametro e exiba
    a soma entre eles


'''

def soma(n1 = 1, n2 = 2, n3 = 3):
    return n1 + n2 + n3

somando = soma()
print(somando)

print('--------------')

def soma(n1, n2, n3):
    print(n1 + n2 + n3)

soma(1, 2, 3)
soma(3, 5, 7)