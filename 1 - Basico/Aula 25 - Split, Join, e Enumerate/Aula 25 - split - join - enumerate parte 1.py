'''
    Split, Join, Enumerate
    - split: Dividir uma string
    - Join: Juntar uma lista
    - Enumerate: Enumerar os elementos da lista
    OBS: São funções de string
'''

string = "O Brasil é o país da alegria, comida, e futebol"
lista = string.split(' ')
lista2 = string.split(',')
print(lista)
print(lista2)

'''
A função split irá separar a string em itens conforme o comando do usuario, exemplo:

    split(' ') - Separa os itens conforme os espaços entre elas, ficando
    10 itens separados por espaço
    
    split(',') Separa os itens conforme as virgulas no texto, ficando
    3 itens separados por virgulas
'''



