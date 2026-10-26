#Pide un numero por pantalla e indicar
#si es un multiplo de 3 siempre y cuando el
#resultado de numero entero



#---Pedir numero al usuario
print("Introduce un número entero")
numero = int(input())


# ---Comprobar si es multiplo de 3


if numero % 3 == 0 :
    print("El número",numero, "es multiplo de 3") 
else:
    print("El número",numero, "no es multiplo de 3")
