# --- Pedimos los tiempos por pantalla ---
#min: 10 seg:25 centesimas:348

#minutos_hannah = input("Ingresa los minutos para hannah")
print("¿Cuántos minutos ha hecho Hannah?")
minutos = int
minutos = int(input())
#segundos_hannah = input("Ingresa los segundos para hannah")
print("¿Cuántos segundos ha hecho Hannah?")
segundos = int
segundos = int(input())

#centesimas_hannah = input("Ingresa las centesimas para hannah")
print("¿Cuántos centésimas ha hecho Hannah?")
centesimas = int
centesimas = int(input())

# --- Extraer minutos segundos y centésimas ---

print("El tiempo de Hannah es de:",minutos,":",segundos,":",centesimas)

# --- Convertimos los tiempos a segundos ---
segundos_totales = float
minutos_a_segundos = float
centesimas_a_segundos= float
segundosYcentesimas = float

minutos_a_segundos = minutos * 60
centesiamas_a_segundos = centesimas * 0.001


segundos_totales = segundos + minutos_a_segundos + centesiamas_a_segundos

print(segundos_totales)

# --- Calculamos la velocidad media ---

velocidad_media = float

velocidad_media = 100 / segundos_totales

# --- Imprimir los resultados por pantalla ---

print("La velocidad media de Hannah ha sido de:", velocidad_media, "m/s")

