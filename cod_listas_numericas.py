#Crea una lista llamada “numeros“ que contenga los siguientes numeros enteros:[1,2,3,4,5,6,7,8,9,10]

numeros = list(range(1,11))
print(numeros)
#Crea una nueva lista con los números pares de la lista anterior en orden inverso
#list_numeros2 = [10,8,6,4,2]
pares = []
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
print(pares)

pares_invertidos = pares[::-1]
print(pares_invertidos)


#Escribe un bucle que recorra la lista “numeros“ e imprima el cuadrado de cada numero por
#consola.
for numero in numeros:
    print(numero*numero) # También print(numero**2)
#Intenta rehacer los pasos 2 y 3 con el menor número de lineas posible (método de
#compresión).
print("----------------")

numeros_pares_invertidos = [numero for numero in numeros if numero % 2 == 0][::-1]
numeros_cuadrados = [numero**2 for numero in numeros]

print(numeros_pares_invertidos)
print(numeros_cuadrados)

print("------------")
#Usa un método que te devuelva el número más pequeño de la lista e imprímelo por pantalla
num_menor = min(numeros_cuadrados) 
print("El numero mas pequeño es: ",num_menor)
print("-------")
#Haz lo mismo con el número más alto
num_mayor = max(numeros_cuadrados)
print("El numero mas mayor es: ",num_mayor)
print("-------")
#Suma todos los elementos de la lista sin un bucle.
suma_elementos = sum(numeros_cuadrados)
print(suma_elementos)
print("--------")

#Suma todos los elementos de la lista con un bucle.
i = 0
for numero in numeros_cuadrados:
    i = numero + i
    print (i)

print("-------")
#Encuentra el índice correspondiente al número 8 en la lista original y en la lista resultante tras
#el punto 2

lista_original_8 = numeros.index(8)

print("El numero en el octavo lugar es: ", lista_original_8)

print("-------")
lista_cuadrados_8 = pares_invertidos.index(8)
print("El numero en el octavo lugar es: ",lista_cuadrados_8)
