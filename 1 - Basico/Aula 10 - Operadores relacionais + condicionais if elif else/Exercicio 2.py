'''
Exercicio
- Suponha que uma pessoa só pode pegar um emprestimo do banco se ela tiver entre 20 e 30 anos
'''

nome = input('Qual seu nome?  ')
idade = input('Qual sua idade? ')

#  Limite para conseguir emprestimo do banco
limite_minimo = 20
limite_maximo = 30

if int(idade) >= limite_minimo and int(idade) <= limite_maximo:
    print(f'O usuário {nome} esta apto à realizar emprestimos no banco do LULU')
else:
    print(f'O usuário {nome} Não esta dentro do padrão de idade necessário')