'''
    Desempacotamento de listas
'''

lista = ['Lucas', 'Rocha', 'Andrade', 1, 2, 3, 4, 5, 6, 7]
# Atribuido uma var para cada valor da lista
n1, n2, n3, *outralista, ultimo_da_lista = lista

# printando somente o valor n2 da lista
print(n2)
print(outralista)
print(ultimo_da_lista)

'''
    Importante: Se apagarmos (por exemplo) o n3, ocorrerá um erro, pois
    para atribuirmos variaveis para os valores da lista, a quantidade de 
    variaveis deve ser igual a quantidade de valores da lista.
    
    Uma maneira de resolver isso é criando uma variavel (com asterisco), 
    e habilitará a possibilidade de printarmos valores infinitamente dentro da lista
    
    podemos também printar o ultimo valor da lista após criarmos a variavel com
    asterisco
    
    é importante destacar que o posicionamento da variavel asterisco atribuida da lista,
    informa quais valores irá pegar
'''