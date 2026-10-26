#Crea un programa que imprima todos los números primos entre el 2 y el 100. 
# Un numero primo es un numero positivo y entero mayor que uno 
# que no tiene un divisor positivo y entero que no sea 1 o sí mismo.

#--- crear bucle del 2 al 100
for num in range(2,101):
    prime = True
#---para dicho numero, verificar si hay alguno que sea divisor
    for i in range(2, num):
        if num % i == 0:
            prime = False
#--- también se puede colocar aquí un "break", de esta forma, evitamos que el if ejecute
# una búsqueda innecesaria de otros números superiores si ya antes ha encontrado otro
# que de como resto 0.          
    if prime == True:
        print (num)
