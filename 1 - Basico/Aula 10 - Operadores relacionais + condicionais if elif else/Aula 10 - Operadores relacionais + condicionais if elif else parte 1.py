'''
Aula 10 - Operadores relacionais + condicionais Parte 1
==, igualdade
>, maior que
>=, maior ou igual a
<, menor que
<= menor ou igual a
!= diferente
'''

#  Diferença entre = e ==

variavel = 'valor'
#  Neste caso estou AFIRMANDO que o variavel é igual a 'valor'
print(variavel == 'valor')
#  print: True
#  Neste caso estou PERGUNTANDO se variavel é igual a 'valor'
#  A expressão acima se torna verdadeira, pois antes dela, atribuimos que variavel = 'valor'

print(2 == 2)
#  Print: True
#  Na expressão acima 2 é de fato igual a 2, logo é uma expressão verdadeira
print(2 == 1)
#  Print: False
#  Na expressão acima logicamente 2 NÃO é igual a 1, logo a expressão é falsa


num_1 = 2
num_2 = '2'
print(num_1 == num_2)
#  print: False
#  Nos exemplos acima, pergunto ao sistema se 2 do tipo inteiro é igual a 2 do tipo string.
#  O sistema obviamente irá informar que a expressão é falsa, pois os tipos são diferentes...
#  ... mesmo que visualmente sejam identicas.

val_1 = 2
val_2 = 2
expressao = (val_1 == val_2)
print(expressao)
#  Printa: True
#  Neste exemplo acima atribuimos a variavel 'expressao' recebe o retorno da pergunta lógica...
#  ...de igualdade (que neste caso é verdadeiro)

val_1 = 2
val_2 = 2
expressao = (val_1 > val_2)
print(expressao)
#  Printa: False

val_1 = 3
val_2 = 2
expressao = (val_1 > val_2)
print(expressao)
#  Printa: False

val_1 = 2
val_2 = 2
expressao = (val_1 >= val_2)
print(expressao)
#  Printa: True

#  Usando Strings

exp_1 = 'Lucas'
exp_2 = 'Andrade'
retorno = (exp_1 == exp_2)
print(retorno)
#  Printa: False

exp_1 = 'Lucas'
exp_2 = 'Andrade'
retorno = (exp_1 != exp_2)
print(retorno)
#  Printa: True


#  IMPORTANTE: Se rodarmos este código, a tela retorna a afirmação de VERDADEIRO ou FALSO dependendo...
#  ... da expressão, pois isto é uma pergunta ao sistema.

