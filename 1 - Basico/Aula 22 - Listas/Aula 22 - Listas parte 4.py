
# Somando os valores da lista
l1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

soma = 0
for valor in l1:
    soma = soma + valor
    print(f'{soma} + {valor} = {soma}')
print(soma)

print()
# Mostrando os tipos de dados de uma lista utilizando o for
l2 = [1, 2.4, True, 'Lucas']

for valor in l2:
    print(f'Valor: {valor}, tipo: {type(valor)}')