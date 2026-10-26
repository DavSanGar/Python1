# --- Pedir al usuario que ingrese la cantidad en euros --
dinero = int

print("¿Me puedes indicar con qué dinero dispones?")
dinero = int(input())

print ("Dispones de este dinero:", dinero, "€")

# --- Convertimos la cantidad ingresada a un float ---

dinero_decimal = float(dinero)

print ("Dispones de este dinero:", dinero_decimal, "€")

# --- Convertir la cantidad de euros a dolares ---
euroAdolar = float
USD = 1.04
euroAdolar = dinero_decimal * USD

# --- Imprimir el resultado de la conversión ---

print("Tus euros equivalen a", euroAdolar,"dólares")

# --- Calculamos la cantidad que se queda la casa de cambios ---
ganancia_casaCambio = float

comision = float
comision = 0.05

ganancia_casaCambio = euroAdolar * comision

import time
time.sleep(2)

print("La comisión es:", ganancia_casaCambio, "dolares")


# --- Calculamos la cantidad de dolares que recibe el usuario ---
import time
time.sleep(2)

dolares_recibidos = float

dolares_recibidos = euroAdolar - ganancia_casaCambio

print("El dinero real que te corresponde es:", dolares_recibidos, "dólares")