'''
Crea un script que pida al usuario una palabra 
y luego muestre por pantalla una a una las letras 
de la palabra introducida empezando por la última.
'''
# --- pedir palabra al usuario

palabra = input("Escribe una palabra:" )
palabra = palabra.strip()
longitud = len(palabra)

# Tambien sirve esta forma sin tener que hacer bucle: 
print((palabra[::-1]))  # esto imprime en la misma linea
# o for i in palabra[::-1]:
# o para que la imprima en la misma línea y no cada entra en una linea distinta: 

# --- bucle que recorra el string de atras en adelante (esto imprime cada letra en una linea distinta)
#for i in range(longitud-1, -1, -1):
 #   print(palabra[i])
