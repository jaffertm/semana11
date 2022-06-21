m = []
n = int(input("Ingrese el total de filas y columnas de la matriz: "))
for i in  range(n):
    m.append([])
    for j in range(n):
        m[i].append(int(input("Ingresar el valor de la fila"+ str(i +1) + "columna"+ str(j +1) + ":")))
print("Los valores de la diagonal son: ")
for i in range(n):
    print(m[i][i])