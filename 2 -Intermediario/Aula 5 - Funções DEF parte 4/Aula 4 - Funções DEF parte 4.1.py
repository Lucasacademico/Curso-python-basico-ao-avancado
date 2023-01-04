'''
    Escopos de variaveis em python
'''

# Variavel em escopo global
variavel = 'valor'

# Função acessando a variavel do escopo global
def func():
    print(variavel)

# Outra função aproveitando também a variavel do escopo global
def func2():
    print(variavel)

func()
func2()