'''
Aula 12 - LEN - Quantidade de caracteres - parte 1
- Função de checagem de quantidade de caracteres dentro de uma string
- Funciona com STring e outros tipos de dados (ainda não informado)
- Não funciona com float e/ou int
'''

#  Primeiro alocamos uma String para a variavel String
usuario = input('Digite seu usuário: ')

#  Criamos uma variavel para receber a informação da quantidade de caracteres do usuário
qtd_caracteres = len(usuario)
#  len(usuario), informa a quantidade de caracteres inserida pelo usuario
#  qtd_caracteres, recebe o valor da função len() em inteiro

print(usuario, qtd_caracteres ,type(qtd_caracteres))
#  printa: Lucas 5 <class 'int'>
#  Resumindo, printa o nome do usuário, quantidade de caracteres, e o tipo da variavel de qtd de caract..
