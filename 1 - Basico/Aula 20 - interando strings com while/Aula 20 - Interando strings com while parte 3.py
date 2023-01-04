

frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
contador = 0
nova_string = ''

# Irá transformar a letra que o usuario escolher em maiuscula em toda frase
input_usuario = input('Qual letra deseja colocar maiúscula: ')

# Criando while para demonstrar os indices da frase utilizando o tamanho da string
while contador < tamanho_frase:
    letra = frase[contador]
    if letra == input_usuario:
        nova_string += input_usuario.upper()
    else:
        nova_string += letra
    contador += 1


print(nova_string)