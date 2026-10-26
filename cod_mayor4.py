#Crea un script que pida al usuario 4 números diferentes e imprima el mayor de los cuatro por pantalla.

# --- Pedir NUMEROS al usuario
n1 = int(input("Escribe el primer numero entero: "))
n2 = int(input("Escribe el segundo numero entero: "))
n3 = int(input("Escribe el tercer numero entero: "))
n4 = int(input("Escribe el cuarto numero entero: "))

# --- Imprimir el mayor de los cuatro numeros
if n1 > (n2 and n3 and n4):
    print("El numero mayor de los cuatro es primer número:", n1)
elif n2 > (n1 and n3 and n4):
     print("El numero mayor de los cuatro es segundo número:", n2)
elif n3 > (n1 and n2 and n4):
      print("El numero mayor de los cuatro es tercer número:", n3)
else:
      print("El numero mayor de los cuatro es cuarto nuúero:", n4)

