'''
Operadores Aritméticos
- operador de soma (+)
- operador de subtração (-)
- operador de multiplicação (*)
- Operador de divisão (/)
- operador de divisão inteira (//)
- operador de exponenciação (**)
- operador de resto de divisão (%)
- operação com parenteses ()
'''

#  Soma
print(10 + 10)

#  Subtração
print(11 - 10)

#  Multiplicação
print(10 * 10)

#  Divisão
print(10 / 10)

#  Divisão Inteira
print(10 // 10)

#  Exponenciação
print(10 ** 2)

#  Resto da divisão
print(5 % 2)


#  Operações com Strings

print(3 * 'Lucas')
#  printa: LucasLucasLucas, pois irá repetir 3 vezes a String (de acordo com o multiplicador)

print('20' + '30')
#  printa: 2030, pois o + irá concatenar entre 20 e 30.
#  Concatenar, de maneira informal, significa 'juntar'

print('5+2*10 Sem parenteses', 5+2*10)
#  printa: 5+2*10 Sem parenteses 25

print('(5+2)*10 Com parenteses', (5+2)*10)
#  printa (5+2)*10 Com parentese 70


'''
Observação

Soma entre Inteiro e String
    ex:
        print(5 + '5') - irá ocorre um erro, pois não soma nem concatena entre strings e inteiros
        
Logo, deve haver logica nas operações
'''
