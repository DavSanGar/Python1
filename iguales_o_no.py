#Escriba un programa que pida tres números y 
# que escriba si son los tres iguales, si hay dos iguales o si son los tres distintos

numero1 = int(input("Escribe el primer número: "))
numero2 = int(input("Escribe el segundo número: "))
numero3 = int(input("Escribe el tercer número: "))
todos = int
if numero1 == numero2 == numero3: 
    print("Todos los números son iguales")
if numero1 == numero2:
    print("El primer y el segundo número son iguales.")
elif numero2 == numero3:
    print("El segundo y el tercer número son iguales.")
elif numero3 == numero1:
    print("El primer y el tercer número son iguales.")
else:
    print("Ninguno de los número son iguales")