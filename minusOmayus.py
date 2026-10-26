
#EJERCICIOS 2B
#MAYUSCULA O MINUSCULA (BONUS*):
#Permite que el usuario introduzca una letra (del alfabeto latino) como input. Comprueba si esta es una mayúscula o una minúscula.


# --- Pedir al usuario una letra
letra = input("Introduce una letra: ")

if letra != letra.lower():
    print("La letra es mayúscula")
else:
    print("La letra es minúscula")