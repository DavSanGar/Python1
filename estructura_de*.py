'''Escribe un programa que pida al usuario un número entero 
y muestre por pantalla una estructura como la de más abajo, 
donde el valor de entrada es el número de estrellas en el 
centro de la estructura.
*
** 
*** 
**** 
***** 
**** 
*** 
**
*
'''

# --- pedir al usuario un numero entero
numero = int(input("Escribe un número. Este será el tamaño máximo de la pirámide: "))
completo = False
# --- bucle ascendente
#for i in range(0,numero):
 #   i = str("*") * i
  #  print(i)
  
# --- bucle descendente    
#for i in range(numero,0,-1):
 #   i = str("*") * i
  #  print(i)

while completo == False:
    for i in range(0, numero):
        i = str("*") * i
        print(i)
    for j in range(numero, 0, -1):
        j = str("*") * j 
        print(j)
    completo = True