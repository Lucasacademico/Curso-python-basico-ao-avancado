'''
Input: Entrada de dados do usuário - parte 1
'''

nome = input("Qual o seu nome? ")
#  A função input("Qual o seu nome?" ) possibilita que o usuário digite seu nome porém nao armazena em variavel
#  Atribuir a variavel nome = input("Qual o seu nome?" ) informa que o digitado pelo usuário será salvo na
#  ... variavel nome
#  Caso o usuário digite um numero, será uma numero no formato string

idade = input("Qual a sua idade? ")

ano_nascimento = 2022 - int(idade)
'''
Nesta declaração de ano_nascimento, se tentarmos subtrair o 2022 pelo valor dade idade que é string, ocorrerá
um erro, pois inteiros não subtraem de strings.
Entretanto, se realizarmos a conversão da idade para inteiro - int(idade), ai conseguimos realizar a subtração
'''

print()
print(f'{nome} tem {idade} anos '
      f'{nome} nasceu em em {ano_nascimento}')
#  Na frase estamos confirmando tanto o nome e a idadeque o usuário digitou, quanto o tipo do valor digitado.


