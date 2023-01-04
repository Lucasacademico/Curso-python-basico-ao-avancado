
lista = [
    [1,2],
    [3,4],
    [5,6],
]

for v in lista:
    print(v[0], v[1])

print()

lista = [
    [0, 'Lucas'],
    [1, 'Rocha'],
    [2, 'Andrade'],
]
for indice, valor in lista:
    print(indice, valor)

print()
# usando a função enumerate
lista = ['Lucas', 'Rocha', 'Andrade']
for indice, nome in enumerate(lista):
    print(indice, nome)
    # A Função enumerate facilita o print de indices e valores