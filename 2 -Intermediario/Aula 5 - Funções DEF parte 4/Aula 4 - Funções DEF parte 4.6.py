
variavel = 'valor'

# não é possível printarmos uma variavel de uma função x em uma função y
def func():
    outra_variavel = 'valor'

def func2():
    print(outra_variavel)

func()
func2()