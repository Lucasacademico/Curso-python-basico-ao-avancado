
# Podemos criar uma função para passar uma informação
def func(*args, **kwargs):
    idade = kwargs.get('idade')
    print(idade)

func(idade=21)

print('-------------------')

# mostrando um valor inexistente
def func(*args, **kwargs):
    print(args)

    # valor idade não declarado
    nome = kwargs.get('idade')
    if idade is not None:
        print(idade)

lista = [1,2,3,4,5]
lista2 = [10, 20, 30, 40, 50]
func(*lista, *lista2, nome='Lucas', sobrenome='Andrade')