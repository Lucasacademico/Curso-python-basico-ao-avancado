
contador = 1
acumulador = 1

while contador <= 10:
    print(contador, acumulador)

    if contador > 5:
        break
    # Quebra o while antes de finalizar, e não executa o else

    acumulador = acumulador + contador
    contador += 1
else:
    print('Cheguei no else')
    # entra no else após o while finalizar seu trabalho
print('execução passando do else')