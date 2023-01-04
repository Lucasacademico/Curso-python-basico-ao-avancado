'''
Criar autenticação de usuário e senha
'''

user = input('Nome do Usuário: ')
senha = input('Senha: ')

usuario_bd = 'Lucas'
senha_bd = '123'

if user == usuario_bd:
    print()
else:
    print('Usuario incorreto')

if senha == senha_bd:
    print()
else:
    print('Senha incorreta')

if user == usuario_bd and senha ==  senha_bd:
    print('Acesso Liberado')
else:
    print('Acesso Negado')