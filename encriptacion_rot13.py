'''
El abecedario latino es un sistema de escritura alfabético más usado del mundo hoy en día. Se
compone de 26 letras principales, más ciertas modificaciones y letras adicionales según el idioma
del que se trate (por ejemplo, en castellano y gallego se incluye la ”ñ”, en portugués, francés y
catalán la ”Ç”, en alemán la ”ß”, etc.).
Aplicar el cifrado ROT13 a un texto se reduce a examinar sus caracteres alfabéticos y sustituirlos
por la letra que está 13 posiciones por delante en el alfabeto, volviendo al principio si es necesario
y conservando las mayúsculas y minúsculas: a se convierte en n, B se convierte en O, y así hasta
la Z, que se convierte en M. Solo quedan afectadas las 26 letras principales que aparecen en el
alfabeto latino; los números, símbolos, espacios y otros caracteres se dejan igual.

[a,b,c,d,e,f,g,h,i,j,k,l,m] [H, O, L, A]

[n,o,p,q,r,s,t,u,v,w,x,y,z] [U, B, Y, N]

1. Desarrolla un script que recibiendo de entrada una cadena de caracteres devuelva el texto
codificado según el cifrado ROT13
2. Desarrolla ahora un script que compare dos cadenas de caracteres y nos diga si una de ellas
esta codificación ROT13 de la otra.
'''

abc = "abcdefghijklmnopqrstuvwxyz"
abc_mayus = abc.upper()
mensaje = "JamóN"
mensaje_comparacion= "WngóA"
mensaje_cifrado = ""
#---Recorremos cada letra del mensaje
for char in mensaje:
    #Compruebo si encuentra en minúscula
    if char in abc:
        for i in range(len(abc)): #len(abc)
        #----Cuando encuentro la letra, guardo esa letra/índice
            if char == abc[i]:
                char_indice = i
            
                if char_indice + 13 >= 26:
                    char_indice = char_indice - 26
            
                nuevo_indice = char_indice + 13
                letra_cifrada = abc[nuevo_indice]

        mensaje_cifrado = mensaje_cifrado + letra_cifrada
    elif char in abc_mayus:
        for i in range(len(abc_mayus)): #len(abc_mayus)
        #----Cuando encuentro la letra, guardo esa letra/índice
            if char == abc_mayus[i]:
                char_indice = i
                # Si la letra está en la segunda mitad del alfabeto:
                if char_indice + 13 >= 26:
                    char_indice = char_indice - 26
            
                nuevo_indice = char_indice + 13
                letra_cifrada = abc_mayus[nuevo_indice]
        mensaje_cifrado = mensaje_cifrado + letra_cifrada
    
    else:
        mensaje_cifrado = mensaje_cifrado + char

        
    print("Este es el mensaje cifrado letra por letra en la iteración: ", mensaje_cifrado)
    print(" ")
print("Este es el mensaje cifrado ejecutado de una sola vez: ", mensaje_cifrado) 
if mensaje_cifrado == mensaje_comparacion:
    print("El mensaje ", mensaje, "y el mensaje", mensaje_comparacion, "son mensajes que se corresponden en la encriptación")
else:
    print("El mensaje ", mensaje, "y el mensaje", mensaje_comparacion, "son mensajes que NO se corresponden en la encriptación")