#Escriba un programa que pida el año actual y un año cualquiera y 
# que escriba cuántos años han pasado desde ese año o cuántos años 
# faltan para llegar a ese año.

año_actual = int(input("Escribe el año en el que estamos: "))
año_aleatorio = int(input("Escribe un año aleatorio: "))
diferencia_años = año_actual - año_aleatorio
diferencia_años = abs(diferencia_años)

if año_actual == año_aleatorio:
    print("Es el mismo año. No hay diferencia")
else:
    print("La diferencia de años entre ambos es de :", diferencia_años, "años")