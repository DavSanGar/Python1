#Pide a un usuario 4 números y devuelve
#los números introducidos en orden ascendente, 
#Para ellos usar listas y bucle while
lista_num = [] 
terminado = False

  #--- crear un bucle para ir pidiendo los numero e ir añadiendolos a la lista
while terminado == False:
    numero = input("Introduce un número: ")
    if numero.isnumeric() == False:
        print("No ha introducido un número, intentelo de nuevo")
        continue
    #---Pasar a enteros el valor introducido
    numero = int(numero)
    #--- Añadir valores a la lista
    lista_num.append(numero)

    if len(lista_num) == 4:
        terminado = True
    #---Imprimir la lista de 4 numeros
print("La lista de números es: ", lista_num)

lista_num.sort()

#--- imprimir la lista ordenada
print("La lista ordenada de manera ascendente es: ", lista_num)
#--- imprimir el mayor numero de la lista
print("El número más alto de la lista es: ", lista_num[-1])
