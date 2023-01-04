
# função usando variaveis
nome1 = 'Lucas'
nome2 = 'Nagila'
mensagem = 'Olá me chamo: '

def funcao():
    print(f'{mensagem}{nome1}')

funcao()

# Pula linha
print()

# criando variaveis dentro do parametro da função
def funcao(msg = 'Olá', nome = 'Usuario'):
    print(msg, nome)

funcao()
# Definindo parte da variavel da func
funcao(nome = 'Zézinho')
