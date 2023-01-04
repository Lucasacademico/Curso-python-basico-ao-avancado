
idade = input('Qual sua idade? ')
if not idade.isnumeric():
    print('Digite apenas numeros')
else:
    idade = int(idade)
    maioridade = (idade >= 18)
    msg = 'Pode acessar o site' if maioridade else 'Não pode acessar o site'

print(msg)