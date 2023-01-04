'''
Variáveis
- Uma variavel pode iniciar com letra, pode conter números, separar com underline (_), e pode ser utilizado letras
minusculas
- o simbolo de igual (=) é considerado um operador de atribuição nas variáveis
- Uma variável pode conter numeros, porém o nome da variavel não pode iniciar com numeros
'''

#  Atribuição de valores nas variaveis
nome = 'Lucas'
idade = 28
altura = 1.79
e_maior = idade > 18
peso = 120


#  Exemplo de uso básico

print(nome)
#  print(nome) - irá printar o nome 'Lucas' que foi atribuido na variavel 'nome'

print(nome, type(nome))
#  Podemos também verificar o tipo da variavel com função 'type()'


#  pula linha
print()


#  Exempo de uso comum
print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
print('É maior:', e_maior)
print('Peso:', peso)

#  pula linha
print()

#  Operações entre variaveis
print(idade * altura)

