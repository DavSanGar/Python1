#Crea un programa que imprima todos los números primos entre el 2 y el 100. 
# Un numero primo es un numero positivo y entero mayor que uno 
# que no tiene un divisor positivo y entero que no sea 1 o sí mismo.

for num in range(2, 101):
    prime = True
    i = 2
    while prime == True and i < num:
        if num% i == 0:
            prime = False
        i = i + 1
    if prime == True:
        print(num)
        