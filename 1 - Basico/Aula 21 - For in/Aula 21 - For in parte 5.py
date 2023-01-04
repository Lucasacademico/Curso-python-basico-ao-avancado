
# Código: Transforma não transforma o t em maiuscula devido o continue
# ... Termina o laço e finaliza o código sem printar o resto das letras
texto = 'python'
nova_string = ''

# continue pula para a proxima iteração
# break termina o laço

for letra in texto:
    if letra == 't':
        continue # continue pula para a proxima iteração
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
        break # break termina o laço
    else:
        nova_string += letra

print(nova_string)