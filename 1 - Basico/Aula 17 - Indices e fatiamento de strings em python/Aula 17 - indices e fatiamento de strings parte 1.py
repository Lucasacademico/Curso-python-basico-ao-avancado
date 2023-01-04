'''
    Manipulando strings = Aula 17
    * String indices
    * Fatiamento de strings (inicio:fim:passo)
    * Funções Built-in len, abs, type, print, etc...

    Site para conferir:
    https://docs.python.org/3/library/stdtypes.html
    https://docs.python.org/3/library/functions.html
'''

# possui 9 indices positivos (0 a 8) (carateres da variavel texto)
texto = 'Python S2'
print(texto[2])
# Printamos o indice 2 do texto, que é o char 't'
# se colocarmos o indice 6, não printará nada, pois neste indice é o espaço

# Abaixo faremos o mesmo processo, porém utilizando indices negativos
texto = 'Python S2'
print(texto[-9])

'''
    Exemplo:
        [012345678] - Indice Positivo
        'Python S2'
       -[987654321] - Indice Negativo
        
        print(texto[4]) 
            printará: o (que é o indice positivo 4)
            
        print(texto[-8])
            printará: y (que é o indice negativo -8)
'''

url = 'www.google.com.br/'
# Se printarmos a URL, printará o endereço junto com a /
print(url)
# Se printarmos a url fatiando a /
print(url[:-1])
# No exemplo acima o -1 na url retirará a / da url.

