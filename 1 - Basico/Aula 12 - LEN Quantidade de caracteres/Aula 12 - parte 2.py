'''
Aula 12 - LEN - Quantidade de caracteres - parte 2
- Função de checagem de quantidade de caracteres dentro de uma string
- Funciona com STring e outros tipos de dados (ainda não informado)
- Não funciona com float e/ou int
'''

#  Função LEN com condicionais
usuario = input('Digite seu usuário: ')
qtd_caracteres = len(usuario)
if qtd_caracteres < 6:
    print('Digite no minimo 6 caracteres!')
else:
    print('Cadastrado no sistema')

