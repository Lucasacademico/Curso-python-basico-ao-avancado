
'''
Introdução à formatação de Strings

Anteriormente aprendemos que para podemos inserir variaveis e textos em uma mesma função para mostrar
um texto com as informações contidas das variaveis.
    ex:

'''

nome = 'Lucas Andrade'
idade = 28
altura = 1.79
peso = 120
imc = peso/(altura ** 2)

#  Maneira não-convencional de printar variaveis com strings em um texto
print(nome, 'tem', idade, 'anos de idade e seu IMC é', imc)
    #  printa: Lucas Andrade tem 28 anos de idade e seu IMC é 37.452014606285694

#  Maneira convencional e correta de printar variaveis com strings em um texto
print(f'{nome} tem {idade} anos de idade e seu IMC é {imc:.2f}')
    #  printa: Lucas Andrade tem 28 anos de idade e seu IMC é 37.45

print('{} tem {} anos de idade e seu IMC é {}'.format(nome, idade, imc))
    #  printa: Lucas Andrade tem 28 anos de idade e seu IMC é 37.45
    #  OBS: para formatar o float do IMC, devemos inserir a função de formatação dentro da chave do imc

print('{0} tem {1} anos de idade e seu IMC é {2}'.format(nome, idade, imc))
    #  printa: Lucas Andrade tem 28 anos de idade e seu IMC é 37.45
    #  Atribução de numeros conforme variavel (deve seguir esta ordem)

print('{0} {0} tem {1} {1} anos de idade e seu IMC é {2} {1}'.format(nome, idade, imc))
    #  printa: Lucas Andrade Lucas Andrade tem 28 28 anos de idade e seu IMC é 37.452014606285694 28
    #  reutiliza os dados das Variaveis, bastando repetir a chave com o numero dentro

print('{n} tem {i} anos de idade e seu IMC é {im}'.format(n=nome, i=idade, im=imc))
    #  printa: Lucas Andrade tem 28 anos de idade e seu IMC é 37.45
    #  neste exemplo atribuimos parametros nas variaveis, para invocarmos as infos das var's utilizando....
    #  ... os parametros atribuidos.




'''
1 - Nos dois casos acima a formatação muda completamente, para seguir da maneira correta deve seguir os
seguintes passos:
    1 - inserir a função print()
    2 - inserir um f'' dentro da função print, ficando - print(f'')
    3 - dentro das aspas de f'', inserir o texto normalmente
    4 - nas partes que devem conter as variaveis, inserir uma chave {}, com o nome da variavel dentro

2 - No terceiro caso, é diferente, basta inserirmos chaves nos locais que a variavel deverá se mostrar 
no texto, e aplicar a função .format()
ex:
    supondo que:
    var0 = x
    var1 = y
    var2 = z

    print('alguma coisa {0} outra coisa {1} e mais outra {2}'.format(var0, var1, var2))
        Printa: alguma coisa x outra coisa y e mais outra z
    - Neste exemplo, as variaveis devem seguir a ordem das chaves para colocar as variaveis em seus
    respectivos locais.
    - Os numeros dentro da variavel não servem somente para mostrar os valores são referente as variaveis,
    mas tambem servem para demarcar que aquela chave com o numero dentro, sempre poderá ser repetida e re-
    utilizada.
    
    Ainda nesta explicação de como podemos seguir com a função .format, e seguindo o mesmo exemplo, podemos
    reutilizar a chave configurada com a variavel
    ex:
        print('alguma coisa {0} {0} {0} outra coisa {1} {0} e mais outra {2} {2}'.format(var0, var1, var2))
        printa: alguma coisa x x x outra coisa y x e mais outra z z
            Perceba que no exemplo as chaves foram reutilizadas, independente do local atribuido.

2.1 - podemos ir mais alem na função .format, atribuindo parametros nas variaveis.
ex:
    print('{n} tem {i} anos de idade e seu IMC é {imc}'.format(n=nome, i=idade, im=imc))
      printa: Lucas Andrade tem 28 anos de idade e seu IMC é 37.45
      neste exemplo atribuimos parametros nas variaveis, para invocarmos as infos das var's utilizando....
      ... os parametros atribuidos.
            
3 - Outro ponto, é a formatação da varivel IMC, que podemos reduzir a quantidade de numeros após a virgula,
(obviamente) o numero precisa ser do tipo float, e basta que insiramos uma pequena função de formatação
ex: 
        Variavel IMC = 37.452014606285694
        Variavel IMC:.2f = 37.45
    Conforme o exemplo acima, estou dizendo para variavel que ela deve mostrar somente duas casas decimais 
    após a virgula.
'''


