#Crea un script que pida al usuario 3 números diferentes y le indique si alguno de ellos es la suma
#de los otros dos.

# --- Pedir tres numeros
n1 = int(input("Escribe el primer número: "))
n2 = int(input("Escribe el segundo número: "))
n3 = int(input("Escribe el tercer número: "))



# --- Comprobar si alguno de ellos es la suma de los otros dos
# Si es cierto imprimimos True
if n1 == (n2 + n3):
    print("La suma del segundo y tercer número es CIERTA. Coincide con el primer número ", n1)
elif n2 == (n1 + n3):
    print("La suma del primer y tercer número es CIERTA. Coincide con el segundo número ", n2)
elif n3 == (n1 + n2):
    print("La suma del primer y segundo número es CIERTA. Coincide con el tercer número ", n3)
else:
    print("La suma de cualquiera de dos de los tres números es FALSA")




# Si es falso imprimir False

