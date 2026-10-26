#En una hamburguesería han abierto la posibilidad de hacer pedidos online. Ofrecen básicamente
#dos productos de fama mundial: su hamburguesa clásica y la hamburguesa vegana.
#Los ingredientes extra de la hamburguesa clásica son:
#- Queso Idiazabal
#- Bacon
#- Huevo
#Los ingredientes extra de la hamburguesa vegana son:
#- Tofu
#- Cebolla caramelizada
#Crea un script que le pregunte al usuario que tipo de hamburguesa quiere. En función de la
#respuesta debe enseñarle los ingredientes extra disponibles y permitirle escoger uno de ellos.
#Finalmente debe imprimir por pantalla que tipo de hamburguesa se ha elegido y cuales son sus
#ingredientes.


# --- Pedir al usuario el tipo de hamburguesa
hamburguesa = input("Tenemos dos hamburguesas en venta online. La hamburguesa clasica y la vegana. ¿Cuál prefieres? ")
hamburguesa = hamburguesa.title()


# --- Comprobamos que hamburguesa ha pedido el usuario
# Si ha elegido la clasica
if hamburguesa == "Clasica":
   
    ## Ofrecemos la opción de elegir un ingresiente extra: queso, bacon, huevo

    print("Los ingredientes extra de esta hamburguesa son: Queso Ideazabal, Bacon y Huevo. Sólo puedes elegir uno. ¿Cuál prefieres? ")
    ingrediente_extra = input()
    ingrediente_extra = ingrediente_extra.lower()
    ## Imprimiremos que tipo de hamburguesa ha elegido
    if ingrediente_extra == "queso ideazabal" :
        print("""La hamburguesda que has elegido contiene: 
        - 180gr de carne de vaca gallega 
        - tomate 
        - lechuga batavia 
        - cebolla morada
        - queso ideazabal 
        El precio es: 11.25€""")
    elif ingrediente_extra == "bacon" :
        print("""La hamburguesda que has elegido contiene: 
        - 180gr de carne de vaca gallega 
        - tomate 
        - lechuga batavia 
        - cebolla morada
        - bacon 
        El precio es: 11.45€""")
    else: 
        print("""La hamburguesda que has elegido contiene: 
        - 180gr de carne de vaca gallega 
        - tomate 
        - lechuga batavia 
        - cebolla morada
        - huevo 
        El precio es: 10.95€""")

 

#Si ha elegido la vegana
if hamburguesa == "Vegana":

    ## Ofrecemos la opción de elegir un ingresiente extra: tofu, cebolla caramelizada
    print("Los ingredientes extra de esta hamburguesa son: tofu y cebolla caramelizada. Sólo puedes elegir uno. ¿Cuál prefieres? ")
    ingrediente_extra = input()
    ingrediente_extra = ingrediente_extra.lower()
    ## Imprimiremos que tipo de hamburguesa ha elegido
    if ingrediente_extra == "tofu" :
        print("""La hamburguesda que has elegido contiene: 
        - 120 gr seitán 
        - tomate 
        - lechuga batavia 
        - seta de cardo empanada
        - tofu
        El precio es: 28.95€ """)
    else:
        print("""La hamburguesda que has elegido contiene: 
        - 120 gr seitán 
        - tomate 
        - lechuga batavia 
        - seta de cardo empanada
        - cebolla caramelizada
        El precio es: 25.95€ """)

    
#Si no elige ninguna de las dos imprimimos mensaje de error
if hamburguesa != "Clasica" and hamburguesa != "Vegana":
    print("¡¡ERROR!!")
  