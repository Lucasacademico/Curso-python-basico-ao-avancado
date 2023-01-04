'''
    Utilizar estrutura de repetição (for ou While)
    - Criar dois contadores dentro do mesmo laço
    - Um contador de 0 a 8, e outro de 10 a 2
'''

x = 10
y = 0

# usando While
while x >= 2 and y >= 0:
    print(x, y)
    x -= 1
    y += 1

    if x == 2 and y == 8:
        print(x, y)
        break