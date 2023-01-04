
def divisao(n1, n2):
    if n2 > 0:
        return n1 / n2

divide = divisao(9,2)

if divide:
    print(divide)
else:
    print('Conta invalida')
# OBS: O divisor não pode ser zero (0)

print('---------------------')

# Mesmo resultado, modo diferente
def divisao(n1, n2):
    if n2 == 0:
        return

    return n1 / n2

divide = divisao(8, 0)

if divide:
    print(divide)
else:
    print('Conta invalida')