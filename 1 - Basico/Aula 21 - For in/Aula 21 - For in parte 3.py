'''
    Função range(start = 0, stop, step = 1)
'''

# For de 1 a 10
for n in range(10):
    print(n)


print()

# For de 5 à 10
for n in range(5, 10, 1):
    print(n)

print()

# FOr de 20 à 10
for n in range(20, 10, -1):
    print(n)

print()

# For de 1 a 10 pulando de 2 em 2
for n in range(0, 10, 2):
    print(n)

print()

# For de 1 a 100 pulando de 8 em 8
for n in range(0, 100, 8):
    print(n)

print()

# Encontrando multiplos de 8 (de 0 a 100)
for n in range(100):
    if n % 8 == 0:
        print(n)