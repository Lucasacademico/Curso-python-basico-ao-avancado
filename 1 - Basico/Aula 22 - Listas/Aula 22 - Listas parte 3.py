
# Adicionando valores com o insert em um indice específico
l2 = [4, 5, 6]

l2.insert(1, 'Lucas')
print(l2[1])

# Removendo um valor da lista com o pop
print()
print('Lista Atual', l2)
l2.pop() # Excluindo o ultimo indice da lista com o pop
print(l2)

print()

# Excluindo indices de 3 a 4 com a função del
l3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(l3)
del(l3[3:5]) # lembrando que é de 3 a 4 (escrito com 3:5
print(l3)

# Printando o maximo e minimo de uma lista
print()
l4 = [5, 10, 15, 20, 25, 30, 35, 40, 45]
print(max(l4))
print(min(l4))

# Printando um range de valores em uma lista com função list
print()
l5 = list(range(1, 10))
print(l5)

# Printando um range de valores em uma lista (de 8 em 8) com função list
print()
l5 = list(range(0, 100, 8))
print(l5)

# Printando valores de uma lista com for
print()
l6 = list(range(0, 100, 20))
for valor in l6:
    print(valor)