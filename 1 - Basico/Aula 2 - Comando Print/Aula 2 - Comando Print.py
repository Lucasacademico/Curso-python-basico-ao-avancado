
#  comando para printar uma mensagem na tela
#  No exemplo abaixo mostra como printamos numeros inteiros
print(12345)

#  Print de Strings
#  No exemplo abaixo, as virgulas separam argumentos dentro da função print
print('Joao', 'Maria', 'Silva')

#  No exemplo abaixo um texto pode ser inserido dentro de um unico argumento da função print
print('Isto é um texto exemplo')

#  No exemplo abaixo o print possui uma função separadora, que serve para separar os argumentos conforme o descrito..
#  ... dentro da função sep=''
#  exemplo1: sep='-', ira printar Joao-Maria
#  exemplo2: sep='x', irá printar JoaoxMaria
#  Obs: O separador irá funcionar entre TODOS os argumentos dentro do print
print('Joao', 'Maria', sep='-')

#  No exemplo abaixo, a função end='x', serve para inserir algum simbolo, ou qualquer coisa no final dos argumentos...
#  ... dentro do print.
#  No código abaixo, será printado na tela a seguinte informação:Pedro-Joséx
print('Pedro', 'José', sep='-', end='x')

print('João', 'Maria', sep='-', end='######')
#  OBS: Se por acaso, no print anterior inserirmos um end sem nenhuma atribuição, end='', o código irá se juntar com
#  ... um código seguinte (se houver), pois o end sem atribuição retira espaço entre os print


'''
Observações importantes da Aula:
O python diferencia letras maisculas de minusculas, logo:
    print() é o correto
    Print() com P maiusculo é incorreto, e não irá funcionar
  
'''


