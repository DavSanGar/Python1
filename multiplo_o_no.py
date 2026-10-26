#Escriba un programa que pida dos números enteros y 
# que escriba si el mayor es múltiplo del menor.

numero1 = int(input("Escribe un número: "))
numero2 = int(input("Escribe otro número: "))

if numero1 < 0 or numero2 < 0:
    print("Esta operación no se puede hacer con números negativos")
else:
    if numero1 % numero2 == 0:
        print(numero1, "es multiplo de", numero2)
    elif numero1 % numero2 != 0:
        print(numero1, "no es multiplo de", numero2)



