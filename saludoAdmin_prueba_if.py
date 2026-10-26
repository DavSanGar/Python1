# Crear un scrip que dado un usuario le de una bienvenida personalizada 
# al administrador, y una genérica si es otra persona 


nombre = input("¿Cómo te llamas?")


nombreAdministrador = "david"

if nombre.lower() == nombreAdministrador :
    print("Bienvenido, ", nombreAdministrador, "eres el administrador.")
else :
    print("Bienvenido. Tienes acceso de invitado")    

