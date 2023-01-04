'''
    Faça um programa que pergunte a hora ao usuario e, baseando-se no horario
    descrito, exiba a saudação apropriada. Ex: bom dia (0-11), boa tarde (12-17)
    boa noite (18-23).
'''

hora = input('Digite a hora atual: ')

if hora.isdigit():
    hora = int(hora)

    if hora >= 0 and hora <= 11:
        print('Bom dia flor do dia')
    elif hora >= 12 and hora <= 17:
        print('Boa tarde flor da tarde')
    elif hora >= 18 and hora <= 23:
        print('Boa noite flor da noite')
    else:
        print('Valor incorreto')
else:
    print('Valor incorreto')