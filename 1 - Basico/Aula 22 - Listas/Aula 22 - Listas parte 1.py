'''
    Listas em Python
    - Fatiamento
    - append, insert, pop, del, clear, extend, +
    - min, max
    - range
'''

lista = ['A', 'B', 'C', 'D', 'E', 'F']

# Printando a lista
print(lista)

# printando indice B da lista
print(lista[1])

# alterando um valor da lista
lista[4] = 'X'

# Printando novo valor do indice 5 da lista
print(lista[4])

# Printando apenas 3 valores da lista
print(lista[0:3])
'''
    Observação: No exemplo acima, é printado somente os indices:
    0, 1, 2.
    O 3 não é incluso, logo o comando é o tamanho da exibição, começando
    do 0.
'''

# Simplificando o exemplo acima
print(lista[:3])

# Printando 2 valores a partir do indice 1
print(lista[1:3])

# Pulando de 2 em 2
print(lista[::2])

# Imprimindo de forma invertida
print(lista[::-1])