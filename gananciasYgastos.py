# --- Pedir nombre al usuario ---
nombre = str
print("¿Cómo te llamas?")
nombre = input()


# --- Saludar al usuario ---
print ("Buenas tardes", nombre.title(),".Bienvenido" )

import time
time.sleep(2)

# --- Guardamos ingresos y horas trabajadas
#ingresos_hora = 25 # en euros
#horas_trabajadas = 25

ingresos_hora = int
horas_trabajadas = int
ganancias_semanales = int

ingresos_hora = 25
horas_trabajadas = 25

# --- Calculamos la ganancia semanal

ganancias_semanales = ingresos_hora * horas_trabajadas
print("Has trabajado 25 horas esta semana")
import time
time.sleep(1.5)
print("Has ganado 25€ por cada hora")
import time
time.sleep(1.5)
print("Tu sueldo semanal es:", ganancias_semanales, "€")

import time
time.sleep(2)

# --- Calculamos la ganancia anual
ganancia_anual = int

ganancia_anual = ganancias_semanales * 52

# --- Imprime ganancia anual por pantalla

print("Con lo que tu ganancia total anual es de :", ganancia_anual, "€")


# --- Pedimos los gastos mensual al usuario
gastos_vivienda = int
gastos_gasoil = int
gastos_ocio = int
gastos_comida = int
gastos_mensuales = int

print("¿Cuánto te gastas al mes en la vivienda?")
gastos_vivienda = int(input())
print("¿Cuánto te gastas al mes en la gasoil?")
gastos_gasoil = int(input())
print("¿Cuánto te gastas al mes en la ocio?")
gastos_ocio = int(input())
print("¿Cuánto te gastas al mes en la comida?")
gastos_comida = int(input())

import time
time.sleep(2)

gastos_mensuales = gastos_vivienda + gastos_gasoil + gastos_ocio + gastos_comida

print("Tu gasto total mensual es de:", gastos_mensuales, "€")

import time
time.sleep(2)

# --- Calculamos el gasto anual 
gasto_anual = int

gasto_anual = gastos_mensuales * 12

print("Tu gasto total anual es de:", gasto_anual, "€")

# --- Calculamos los ahorros
import time
time.sleep(2)
ahorros = int

ahorros = ganancia_anual - gasto_anual

print("Tus ahorros anuales son:", ahorros, "€")
