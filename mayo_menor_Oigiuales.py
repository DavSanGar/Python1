#Escriba un programa que pida dos números y que conteste 
# cuál es el menor y cuál el mayor o que escriba que son iguales.

numero1 = int(input("Escribe un número: "))
numero2 = int(input("Escribe otro número: "))

if numero1 > numero2:
    print("El primer número es el número mayor de los dos")
elif numero2 > numero1:
    print("El segundo número es el número mayor de los dos")
else:
    print("Ambos números son iguales")
