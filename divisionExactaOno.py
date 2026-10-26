#Escriba un programa que pida dos números enteros y que calcule su división, 
# escribiendo si la división es exacta o no.

dividendo = int(input("Escribe un numero: "))
divisor = int(input("Escribe otro numero: "))
resto = float
cociente = float

if divisor == 0 :
    print("No es posible dividir entre 0")
else:
    cociente = dividendo / divisor
    resto = dividendo % divisor
    
    
    if resto == 0:
        print("Esta operación da un cociente con valor entero. Cociente: " + str(cociente) + " Resto: " +str(resto))
    else:
        print("Esta operación da un cociente con valor decimal. Cociente: " + str(cociente) + " Resto: " + str(resto))

    