'''
    2 - Crie uma funcao1 que recebe uma funcao2 como parâmeetro e retorne o valor da funcao2
    executada. Faça a funcao1 executar duas funções que recebam um número diferente de argumentos
'''

def funcao1(saudacao='olá'):
    return f'{saudacao}'

def funcao2(nome='Lucas', sobrenome='Andrade'):
    return f'{nome}{sobrenome}'

def mestre(*args):
    print(args)

var1 = funcao1()
var2 = funcao2()
mestre(var1, var2)

print('------------------------')

def mestre(funcao):
    return funcao()

def fala_oi(nome):
    return f'Oi {nome}'

def saudacao{nome, saudacao}
    return {saudacao} {nome}

executando = mestre(saudacao)
