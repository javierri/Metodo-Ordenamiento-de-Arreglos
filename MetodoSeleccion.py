# Metodo de Ordenamiento por Selección 
# Observación: Solo funciona si el arreglo no tiene elementos repetidos
# Autor: Javier Rivera (UNEFA Mérida)

arreglo = [5,3,4,2,6,1,7,9,8]

menor = arreglo[0]
for i in range(len(arreglo)):
    menor = arreglo[i]
    for elem in arreglo[i:]:
        if (elem < menor):
            menor = elem
    
    if (menor < arreglo[i]):
        arreglo.remove(menor)
        arreglo.insert(i,menor)

print arreglo
