string = "O Brasil é o país da alegria, comida, e futebol. Brasil"
lista1 = string.split(' ')
lista2 = string.split(',')

palavra = ''
contagem = 0

# função pra mostrar a palavra qe mais aparece na frase
for valor in lista1:
    qtd_vezes = lista1.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f'A palavra que apareceu mais vezes: "{palavra}" {contagem}x')
