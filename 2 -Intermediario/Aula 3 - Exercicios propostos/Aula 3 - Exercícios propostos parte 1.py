'''
    1 - Crie uma funão que exibe uma saudação com os parâmetros
    saudação e nome


'''


def funcao(saudacao = 'Olá', nome = 'Lucas'):
    return f'{saudacao} {nome}'

variavel = funcao()
print(variavel)

print('--------------')

def funcao(saudacao, nome):
    print(f'{saudacao} {nome}')

funcao('Olá', 'Lucas')
funcao('Oi', 'Nagila')