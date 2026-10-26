def saludo():
    print("Hola amigo")
    return
saludo()

def saludo1(string):
    print("Hola", string.upper())
saludo1("pedro")

import math
def num(numero):
    resultado = (math.factorial(numero))
    print(resultado)

num(7)


def total_factura(valor):
    
    factura = valor * 1.21
    print(factura)
total_factura(25)

import math
def area_circulo(radio):
    area = (math.pi * radio**2)
    print(area)
area_circulo(4.2)

import math
def vol_cilindro(altura, radio):
    volumen = (math.pi * (radio**2) * altura)
    print(volumen)
vol_cilindro(5,1.5)

lista1 = [2,5,8,54,22,61,89,145]
def media_lista():
    media = sum(lista1)/len(lista1)
    return media
print(media_lista())


lista2 = [2,4,5,21,16,64]
lista_cuadrados = []
def cuadrados():
    for num in lista2:
        cuadrado = num**2
        lista_cuadrados.append(cuadrado)
    print(lista_cuadrados)
cuadrados()

import math
lista3 = [4,7,83,20,31,10]
lista_varianza =  []
def nuevos_valores():
    media = sum(lista3)/len(lista3)
    for num in lista3:
        varianza = (num-media)**2
        lista_varianza.append(varianza)
        varianza_2digitos = [round(num, 2)for num in lista_varianza]
        varianza_final = sum(varianza_2digitos)/media

    desviacion = varianza_final**0.5
    print("La lista oficial es :", lista3)
    print("La nueva lista es :", varianza_2digitos)
    print(f"La varianza de los numeros de la lista {lista3} es {varianza_final}")
    print("La desviacion tipica de esta varianza es ", desviacion)
nuevos_valores()
