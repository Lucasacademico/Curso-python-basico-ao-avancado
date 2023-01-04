'''
    Faça um programa que peça o primeiro nome do usuario.
    Se o nome tiver 4 letras ou menos, escreva: "Seu nome é curto"
    Se tiver entre 5 e 6 letras, escreva: "Seu nome é normal"
    Se for maior que 6 letras, escreva: "Seu nome é muito grande".
'''

nome = input("Digite seu nome: ")

qtd_user = len(nome)

if qtd_user <= 4:
    print(f'{nome} é um nome curto')
elif qtd_user > 4 and qtd_user < 7:
    print(f'{nome} é um nome normal')
else:
    print(f'{nome} é um nome muito grande')