'''
Crea un programa en el que se pregunte al 
usuario por una frase y una letra, y muestre 
por pantalla el número de veces que aparece 
la letra en la frase.
'''

# --- pedir frase y letra
frase = input("Escribe una frase: ")
letra = input("Elige una letra del abecedario: ")
contador = 0
# --- bucle para recorrer la frase 
# --- y contar las apariciones de la letra
for caracter in frase:
    if caracter == letra:
        # también vale esta manera de sumar: contador = contador +1
        contador += 1
print(contador)     
