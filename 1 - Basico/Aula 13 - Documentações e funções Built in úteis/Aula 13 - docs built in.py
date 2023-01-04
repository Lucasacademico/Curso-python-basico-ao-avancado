'''
O intuito dessa aula é mostrar a importancia de leitura da documentação python,
e fazer com que erros criados propositalmente pelos usuarios, não quebrem o código
e sim informem o erro ao usuario.
'''



num1 = input('Digite um numero: ')
num2 = input('Digite outro numero: ')

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)

    print(num1 + num2)

else:
    print('Não pode converter os numeros para realizar as contas.')