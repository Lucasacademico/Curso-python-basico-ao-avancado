'''
Tipos de dados:
- str: string
    ex: "isto é uma string", 'isso tbm é uma string'

- int: inteiro
    ex: 123456, 10, 5000.....

- float: real/ponto flutuante
    ex: -23  244.23  -33.55  0.0

- bool: booleano/lógico
    ex: false or true

O interpretador do python já consegue entender a tipagem de dado, desde que insiramos do modo correto.
'''

#  Retornando o tipo de dado

print('Lucas', type('Lucas'))
#  printará: Lucas <class 'str'>, que é o tipo de dado string do nome Lucas

print('1234', type('1234'))
#  printará: 1234 <class 'str'>, que é o tipo de dado STRING pois o número esta em formato string

print(1234, type(1234))
#  printará: 1234 <class 'int'>, que é o tipo de dado INT do numero 1234

print(28.6, type(28.6))
#  printará: 28.6 <class 'float'>, que é o tipo de dado FLOAT do numero 28.6

print(10 == 10, type(10 == 10))
#  printará: True <class 'bool'>, que é o tipo de dado BOOLEANO da afirmação 10 == 10

print('L' == 'L', type('L' == 'L'))
#  printará: True <class 'bool'>, que é o tipo de dado BOOLEANO da afirmação 'L' == 'L'

print('l' == 'L', type('l' == 'L'))
#  printará: False <class 'bool'>, que é o tipo de dado BOOLEANO da afirmação 'l' == 'L'


#  Type Cashing

print('Lucas', type('Lucas'), bool('Lucas'))
#  Faz com que 'Lucas' do tipo 'str', converta para 'bool', retornando 'True'
#  Printa: Lucas <class 'str'> True

print('10', type('10'), type(int('10')))
#  Faz com que a string '10', do tipo 'str', retorte o valor convertido do 10 que era string, porém foi transformado
#  ...em inteiro
#  printa: 10 <class 'str'> <class 'int'>

#  Importante: não é possível a utilização do type cashing em todos os tipos, o exemplo disso é que podemos alterar...
#  ... um numero do formtato string em inteiro, mas não podemos transformar uma palavra string em inteiro, pois não...
#  ... é lógico.
