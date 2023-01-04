'''
    Formatando valores com modificadores - Aula 16

    :s - Texto (strings)
    :d - Inteiros(int)
    :f - Numeros de pontos flutuantes (float)
    :.(numero) - Quantidade de casas decimais (float) - :.2f
    : (caractere) (> ou < ou ^) (quantidade) (tipo - s, d, ou f)

    > - Esquerda
    < - Direita
    ^ - Centro
'''

num_1 = 10
num_2 = 3
divisao = num_1 / num_2
print('{:.2f}'.format(divisao))
print(f'{divisao:.2f}')
# printa: 3.33
# Nas variaveis acima apenas corrig a formatação do resultado da div

nome = 'Lucas Andrade'
print(f'{nome:s}')
# printa: Lucas Andrade
# No print acima estou informando que a variavel nome é uma string

num_1 = 1
print(f'{num_1:0>10}')
# printa: 0000000001
# Formatando a var num_1 para ter dez casas para esquerda (adicionando 9 zeros antes do 1).

num_2 = 1150
print(f'{num_2:0>10}')
# printa: 0000001150
# Formatando a var num_2 para ter dez casas para esqueda (adicionando 6 zeros antes do 1150).

num_3 = 1111
print(f'{num_3:0<10}')
# printa: 1111000000
# Formatando a var num_3 para ter dez casas para direita (adicionando 6 zeros depois do 1150).

num_4 = 2222
print(f'{num_4:0^10}')
# printa: 0002222000
# Formatando a var num_4 para ter dez casas (inserindo o 2222 no centro de zeros).

num_5 = 3333
print(f'{num_5:.2f}')
# Formatando a var num_5 transformando o inteiro em float).
# printa: 3333.00

num_6 = 4444
print(f'{num_6:0>10.2f}')
# Formatando a var num_6 transformando o inteiro em float).

nome = 'Lucas Andrade'
nome_formatado = '{}'.format(nome)
print(nome_formatado)
# O exemplo acima irá printar somente o nome Lucas Andrade, visto que dentro das chaves
#... não é inserido qualquer informação para formatação

nome = 'Lucas Andrade'
nome_formatado = '{:@>50}'.format(nome)
print(nome_formatado)
# printa: @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@Lucas Andrade

nome = 'Lucas Andrade'
nome_formatado = '{n} {n} {n}'.format(n=nome)
print(nome_formatado)
# printa: Lucas Andrade Lucas Andrade Lucas Andrade

nome = 'Lucas Andrade'
nome_formatado = '{n:0^20}'.format(n=nome)
print(nome_formatado)
# printa: 000Lucas Andrade0000

nome = 'Lucas'
nome_meio = 'Rocha'
nome_final = 'Andrade'
nome_formatado = '{0} {1} {2}'.format(nome, nome_meio, nome_final)
print(nome_formatado)
# printa: Lucas Rocha Andrade

