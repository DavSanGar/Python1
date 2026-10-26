#Define una lista de 5 palabras aleatorias y una lista de letras prohibidas que contenga tres letras.
#Filtra las palabras en tu lista original crea una nueva lista de palabras filtradas que solo contenga
#aquellas palabras que no tienen ninguna letra prohibida.

palabras = ["jamon", "estrella", "camion", "lobo", "liebre"]
letras_prohibidas = ["c", "o", "f"]
palabras_filtradas = []
palabras_prohibidas = []

for palabra in palabras:
    incluir = True
    for letra in letras_prohibidas:
        if letra in palabra:
           incluir = False
    if incluir:
        palabras_filtradas.append(palabra)

    if incluir != True:
        palabras_prohibidas.append(palabra)


            
print("Esta es la lista de palabras que NO contienen las letras prohibidas: ", palabras_filtradas)
print(" ")
print("Esta es la lista de palabras que SI contienen las letras prohibidas: ", palabras_prohibidas)
