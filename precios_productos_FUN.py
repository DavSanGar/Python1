'''Analisis de precios de productos:

Escribir un script que analice una lista de precios
de productos y dertermine el precio más alto, el más bajo
y el precio promedio de todos los productos. Soluciona el ejercicio 
sin usar funciones max() y min()
'''

def precio_mas_alto():
    precios = [5.34, 6.29, 9.8, 1.72, 12.40]
    mayor = 0
    for precio in precios:
        if precio > mayor:
            mayor = precio
    return mayor
print(precio_mas_alto())

def precio_mas_bajo():
    precios = [5.34, 6.29, 9.8, 1.72, 12.40]
    menor = precios[0]
    for precio in precios:
        if precio < menor:
            menor = precio
    return menor
print(precio_mas_bajo())

def precio_promedio():
    precios = [5.34, 6.29, 9.8, 1.72, 12.40]
    promedio = sum(precios)/len(precios)
    return promedio
print(precio_promedio())

 
def mayorYmenor():
    n1 = precio_mas_alto()
    n2 = precio_mas_bajo()
    return n1+n2
resultado = mayorYmenor()
print(resultado)

def sumaTodos():
    n1 = precio_mas_alto()
    n2 = precio_mas_bajo()
    n3 = precio_promedio()
    return n1 + n2 + n3
resultado = sumaTodos()
print(resultado)