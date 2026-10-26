'''Analisis de precios de productos:

Escribir un script que analice una lista de precios
de productos y dertermine el precio más alto, el más bajo
y el precio promedio de todos los productos. Soluciona el ejercicio 
sin usar funciones max() y min()
'''

#--- Lista de precios
lista_precios = [5.34, 6.29, 9.8, 1.72, 12.40]
precio_total = 0
precio_max = 0.0
precio_min = float("inf")



#--- Bucle para recorrer la lista
for precio in lista_precios:
    #if statement
    #comprobamos si el precio es mas alto que el anterior
    if precio > precio_max:
        precio_max = precio
    
    #comprobamos si el precio es mas bajo que el anterior
    if precio < precio_min:
        precio_min = precio
#sumamos los valores de la lista
    precio_total += precio

print("El precio máximo de la lista es: ", precio_max)
print("El precio minimo de la lista es: ",precio_min)
print("El precio total de la lista es: ",precio_total)

#---calcular el precio promedio
precio_promedio = precio_total / len(lista_precios)
#---imprimimos
print("El precio medio de la lista es: ",precio_promedio)

if precio_max == precio_min:
    print("Los precios máximos y mínimos son iguales")
