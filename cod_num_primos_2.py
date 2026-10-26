#Dado una lista de números enteros, escribe un script en Python que devuelva una nueva lista con
#los números primos de la lista original. Además, el script debe devolver el número total de
#números primos encontrados y la suma de los números primos encontrados
import random
numeros = [random.randint(1,100)for i in range(10)]
lista_primos = []
total_primos = 0
primos_encontrados = 0

print("Esta es la lista de números inicial: ", numeros)
print(" ")
#---bucle para recorrer los numeros
for numero in numeros:
    primo = True
    #---aquí compruebo si hay primos
    for i in range(2,numero):
        if numero % i == 0:
            primo = False
    #---al ser verdadero, añadimos numero a la lista
    if primo == True:
        lista_primos.append(numero)

#---Imprimimos la lista de primos
print("Esta es la lista de números primos sobre la primera lista: ", lista_primos)
print(" ")
#---Imprimimos la lista de primos
primos_encontrados = len(lista_primos)
print("Este es el total de números primos encontrados", primos_encontrados)
print(" ")
total_primos = sum(lista_primos)
print("Esta es la suma de los números primos encontrados", total_primos)
