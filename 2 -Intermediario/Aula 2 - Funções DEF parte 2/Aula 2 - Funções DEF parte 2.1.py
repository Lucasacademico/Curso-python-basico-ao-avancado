'''
    Funções DEF em python parte 2
'''

# Podemos declarar variaveis dentro da função, e expecificar o valor fora da função
def funcao(var):
    print(var)

funcao('Valor que eu quero')

print('---------------------')

# Variavel recebendo a função, e printando a variavel que recebe a função
def funcao(var):
    print(var)

variavel = funcao('Variavel recebendo a função')
print(variavel)
# Aqui retorna também um none

print('---------------------')

# Maneira errada de retornar uma funcão
def funcao(var):
    # aqui estamos usando o print
    print(var)

variavel = funcao('valor da função na variavel')

if variavel:
    print(variavel)
else:
    print('nenhum')
# Deste modo printará tanto o IF quanto o Else

print('---------------------')

# Maneira correta de retornar uma função
def funcao(var):
    # aqui estamos usando o return
    return var

variavel = funcao('valor da função na variavel')

if variavel:
    print(variavel)
else:
    print('nenhum')
# Deste modo, será printado somente o valor do IF, sem o valor de Else