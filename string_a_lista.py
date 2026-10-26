'''Desarrolla un script en Python que dado una cadena de caracteres con la siguiente información:
nombre, apellido, DNI, código_asignatura, convocatoria, nota1, nota2, nota3 … 
Por ejemplo: David Fernandez 12311267A 43527 2 2.1 4.6 3.4. 
El script debe crear una lista con esos datos,
introducirlo en una lista de listas donde se encuentra la información de todos los alumnos e
imprimir la nota media de los alumnos junto con el DNI.'''

base_datos = [["Alvaro", "Gomez", "87654327B", "64782", "1", "7.6", "5.4", "9.3"]]

david_fernandez = "David Fernandez 12311267A 43527 2 2.1 4.6 3.4"

datos_alumno = david_fernandez.split()

base_datos.append(datos_alumno)

for alumno in base_datos:
    dni = alumno[2]
    #print("El DNI es: ",dni)
    suma_notas = 0
    for i in range(5, len(alumno)):
        notas = (alumno[i])
        suma_notas = suma_notas + float(alumno[i])
        media = suma_notas / 3
    #print("La nota media es: ",media)
    #print("---")
        

'''Supón ahora que tu input es un string como este:

David Fernandez 12311267A 43527 2 9.1 7.6 2.4\n
Maria Garcia 12316487A 43527 2 7.1 8.6 5.4\n
Juan Perez 647829236A 43527 2 8.1 8.5 8.4\n 

Reescribe el script para que procese ese input adecuadamente e imprima la nota media y el DNI
de todos los alumnos en ese string.'''

maria_garcia = "Maria Garcia 12316487A 43527 2 7.1 8.6 5.4"
juan_perez = "Juan Perez 647829236A 43527 2 8.1 8.5 8.4"

datos_alumno[5] = "9.1"
datos_alumno[6] = "7.6"
datos_alumno[7] = "2.4"

datos_alumno2 = maria_garcia.split()
datos_alumno3 = juan_perez.split()

base_datos.append(datos_alumno2)
base_datos.append(datos_alumno3)

for alumno in base_datos:
    dni = alumno[2]
    suma_notas = 0
    for i in range(5, len(alumno)):
        notas = alumno[i]
        suma_notas = suma_notas + float(alumno[i])
        media = suma_notas / 3
    print(f"El alumno con DNI , {dni}, tiene una nota media de {media:.2f}")
    print("----------")
