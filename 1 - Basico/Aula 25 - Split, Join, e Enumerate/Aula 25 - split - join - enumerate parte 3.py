
string = "O Brasil é o país da alegria, comida, e futebol"
lista1 = string.split(' ')
lista2 = string.split(',')

#printar a quantidade de palavras da lista 1
for valor in lista1:
    print(f'A palavra "{valor}" apareceu {lista1.count(valor)} x na frase')