'''
Supongamos que eres un administrador de sistemas y necesitas validar el acceso de los usuarios
a un sitio web. Crea un script que verifique si el nombre de usuario y la contraseña ingresados son
correctos y permita el acceso solo si ambos son correctos.
Pista 1: Puedes crear dos listas, una con los nombre de usuario como por ejemplo…
nombres_usuario = ["juan123", "ana456", „pedro789"]
Y otra lista con las contraseñas guardadas para cada usuario…
contraseñas = ["clave123", "clave456", „clave789"]
Otra opción puede ser que crees una lista de listas con la forma:
nombres_contraseñas = [ ["juan123“,"clave123"] , ["ana456“,“clave456“] , ["pedro789“,
"clave789“] ]
Despues puedes pedir el usuario y contraseña y comprobar si coinciden.
Pista 2: Para verificar si el usuario y contraseña son correctos puedes crear un bucle donde
recorras los nombres de usuario y compruebes con un if si el nombre de usuario introducido y la
contraseña coinciden con los datos de tus listas.
'''

usuarios = ["Manolo", "Nuria", "Ruben", "Maria S.", "Alberto", "Maria F."]
contraseñas = ["manolo01", "nuricienta22", "Rub33", "maria.sanchez", "mevuelvoloco", "mariaf99"]
intentos = 3


while intentos > 0 :
    usuario = input("Escribre tu nombre de usuario: ")
    contraseña = input("Escribe tu contraseña: ")
    credenciales = False
    for i in range(len(usuarios)):

        if usuarios[i] == usuario and contraseñas[i] == contraseña:
            credenciales = True
            break
    if credenciales:
        print("Credenciales correctas. Bienvenido!")
        break
    else:
        intentos = intentos -1
        if intentos > 0:
            print("Credenciales incorrectos. Te quedan", intentos, "intentos más.")
        else:
            print("Límite de intentos. Acceso denegado")
           


        
    




