
# Variavel em escopo global
variavel = 'valor'

# Função acessando a variavel do escopo global
def func():
    print(variavel)

def func2():
    # Alterando uma variavel global dentro de uma função
    # obs: não é uma boa pratica
    global variavel
    # Variavel de escopo local
    variavel = 'Outro Valor'
    print(variavel)

func()
func2()

# printando a variavel de escopo global
print(variavel)