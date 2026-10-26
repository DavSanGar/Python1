# --- Pedir dos numeros al usuario
numero1 = float
numero2 = float

print("Escribe un numero")
numero1 = float(input())
print("Escribe otro numero")
numero2 = float(input())

# --- Comprobar si el divisor es cero


# Si no es cero realizamos la division
# Si es cero imprimimos un error
division = float

if numero2 == 0.0 :
    print("El divisor no puede ser 0")
else:
    division = numero1 / numero2
    print("El resultado de dividir", numero1, "entre", numero2, "es", division)

