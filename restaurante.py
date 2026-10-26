# --- Definir el precio de cada alimento ---
pan = 0.8
sopa = 4.2
macarrones = 4.7
arroz = 3.8
pescado = 10.2
carne= 13.7
albondigas = 6.7
postre1 = 6.1
postre2 = 5.6
postre3 = 7.4
agua = 0.8
vino = 2.0
cerveza = 1.5

# --- Pedir al usuario que introduzca la cantidad de cada alimento que ha consumido ---
cantidad_pan = float
cantidad_sopa = float
cantidad_macarrones = float
cantidad_arroz = float
cantidad_pescado = float
cantidad_carne= float
cantidad_albondigas = float
cantidad_postre1 = float
cantidad_postre2 = float
cantidad_postre3 = float
cantidad_agua = float
cantidad_vino = float
cantidad_cerveza = float
print("Usted a comido pan, arroz, carne, postre2 y cerveza. ¿Cuánto de cada?")

cantidad_pan = float(input())
cantidad_arroz = float(input())
cantidad_carne = float(input())
cantidad_postre2 = float(input())
cantidad_cerveza = float(input())

# --- Calculamos el total de la cuenta ---
total_pan = float
total_arroz = float
total_carne = float
total_postre2 = float
total_cerveza = float
suma_cuenta = float

total_pan = cantidad_pan * pan
total_arroz = cantidad_arroz * arroz
total_carne = cantidad_carne * carne
total_postre2 = cantidad_postre2 * postre2
total_cerveza = cantidad_cerveza * cerveza

suma_cuenta = total_pan + total_arroz + total_carne + total_postre2 + total_cerveza

# --- Imprimimos la cuenta ---

print("Su cuenta tiene un total de:", suma_cuenta, "€")