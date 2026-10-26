# --- Tenemos la contraseña correcta
key_correcto = "123456"

# --- Pedimos al usuario la contraseña
password = input("Introduce la contraseña: ")


# --- Comprobamos que el password introducido coincide con nuestra key
password = password.lower()

# Si coincide damos la bienvenida
if password == key_correcto:
    print("Bienvenido")
else: 
    # Si no coincide damos un error y pedimos la contraseña de nuevo
    print("La contraseña es incorrecta")
    password = input("Intente de nuevo: ")
    ## si esta vez la contraseña coincide damos la bienvenida
     
        ## si no damos un mensaje de error y se termina el programa
    
    if password == key_correcto:
     print("Bienvenido")
    else:
      print("La contraseña es incorrecta. Equipo bloqueado")



    
        