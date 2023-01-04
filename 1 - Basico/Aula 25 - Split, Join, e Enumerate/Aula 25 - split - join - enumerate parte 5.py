
string = 'O Brasil é o o o país do futebol, o Brasil é penta'
lista_1 = string.split(' ')
lista_2 = string.split(',')


for valor in lista_2:
    print(valor.strip().capitalize())
    # função strip tira o espaço da quebra de linha
