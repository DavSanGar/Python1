#Pide a un usuario 4 números y devuelve
#los números introducidos en orden ascendente, 
#Para ellos usar listas y bucle for

#---- inicializar una lista de numeros

lista_num = []

#--- crear un bucle para ir pidiendo los numero e ir añadiendolos a la lista
for i in range(0,4):
    numero = int(input("Introduce un número:" ))
     #--- lo añadimos a la lista de números
    lista_num.append(numero)


print(lista_num)
#--- imprimir el mayor numero de la lista
print("El número más alto de la lista sería el: ", max(lista_num))
#--- imprimir la lista ordenada
lista_num.sort()

print("Los números introducidos en orden ascendente son: ", lista_num)
