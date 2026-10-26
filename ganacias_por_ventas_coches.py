# --- Preguntar al usuario cuantos coches ha vendido de cada tipo y guardamos los datos en variables ---


print("¿Cuántos coches has vendido del modelo i10?")
i10 = float(input())
print("¿Cuántos coches has vendido del modelo i20?")
i20 = float(input())
print("¿Cuántos coches has vendido del modelo i30?")
i30 = float(input())

PVP_i10 = 12250.50
PVP_i20 = 16300.80
PVP_i30 = 19780.40

# --- Calculamos la cantidad de euros a comisionar ese mes ---
ganancia_i10 = float
ganancia_i20 = float
ganancia_i30 = float

comision_i10 = 0.05
comision_i20 = 0.065
comision_i30 = 0.08

ganancia_i10 = (PVP_i10 * comision_i10) * i10
ganancia_i20 = (PVP_i20 * comision_i20) * i20
ganancia_i30 = (PVP_i30 * comision_i30) *i30

print("Las ganancias sobre el modelo i10 es de:", ganancia_i10,"€")
import time
time.sleep(1.5)
print("Las ganancias sobre el modelo i20 es de:", ganancia_i20,"€")
import time
time.sleep(1.5)
print("Las ganancias sobre el modelo i30 es de:", ganancia_i30,"€")

# --- Imprimimos la ganancia total ---

ganancias_Absolutas = float

ganancias_Absolutas = ganancia_i10 + ganancia_i20 + ganancia_i30
import time
time.sleep(2)


print("Tus ganancias totales en este mes ascienden a:", ganancias_Absolutas, "€")