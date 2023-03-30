matriz= []
def mat(n):
    for i in range(n):
        matriz.append([])
        for j in range(n):
            matriz[i].append(0)
    return matriz
def llenar_matriz(n):
    matriz = mat(n)
    for i in range(n):
        for j in range(n):
            matriz[i][j]= int(input("El valor de ", str(x), "][",str(y),"]= "))
def ordenar(n):
    ma=llenar_matriz(n)
    for i in range(n):
        for j in range(n):
            if ma[0][0]==0:
                ma[0][:] = ma[1][:]
                ma[1][:]= ma[0][:]
            else:
                pass
def guass(n):
    for z in range(n-1):
        for x in range(n-z):
            if (matriz[z][z]!=0):
                p = matriz[z+x][z]/ matriz[z][z]
                for y in range(n):
                    matriz[x+z][y] = matriz[x+z][y]*p

def det(n):
    detr=1
    for i in range(n):
        detr = matriz[i][i]*detr
    print("\n el determinante de la matriz es = ", detr)

def detr(n)
    
