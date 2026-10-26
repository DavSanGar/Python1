# --- Pedir nombre por pantalla
nombre = str

print("¿Cómo te llamas?")
nombre = input()
# --- Solucionar nombre mal escrito por el usuario
nombre = nombre.replace(".","")
# --- Solucionar nombre mal escrito por el usuario
nombre = nombre.title()


print(nombre)

# --- Variables con nombres de  los usuarios
usuario_1 = "David"
usuario_2 = "Nuria"
usuario_3 = "Ceci"

# --- Comprobar si el nombre coincide con el de usuarios
# Si coincide entonces damos bienvenida al usuario
if nombre == usuario_1:
    print("Bienvenido David. Eres el usuario administrador")
elif nombre == usuario_2:
    print("Bienvenida Nuria. Eres uruario invitado")
elif nombre == usuario_3:
    print("Bienvenida Ceci. Eres uruario invitado")
else:
    print("Bienvenido. Crea un usuario")

# Si no damos bienvenida generica

