
# juntando listas em tuplas
def func(*args):
    print(args)

lista1 = [1,2,3,4,5]
lista2 = [10,20,30,40,50]
func(*lista1, *lista2)


# Usando o Kwargs
def func(*args, **kwargs):
    print(args)
    print(kwargs)

lista = [1,2,3,4,5]
func(*lista, nome='Lucas', sobrenome='Andrade')
'''
    Lista é printada em cima do args, e nome é printado em cima do kwargs
'''

print('------------------------')
# Usando o kwargs da maneira correta
def func(*args, **kwargs):
    print(args)
    print(kwargs['nome'], ['sobrenome'])

lista = [1,2,3,4,5]
func(*lista, nome='Lucas', sobrenome='Andrade')

print('------------------------')

