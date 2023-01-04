
# Soma de listas (obs: concatena os valores da lista
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = l1 + l2
print(l3)

# A função extend adiciona os vals da l2 na l1...
# ... porém, os valores da l2 continuam o mesmo se printados separadamente.
print()
l1.extend(l2)
print(l1)
print(l2)

# Adicionando um valor qualquer na l1
print()
l1.extend('a')
print(l1)
print(l1)

# Adicionando um valor com a função append na l2
print()
l2.append('b')
print(l2)

'''
    extend e append são bem equivalentes, o correto é utilizar o 
    extend para concatenar valores em uma lista, e o append para 
    adicionar um valor na lista
'''