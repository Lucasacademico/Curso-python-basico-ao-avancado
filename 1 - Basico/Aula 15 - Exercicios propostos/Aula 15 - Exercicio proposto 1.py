'''
Faça um programa que peça ao usuario para digitar um numero inteiro,
informe se este número é par ou impar. Caso o usuário não digite um numero
inteiro, informe que não é um numero inteiro.
'''

num1 = input('Digite um numero')

if num1.isdigit():
    num1 = int(num1)

    if num1 % 2 == 0:
        print(f'{num1} é par')
    else:
        print(f'{num1} é impar')

else:
    print('O valor digitado não é inteiro')
