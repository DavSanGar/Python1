'''Supongamos que eres el propietario de una tienda en línea y tienes una lista de ventas de los
últimos 30 días. Quieres analizar las ventas por día de la semana para identificar los días de mayor
venta.
Pista 1: Puedes crear dos listas, una con las ventas por cada día del mes como por ejemplo…
ventas = [120, 80, 140, 200, 75, 100, 180, 220, 160, 110, 90, 120, 170, 190, 250, 300, 95, 110,
140, 180, 200, 160, 120, 80, 170, 150, 210, 190, 230, 250]
Y otra lista con los días de la semana:
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", „Domingo“]
Después puedes crear una nueva lista con una entrada por cada día de la semana y usar un bucle
para añadir a esta lista la suma de las ventas correspondientes a cada uno de los días de la
semana.
Pista 2: Puede que necesites una variable que lleve la cuenta del día de la semana actual y se
reinicie a cero cuando llegue al séptimo día.'''

ventas_diarias_men = [120, 80, 140, 200, 75, 100, 180, 220, 160, 110, 90, 120, 170, 190, 250, 300, 95, 110,
140, 180, 200, 160, 120, 80, 170, 150, 210, 190, 230, 250]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

dias_ventas = [["Lunes"],["Martes"],["Miércoles"],["Jueves"],["Viernes"],["Sánado"],["Domingo"]]
ventas_totales =[0, 0, 0, 0, 0, 0, 0]

#recorrer la lista de ventas
dia_venta = 0
for venta in ventas_diarias_men:
    #sumar para cada día de la semana la suma total
    ventas_totales[dia_venta] = ventas_totales[dia_venta] + venta
    dia_venta = dia_venta + 1  
    # llegando al domingo, volvemos de nuevo al lunes (indice 0)
    if dia_venta == 7:
        dia_venta = 0
print("El número de ventas a lo largo de la semana es: ",ventas_totales)
print(" ")
dias_ventas[0].append(ventas_totales[0])
dias_ventas[1].append(ventas_totales[1])
dias_ventas[2].append(ventas_totales[2])
dias_ventas[3].append(ventas_totales[3])
dias_ventas[4].append(ventas_totales[4])
dias_ventas[5].append(ventas_totales[5])
dias_ventas[6].append(ventas_totales[6])

print("Esta es la lista de días de la semana junto a sus ventas: ",dias_ventas)
