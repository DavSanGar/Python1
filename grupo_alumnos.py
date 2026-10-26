#En uno de los cursos se ha dividido a una clase en dos grupos A y B. Para mezclar a los alumnos
#lo mejor posible se ha asignado a todas las chicas con nombres empezando por la letra E hasta la
#M en el grupo A y el resto en el B. A los chicos con nombres empezando por la letra A hasta la H y
#R hasta la Z se les ha asignado al grupo A también, el resto están en el B.
#Crea un script que pregunte al usuario si es chica o chico y el nombre. El script debe mostrar por
#pantalla el grupo que le corresponde a ese alumno.

# --- Pedir por pantalla los datos
#chico/chica
genero = input("¿Eres chico o chica?: ")
genero = genero.lower()
#nombre
nombre = input("¿Cuál es tu nombre?: ")
nombre = nombre.lower()
#inicial nombre
inicial = "abcdefghijklmnñopqrstuvwxyz"
# --- Elegir grupo que corresponde
# chica
## E hasta M --> grupo A
## el resto --> grupo B

if genero == "chica":
    if nombre[0] in inicial[4:13]:
        print("Estas en la clase A")
    else:
        print("Estas en la clase B")

# chico
## A hasta H, R hasta Z --> grupo A
## el resto --> grupo B

if genero == "chico":
    if (nombre[0] in inicial[0:8]) or (nombre[0] in inicial[18:27]):
        print("Estas en la clase A")
    else:
        print("Estas en la clase B")
