sueldos = []
for x in range(5):
    valor = int(input("Ingreser sueldo: "))
    sueldos.append(valor)
print("Lista sin ordenar: ")
print(sueldos)
for x in range(4):
    if sueldos[x] > sueldos[x + 1]:
        aux = sueldos[x]
        sueldos[x] = sueldos[x + 1]
        sueldos[x + 1] = aux
print("Lista con el ultimo elemento ordenado: ")
print(sueldos)

