
string = "O Brasil é o país da alegria, comida, e futebol"
lista = string.split(' ')
lista2 = string.split(',')
print(lista)
print(lista2)

# printar cada palavra splitada da lista 1 por espaço
for valor in lista:
    print(valor)

print()

# printar cada palavra splitada da lista 2 por virgula
for valor in lista2:
    print(valor)