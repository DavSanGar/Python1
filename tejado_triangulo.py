#En una obra es necesario construir para el tejado de una casa una estructura triangular con tres
#piezas. El ingeniero se pregunta si dadas la largura de las piezas que ha recibido podrá construir
#esta estructura. Crea un script que dados tres longitudes indique si podría construirse un triangulo
#con esas piezas.
#(Pista: la suma de dos piezas tiene que ser mayor que el lado restante. Esto debe ser así para
#todas las posibles combinaciones)


# --- Pedir al usuario tres longitudes
lado1 = int(input("Indica la longitud del primer lado: "))
lado2 = int(input("Indica la longitud del segundo lado: "))
hipotenusa = int(input("Indica la longitud del tercer lado: "))


# --- Comprobar si pueden conformar un triangulo: 
if (lado1 + lado2) > hipotenusa:
    print("El tejado se puede crear")
else:
    print("El tejado no se puede crear")