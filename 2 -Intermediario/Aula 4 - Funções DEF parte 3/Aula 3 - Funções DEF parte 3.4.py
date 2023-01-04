

def func(*args):
    print(args)

lista = [1, 2, 3, 4, 5]
func(lista, '6')
# Adicionando um valor a mais no momento da impressão, faz com que a lista e o novo valor...
# ... fiquem dentro da tupla, porém separados

print('-------------')
def func(*args):
    print(args)
lista = [1,2,3,4,5]

# lista empacotada na tupla
func(lista)
# lista empacotada na tupla adicionando novos valores
func(lista, 10, 20, 30, 40, 50)
# lista desempacotada na tupla
func(*lista)
# lista desempacotada adicionando novos valores
func(*lista, 10, 20, 30, 40, 50)