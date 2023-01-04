'''
Exercicio
- Suponha que uma pessoa só pode pegar um emprestimo do banco se ela tiver mais do que 18 anos
'''

nome = input('Qual seu nome?  ')
idade = input('Qual sua idade? ')

#  Limite para conseguir emprestimo do banco
maioridade = 18

if int(idade) >= maioridade:
    print(f'O usuário {nome} esta apto à realizar emprestimos no banco do LULU')
else:
    print(f'O usuário {nome} é menor de idade, não esta apto à realizar emprestimos no banco do LULU')

