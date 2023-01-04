'''
Aula 11 - Operadores lógicos + condicionais parte 1
- and, or, not
- in e not in
'''

#  Uso do NOT

a = 2
b = 3
if b > a:
    print('B maior que A')
else:
    print('A maior que B')
#  print: B maior que A

#  Aplicando o NOT na expressão verdadeira
if not b > a:
    print('B maior que A')
else:
    print('A maior que B')
#  print: A maior que B
#  Not esta negando uma verdade lógica, logo


#  string vazio
c = ''
d = 0
if c:
    print('por favor preencha o valor de c')
else:
    print('por favor preencha o valor de d')
#  Printa: por favor preencha o valor de d

#  Not C
if not c:
    print('por favor preencha o valor de c')
else:
    print('por favor preencha o valor de d')
#  printa: por favor preencha o valor de c


#  f = 0 (vazio), string com valor
e = 'husdhsudusd'
f = 0
if e:
    print('por favor preencha o valor de e')
else:
    print('por favor preencha o valor de f')
#  printa: por favor preencha o valor de E


# not E
if not e:
    print('por favor preencha o valor de e')
else:
    print('por favor preencha o valor de f')
#  printa: por favor preencha o valor de F
#  OBS: 0 pode ser considerado um boolean False





