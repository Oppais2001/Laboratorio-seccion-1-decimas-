import random

filas=int(input("Ingrese Cantidad de Filas: "))
columnas=int(input("Ingrese Cantidad de Columnas: "))

def Crear_Matriz(x,y):
    matriz = []
    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            valor = random.randint(1,5)
            matriz[i].append(valor)
    return matriz

def Suma_Matrices(m1,m2):

    if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
        m3 = []
        for i in range(len(m1)):
            m3.append([])
            for j in range(len(m1[0])):
                m3[i].append(m1[i][j] + m2[i][j])
        return m3
    
def Resta_Matrices(m1,m2):
    if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
        m3 = []
        for i in range(len(m1)):
            m3.append([])
            for j in range(len(m1[0])):
                m3[i].append(m1[i][j] - m2[i][j])
        return m3

def Imprime_Matriz(matriz):
    for lista in matriz:
        print("[", end=" ")
        for elemento in lista:
            print(elemento, end=" ")
        print("]")
        
m1=Crear_Matriz(filas,columnas)
m2=Crear_Matriz(filas,columnas)
print("Matriz 1:")
Imprime_Matriz(m1)
print("Matriz 2:")
Imprime_Matriz(m2)
m3=Suma_Matrices(m1,m2)
print("La suma de matriz 1 y matriz 2:")
Imprime_Matriz(m3)
m4=Resta_Matrices(m1,m2)
print("La resta de matriz 1 y matriz 2:")
Imprime_Matriz(m4)


