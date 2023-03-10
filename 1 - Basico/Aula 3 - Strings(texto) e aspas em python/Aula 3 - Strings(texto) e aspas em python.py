#  String é um tipo de dado primitivo em python
#  str = string, em python
#  strings são textos dentro de aspas, a grosso modo.
#  O python sabe, que textos/palavras entre '' e "" são strings
#  Números fora de aspas são INTEIROS, e serão printados como inteiros
#  Números dentro de aspas são STRINGS, e serão printados como strings


print('Isso é um texto de umas aspa simples')
print("Isso é um texto de umas aspa duplas")

#  O print do valor abaixo é do tipo inteiro
print(12345)
#  O print do valor abaixo é do tipo string, pois esta dentro das aspas
print('12345')

#  Hierarquia das aspas
print('Isto é um texto "String" ')
print("Isso também é um texto 'String' ")
#  Nos casos acima, podemos perceber que o compilador irá verificar que tipo de aspas o argumento esta envolto
#  Após confirmar, podemos utilizar a outra aspa restante para utilizar a aspa dentro do argumento como parte do texto.
#  Ou seja, o texto entende que a '' faz parte do parâmetro de definição da string, e a "" que esta dentro faz...
#  ... parte do texto dentro do parâmetro.
#  O mesmo serve para o inverso


#  Quebra de linha
print('Isso é um texto com \n quebra de linha')
