#simulación de red de sensores 
import random

def generar_matriz (n,m):
    matriz = []
    for j in range(n):
        fila = []
        for i in range(m):
            fila.append(random.randint(0,100))
        matriz.append(fila)
    return matriz

def detectar_criticos(matriz):
    criticos = []
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j]> 80:
                criticos.append((i,j,matriz[i][j]))
    return criticos

def mostrar_matriz(matriz):
    print("\nmatriz de sensores: ")
    for fila in matriz:
        print(fila)

def mostrar_criticos(criticos):
    print("\nTemperaturas críticas(> 80 grados): ")
    if len(criticos) == 0:
        print("no se detectaron valores críticos")
    else:
        for sensor in criticos:
            print(f"sensor en [{sensor[0]}][{sensor[1]}]={sensor[2]}grados")

# programa principal
n= int(input("numero de filas: "))
m= int(input("numero de columnas: "))
matriz= generar_matriz(n,m)
mostrar_matriz(matriz)
criticos= detectar_criticos(matriz)
mostrar_criticos(criticos)