#1. Escribe un programa en Python para encontrar los elementos duplicados de una lista,
#añadirlos a una nueva lista y borrarlos de la lista. Después imprime una lista con tan solo los
#elementos únicos.
#----lista_animales = ["leon", "pato", "raton", "rinoceronte", "leon", "jirafa", "tiburon", "elefante", "raton", "canguro"]
#----elementos_duplicados = []
#----elementos_unicos = []
#----print("La lista de elementos inicial es: ", lista_animales)
#----for elementos in lista_animales:
    #----if lista_animales.count(elementos) > 1:
        #----if elementos not in elementos_duplicados:
            #----elementos_duplicados.append(elementos)
#----print("La lista de elementos duplicados es: ",elementos_duplicados)

#----for elemento in lista_animales:
    #----if lista_animales.count(elemento) <= 1:
        #----elementos_unicos.append(elemento)
#----print("La lista de elementos únicos es: ",elementos_unicos)
#----print("------------")
#2. Escribe un programa en Python para unir dos listas y ordenarlas en orden ascendente.
#----import random
#----lista1 = [random.randint(1, 100) for i in range (5)]
#----lista2 = [random.randint(1, 100) for i in range (5)]

#----print("La primera lista aleatoria es: ",lista1)
#----print("La segunda lista aleatoria es: ",lista2)
#----print("-------------")
#----lista_combinada = lista1 + lista2

#----print("La lista única de ambas listas es: ", lista_combinada)
#----print("---------")

#----lista_ordenada = sorted(lista_combinada)

#----print("La lista única de ambas listas ordenada es: ", lista_ordenada)
#----print("---------")

#3. Escribe un script que encuentre el segundo número más grande de una lista.
#----print("El segundo número más alto en la lista es:", lista_ordenada[8])
#----print("---------")
#----lista_combinada.sort(reverse=True)
#----print("Segundo número mas alto usando reverse=True:", lista_combinada[1])
#----print("---------")
#4. Crea un script que cuente el número de elementos más grandes que un determinado número
#dado por el usuario (supón una lista numérica).
#----lista3 = [random.randint(1,100) for i in range(10)]

#----num_usuario = int(input("Introduce un número entre el 1 y el 100: "))
#----print(" ")
#----import time
#----time.sleep(2)
#----print("La lista generada es: ", lista3)
#----print(" ")

#----num_superiores = 0
#----for number in lista3:
    #----if num_usuario < number:
    #----   num_superiores = num_superiores + 1
#----print("Hay", num_superiores, "números por encima del número dado por el usuario.")
#----print("--------")

#5. Crea un script dado un número introducido por el usuario o determinado al inicio del
#programa, realice la suma de aquellos números que sean divisibles por este.
#----number_usu = int(input("Introduce un número entero: "))
#----print(" ")
#----import time
#----time.sleep(2)

#----lista4 = [random.randint(1,100) for i in range(10)] #---- tambien con una lista escrita por nosotros = [20,4,32,16]
#----print("Esta es la lista generada aleatoriamente: ",lista4)
#----print(" ")

#----suma_de_valores = 0
#----for number in lista4:
    #----if number_usu % number == 0:
        #----suma_de_valores = suma_de_valores + number
#----print("Esta es la suma de los números que son mayores al aportardo por el usuario: ", suma_de_valores)


#6. Escribe un script que pida un número al usuario y dada una lista encuentre el número más alto
#que es inferior al número introducido o determinado al inicio del programa.
#----n_usu = int(input("Introduce un número entre el 1 y el 15: "))

#----while n_usu > 15:
    #----print("Ha introducido un numero incorrecto. Intente de nuevo: ")
    #----n_usu = int(input("Introduce un número válido: "))
#----print(" ")

#----lista5 = [random.randint(1,20)for i in range(6)]
#----import time
#----time.sleep(2)
#----print("Esta es la lista: ", lista5)
#----print(" ")
#----lista5_orden = sorted(lista5)

#----resultado = 0
#----for num in lista5_orden:
    #----if num < n_usu:
    #----    resultado = num
#----print("El número mayor por debajo del número usuario es: ", resultado)
#----print("--------")

#7. Crea un script que extraiga los elementos comunes entre dos listas.
#----import time
#----lista6 = [1,2,3,4,5]#----lista6 =[random.randint(1,50)for i in range(10)]
#----print(" ")
#----time.sleep(1)
#----print("Estos son los valores de la lista: ",lista6)
#----lista7 = [4,5,6,7,8]#----lista7 = [random.randint(1,50)for i in range(10)]
#----print(" ")
#----time.sleep(1)
#----print("Estos son los valores de la lista: ",lista7)
#----lista_comunes = []
#----time.sleep(1)

#----for elemento in lista6:
    #----if elemento in lista7:
        #----lista_comunes.append(elemento)
            
#----print(" ")
#----print("Este es la lista de los valores que aparecen en ambas listas: ", lista_comunes)


#8. Crea un script que cuente el número de apariciones de un elemento de una lista en dicha lista
#(P.e. en la lista lista=[23, 65, 23] el número de apariciones de 23 es 2)
#----lista8 = [1,2,3,2,4,5,5,6,7,3,8,9]

#----target = 2
#----target1 = 3
#----n_repetidosT = lista8.count(target)
#----n_repetidosT1 = lista8.count(target1)
#----print("Los números ",target, "y", target1, "aparecen ", n_repetidosT,"y", n_repetidosT1, "respectivamente en esta lista.")
#----print("-------")

#----for num in lista8:
    
    #----print("El número", num, "aparece", lista8.count(num), "veces.")

#----print("------------")    

#9. Escribe un programa que lea una lista de enteros y cree una nueva lista que contenga solo
#números positivos de la lista original.
#----lista9 = [10,25,-2,14,-68,37,-6,77]
#----print("Estos son los valores de la lista origial: ", lista9)
#----print(" ")
#----lista_positivos = []
#----lista_negativos = []
#----for numeros in lista9:
    #----if numeros < 0:
        #----lista_negativos.append(numeros)
    #----else:
        #----lista_positivos.append(numeros)
    
#----print("Estos son los número positivos de la lista original: ", lista_positivos)
#----print(" ")
#----print("Estos son los número negativos de la lista original: ", lista_negativos)

#10. Crea un script que tome una lista de strings y cree una nueva lista que contenga el tamaño de
#los strings de la lista original.
#----lista10 = ["leon", "hormiga", "cerdo", "elefante", "koala"]
#----print(lista10)
#----print(" ")
#----lista_tamaños = []

#----for animales in lista10:
    #----lista_tamaños.append(len(animales))

#----print("La longitud de cada una de las palabras de la lista son: ", lista_tamaños)

#11. Crea un programa que dada una lista de strings, devuelva otra lista con los strings en
#mayúscula
lista10 = ["leon", "hormiga", "cerdo", "elefante", "koala"]
lista_mayus = []
print(lista10)
print(" ")

for animales in lista10:
    animales = animales.upper()
    lista_mayus.append(animales)

print(lista_mayus)

