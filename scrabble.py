#Supongamos una lista de de caracteres llamada “palabras“ que representa una mano de Scrabble
#Cada string contiene dos caracteres: el primer carácter es la letra de una ficha y el
#segundo el numero que representa los puntos de la ficha. Por ejemplo, el string "A5" representa la
#ficha con la letra A y un valor de 5 puntos. Crea un script que calcule el valor total de los puntos
#en una mano de scrabble. El valor total será la suma de los puntos de todas las fichas de la mano.

mano_scrabble = ["A5", "Z8", "U7", "B4", "R2", "P6", "M9"]
print("Esta es la lista de fichas de nuestra mano:", mano_scrabble)
print(" ")

valores_mano = []
suma_valores_mano = 0

for mano in mano_scrabble:
    mano = int(mano[1])
    valores_mano.append(mano)

print("Esta es la lista de los valores de cada ficha:", valores_mano)
print(" ")

suma_valores_mano = sum(valores_mano)
print("Esta es la suma de los valores de todas las fichas:", suma_valores_mano)

