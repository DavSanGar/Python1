#Un bot de trading está programado para realizar ciertas acciones con respecto a un producto financiero.
#Crea un script de manera que dado un precio introducido por el usuario, si el precio del
#producto está por debajo de 100 dólares, el bot imprima por pantalla la orden de comprar. Si está
#entre 100 y 150 dolores (ambos incluidos) el bot deberá imprimir la orden de hold. Si el precio está
#estrictamente por encima de 150 el bot deberá imprimir la orden de vender.



# ---- Pedimos un precio al usuario
activo = float(input("Dime el valor del activo: "))

# --- Comprobar el precio y ver si debemos comprar, holderar o vender

if activo <100 :
    print("El valor del activo es bajo. Debes comprar.")
elif activo in range (100,151):
    print("Debes mantener el activo.")
else:
    print("Debes vender el activo.")