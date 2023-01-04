
# Variavel global
variavel = 'valor'

# Não é possível imprimirmos uma variavel global e local de mesmo nome dentro de uma função
def func():
    print(variavel)
    variavel = 1234
    print(variavel)

func()
