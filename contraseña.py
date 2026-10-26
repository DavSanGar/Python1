# --- Pedir contraseña al usuario
contraseña = str

print("Escribre una contraseña")
contraseña = input()


# --- Comprobar si la contraseña es segura
# Si cumple los requisistos diremos que es segura
# Debe tener una vocal (a,e,o)
# Debe tener un simbolo especial (*,#)

if ("a" in contraseña or "e" in contraseña or "o" in contraseña) and ("*" in contraseña or "#" in contraseña):
    print ("La contraseña es segura")
else:
    print("La contraseña no es segura.")


 
# Si no los cumple diremos que es insegura