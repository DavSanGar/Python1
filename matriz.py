'''Crea un script que dada una lista de listas M (numérica), identifique si se trata de una matriz y en
ese caso imprima dos listas correspondientes a:
1. La fila cuyos elementos suman el máximo
2. La columna cuyos elementos suman el máximo
Si no se trata de una matriz devolverá dos listas vacías.
Por ejemplo:
M1=[[2,5,3],[6,1,8],[7,5,4]] devolverá: L1 = [7,5,4] y L2 = [2,6,9,7]
M2 = [[4,2,3],[4,5],[6,8,2]] devolverá: L1 = [] y L2 = []
(Nota: Definimos matriz como una lista de listas donde todas las listas internas tienen el mismo
numero de objetos)'''
# Definir la lista de listas M
M = [[2, 5, 3],
     [6, 1, 8],
     [1, 5, 4]]

#Verificar si M es una matriz
n_columnas = len(M[0])
n_filas = len(M)
es_matriz = True
#Recorrer todas las listas de M
for i in range(0, n_filas):
    if len(M[i])!= n_columnas:
        es_matriz = False
        break

#Parte 1 --- # Calculamos la suma máxima de cada fila e imprimimos
#Si es una matriz se ejecuta esta parte:
if es_matriz == True:
    sum_maxima_fila = 0 
    for i in range(0, n_filas):
        sum_fila = sum(M[i]) 
        if sum_fila > sum_maxima_fila:
            sum_maxima_fila = sum_fila  
            num_fila = i  
    
    print("La suma máxima de valores en una fila es ",sum_maxima_fila, "y la fila que contiene la suma mayor es ", num_fila)
    print("---")
    
#Parte 2
#Si es una matriz (M)
if es_matriz == True:
    sum_maxima_columna = 0 
    for j in range (0,n_columnas):
        sum_columna = 0 
        columna =[] 
        for fila in M: 
            sum_columna = sum_columna + fila[j]
            columna.append(fila[j])
            if sum_columna > sum_maxima_columna:
              sum_maxima_columna = sum_columna
              columna_mayor = j


    print("La suma mayor de todas las columnas es ", sum_maxima_columna, "y pertenece a la columna ", columna_mayor)
    print("---")
