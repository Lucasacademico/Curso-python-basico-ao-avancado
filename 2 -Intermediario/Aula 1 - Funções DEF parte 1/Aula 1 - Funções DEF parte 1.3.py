
# usando funções dentro de funções
def funcao(msg = 'Olá', nome = 'Lucas'):
    nome = nome.replace('a', '4')
    msg = msg.replace('á', '4')
    print(msg, nome)

funcao()

# pula linha
print()

# usando Return em vez de print
def saudacao(msg ='Olá', nome ='Lucas'):
    nome = nome.replace('a', '4')
    msg = msg.replace('á', '4')
    return f'{msg} {nome}'

variavel = saudacao()
print(variavel)