#Trabajas en colegio y estas encargado de mantener un seguimiento de las notas de los
#estudiantes de un clase. En tu base de datos tienes una lista con los nombres de los estudiantes y
#para cada estudiante debes guardar sus notas provenientes de deberes, exámenes y proyectos.
#También necesitas calcular la nota media de cada estudiante y la nota media de la clase al completo.
#Pista: Para resolver este problema puedes usar una lista anidada donde guardes las notas para
#cada estudiante. Entonces puedes usar un bucle para recorrer la lista de listas y calcular la nota
#media de cada estudiante. También puedes usar otro bucle para calcular la nota media de toda la clase.

#---Listas alumnos, notas deberes, notas examenes, notas proyectos 
alumnos = ["Javier", "Maria", "Nuria", "David", "Pedro", "Alberto", "Sara", "Julia", "Silvia", "Sergio"]
print("Esta es la lista de alumnos: ", alumnos)
print(" ")
notas_deberes =[4, 6, 7.5, 5.5, 8, 6.2, 3.5, 9, 3.7, 8.5]
print("Esta es la lista de notas de deberes: ", notas_deberes)
print(" ")
notas_examenes = [7, 4.2, 6.8, 6.5, 5, 9, 3, 7.3, 5.9, 9]
print("Esta es la lista de notas de examenes: ", notas_examenes)
print(" ")
notas_proyectos = [5, 5, 6.6, 4.5, 7.5, 9, 8.2, 4.7, 8, 6.5]
print("Esta es la lista de notas de proyectos: ", notas_proyectos)
print(" ")

media_alumnos = []
alumnoYnotas = []
med_alum_str = []
##También podemos crear una database:
#database = ["Javier", [4,7,5]],
#  "[Maria", [6,4.2,5]],
#  "[Nuria", [7.5,6.8,6.6]]
# ...]

#---Calcular la media de los alumnos entre las tres secciones
media_deberes = 0
media_examenes = 0
media_proyectos = 0
media = 0
for i in range(0, len(notas_deberes)):
    media = (notas_deberes[i] + notas_examenes[i] + notas_proyectos[i]) / 3
    media_alumnos.append(media)
    media_alumnos = [round(num, 2)for num in media_alumnos]
print ("La nota media de los alumnos entre sus tres trabajos es: ",  media_alumnos)
print(" ")

#---Calculo nota media toda la clase: Dos formas.
#---1ª forma: media_clase = sum(media_alumnos) / 10
              ##print("La nota media de la clase es: ",media_clase)

#---2ª forma:
for i in media_alumnos:
 media_clase = (sum(media_alumnos)) / (len(media_alumnos))
    
print("La nota media de la clase es:{:.2f} ".format(media_clase))
print(" ")
#---Creamos una lista con nombres y nota media final
#med_alum_str = str(media_alumnos)

for alumno in alumnos:
   alumnoYnotas.append(alumno)

alumnoYnotas.insert(1,media_alumnos[0])
alumnoYnotas.insert(3,media_alumnos[1])
alumnoYnotas.insert(5,media_alumnos[2])
alumnoYnotas.insert(7,media_alumnos[3])
alumnoYnotas.insert(9,media_alumnos[4])
alumnoYnotas.insert(11,media_alumnos[5])
alumnoYnotas.insert(13,media_alumnos[6])
alumnoYnotas.insert(15,media_alumnos[7])
alumnoYnotas.insert(17,media_alumnos[8])
alumnoYnotas.insert(19,media_alumnos[9])
print("Esta es la lista de alumnos seguida de su nota media final :", alumnoYnotas)