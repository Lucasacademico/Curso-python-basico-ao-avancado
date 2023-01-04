
variavel = ['lucas', 'Rocha', 'Andrade']

# Verificar se uma palavra com a letra R
for valor in variavel:
    if valor.startswith('R'):
        print(f'{valor} Começa com R')
    else:
        print(f'{valor} não começa com R')


print()

# confirmar se existe uma letra utilizando boolean
comeca_com_l = False
for valor in variavel:
    # lower() - transforma a verificação para letras minusculas
    if valor.lower().startswith('l'):
        comeca_com_l = True

if comeca_com_l:
    print('Existe uma palavra que começa com L')
else:
    print('Não existe uma palavra que começa com L')


print()
# O For também suporte a função else (for/else)
variavel = ['João', 'Matheus', 'antonio']

comeca_com_a = False
for valor in variavel:
    if valor.lower().startswith('a'):
        comeca_com_a = True
else:
    print('Não existe uma palavra que começa com a')

print()
# Diminuindo mais ainda o código
variavel = ['João', 'Matheus', 'antonio']
for valor in variavel:
    print(valor)
    if valor.lower().startswith('J'):
        break
else:
    print('Não existe uma palavra que começa com J')