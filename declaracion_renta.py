#Para tributar en un determinado país es necesario ser mayor de edad y cobrar más de 1000 euros
#al mes. Además los tramos impositivos de la renta anual son los siguientes:
#RENTA TIPO IMPOSITIVO
#Menos de 15.000 eu 5%
#Entre 15.000 y 25.000 eu 15%
#Entre 25.000 y 35.000 eu 20%
#Entre 35.000 y 60.000 eu 30%
#Más de 60.000 eu 45%
#Escribe un script que primero compruebe si eres susceptible de que se te aplique algún tipo
#impositivo y en caso afirmativo imprima por pantalla cuál te tocaría

retenciones = float

# --- Pedir datos al usuario
# edad
edad = int(input("¿Qué edad tienes? :"))

# ingreso
sueldo = float(input("¿Cuánto dinero ganas? :"))


# --- Comprobar si se debe aplicar el tipo impositivo y comprobar cual
# Comprobar si el usuario es mayor de edad y sus ingresos --> si debe tributar: Sí
if sueldo >12000 and sueldo <15000 and edad >= 18 :
    retenciones = sueldo * 0.05
    print("Tus retenciones según tu sueldo corresponden a: ", retenciones, "€")
elif sueldo >=15000 and sueldo <= 25000 and edad >= 18 :
    retenciones = sueldo * 0.15
    print("Tus retenciones según tu sueldo corresponden a: ", retenciones, "€")
elif sueldo >= 25000 and sueldo <= 35000 and edad >= 18 :
    retenciones = sueldo * 0.2
    print("Tus retenciones según tu sueldo corresponden a: ", retenciones, "€")
elif sueldo >= 35000 and sueldo <= 60000 and edad >= 18 :
    retenciones = sueldo * 0.3
    print("Tus retenciones según tu sueldo corresponden a: ", retenciones, "€")
elif sueldo > 60000 and edad >= 18 :
    retenciones = sueldo * 0.45
    print("Tus retenciones según tu sueldo corresponden a: ", retenciones, "€")
else:
    print("No estás obligado a tributar")


    ## calcular su renta anual  
  
    ## comprobar en que tramo se encuentra su ingreso anual
# Si el usuario no esta en el rango de edad o ingresos

    ## imprimir que no tiene obligacion de tributar 
 