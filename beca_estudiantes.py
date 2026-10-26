
# Además para acceder a la beca el estudiante debe tener entre 17 y 21 años.
# Crea un script que pida el nombre, la edad y la nota media del estudiante e indique si puede optar a la beca o no.



##---Pedir datos del usuario
nota = float(input("¿Qué nota tienes? "))
edad = int(input("¿Qué edad tienes? "))

if nota > 8.0 and edad >= 17 and edad <= 21:
    print("Tienes derecho a beca. Introduce tus datos para acceder a la ayuda: ")
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")
    domicilio = input("Domicilio: ")
    cuenta_bancaria = input("Cuenta bancaria: ")

else:
    print("No tienes derecho a beca")
##Comprobar si cumple las condiciones
##Nota media > 8 y edad entre 17 y 21