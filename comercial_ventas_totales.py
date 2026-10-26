#Eres un comercial trabajando para una compañía que vende diversos productos. Quieres crear un
#programa para realizar un seguimiento de los productos que has vendido y el valor total de las
#ventas. Supongamos que hay un total de 10 productos.
#Tú has vendido 5 de estos productos en las siguientes cantidades:
#Producto 1: 3 unidades
#Producto 2: 1 unidad
#Producto 5: 7 unidades
#Producto 6: 2 unidades
#Producto 9 : 4 unidades
#Los precios de cada uno de estos productos son como siguen:
#Producto 1: 30.0 EU 
#Producto 2: 9.8 EU 
#Producto 3: 42.5 EU 
#Producto 4: 32.6 EU 
#Producto 5: 71.5 EU 
#Producto 6: 44.0 EU
#Producto 7: 21.2 EU
#Producto 8: 53.2 EU
#Producto 9: 25.3 EU
#Producto 10: 57.8 EU
#Crea un script que dada una lista con los productos, sus precios y las unidades vendidas, imprima
#la cantidad total de ventas, el dinero facturado por producto y el dinero total.

precio_productos = [30.0, 9.8, 42.5, 32.6, 71.5, 44.0, 21.2, 53.2, 25.3, 57.8]
n_productos_vend = [3, 1, 0, 0, 7, 2, 0, 0, 4, 0]
ventas_totales = []
total_ventas = sum(n_productos_vend)
print("La cantidad total de ventas son: ", total_ventas)

ventas = 0
for i in range(0, len(precio_productos)):
    ventas = precio_productos[i] * n_productos_vend[i]
    ventas_totales.append(ventas)

print(ventas_totales)

facturacion_total = sum(ventas_totales)
print("La facturación total es de: ", facturacion_total)