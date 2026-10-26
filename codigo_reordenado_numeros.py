# --- Pedimos al usuario que introduzca un número
numero = int

print("Coloca un número de cinco dígitos")
numero = (input())

# --- Mostrar el número componente a componente por pantalla

print(f"{numero[0]}\n{numero[1]}\n{numero[2]}\n{numero[3]}\n{numero[4]}")

# --- Pedimos un numero al usuario ---
numero = int

print("Escribe un número de varios digitos")

numero = (input())

# --- Creamos el strig inverso ---
numero_inverso = numero[::-1]

import time
time.sleep(2)



# --- imprimos el resultado por pantalla


print(numero_inverso)