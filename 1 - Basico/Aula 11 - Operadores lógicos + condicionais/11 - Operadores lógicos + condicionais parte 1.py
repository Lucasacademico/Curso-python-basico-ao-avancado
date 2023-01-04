'''
Aula 11 - Operadores lógicos + condicionais parte 1
- and, or, not
- in e not in
'''

#  Utilização do AND
a = 2
b = 2
c = 3
exp = a == b and b < c
print(exp)
#  printa: True

#  Revertendo operador lógico do AND
exp = not a == b and not b < c
print(exp)
#  printa: False
#  o NOT, serve para negar uma expressão (chamado de inversor de valores).
#  Obs: no END, ambas as expressões devem ser verdadeiras para receber o TRUE

#  Utilização do OR
exp = a == b or b < c
print(exp)
#  printa: True
#  Obs: no OR, apenas uma deve ser verdadeira para ser TRUE, caso ambas sejam falsas, valor será FALSE


