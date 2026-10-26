


def filtrar_palabras(palabras, letras_prohibidas):
    palabras_prohibidas = []
    palabras_filtradas = []

    for palabra in palabras:
        if any(letra in palabra for letra in letras_prohibidas):
            palabras_prohibidas.append(palabra)
        else:
            palabras_filtradas.append(palabra)
    return palabras_filtradas, palabras_prohibidas


palabras = ["jamon", "estrella", "camion", "lobo", "liebre"]
letras_prohibidas = ["t", "b", "r"]
    

filtradas, prohibidas = filtrar_palabras(palabras, letras_prohibidas)

print("Filtradas",filtradas)
print("Prohibidas",prohibidas)