import numpy as np

def Suma_Matrices(m1,m2):
    suma=m1+m2
    return suma
def Resta_Matrices(m1,m2):
    resta=m1-m2
    return resta

filas=int(input("Ingrese Cantidad de Filas: "))
columnas=int(input("Ingrese Cantidad de Columnas: "))
matriz1= np.zeros((filas,columnas), int)
print("Ingrese Matriz 1:")
for i in range(filas):
    for j in range(columnas):
        matriz1[i][j] = int(input("Valor para la fila {:2} y columna{:2}:".format(i+1,j+1)))
print("Ingrese Matriz 2:")        
matriz2= np.zeros((filas,columnas), int)
for a in range(filas):
    for b in range(columnas):
        matriz2[a][b] = int(input("Valor para la fila {:2} y columna{:2}:".format(a+1,b+1)))
