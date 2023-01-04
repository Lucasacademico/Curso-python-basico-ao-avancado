'''
Desafio antes de continuar
*Criar variáveis para nome(str), idade(int), altura(float), e peso(float) de uma pessoa;
*Criar variavel com o ano atual
*Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
*Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
*Exibir um texto com todos os valores na tela usando F-Strings (com as chaves)

'''

nome = 'Lucas Rocha'
idade = 28
altura = 1.79
peso = 120.58
ano = 2022
nascimento = ano - idade
imc = peso/(altura ** 2)

print(f'Hoje em {ano}, {nome} tem {idade} de idade, nascido em {nascimento}')
print(f'Possui{altura} de altura, 'f'pesando {peso}')
print(f'Seu IMC é de {imc}')