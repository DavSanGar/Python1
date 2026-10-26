#Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
#pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

contraseña = "gzmdsg"
contra_exacta = False


while contra_exacta == False:
    contraseña_correcta = input("Introduce la contraseña: ")
    if contraseña_correcta != contraseña:
        print("La contraseña es incorrecta. Intente de nuevo")
        continue

    if contraseña_correcta == contraseña:
        contra_exacta = True

    
print("La contraseña es correcta. Bienvenido")