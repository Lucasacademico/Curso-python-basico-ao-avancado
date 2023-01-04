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

nome = 'Lucas Andrade'
nome = nome.ljust(20, '#')
print(nome)
# Essa função preenche o nome com o caracter # até chegar o total de 20 caracteres na variavel.

nome = 'Lucas Andrade'
nome = nome.lower()
print(nome)
# Printa o nome o nome da variavel minuscula

nome = 'Lucas Andrade'
nome = nome.upper()
print(nome)
# Printa o nome o nome da variavel maiuscula

nome = 'Lucas Andrade'
nome = nome.title()
print(nome)
# Printa o nome da variavel em formato de titulo (cada inicio de palavra em maiusculo)

print() # Pula linha

nome = 'Lucas Andrade'
print(nome.lower()) # tudo minusculo
print(nome.upper()) # tudo maiusculo
print(nome.title()) # primeiras letras maiusculas
# podemos printar as funções diretamente no print.


