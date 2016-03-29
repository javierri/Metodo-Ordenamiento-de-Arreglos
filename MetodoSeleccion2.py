 Metodo de Ordenamiento por Selección 
# Observación: funciona si el arreglo tiene elementos repetidos
# Ver en https://repl.it/Bqop/10
# Autor: Javier Rivera (UNEFA Mérida)

arreglo = [5,3,4,2,6,1,7,3,9,8]

menor = arreglo[0]
for i in range(len(arreglo)):
    menor = arreglo[i]
    pos = i
    for j in range(i+1,len(arreglo)):
        if (arreglo[j] < menor):
            menor = arreglo[j]
            pos = j
    
    if (menor < arreglo[i]):
        del arreglo[pos]
        arreglo.insert(i,menor)

print arreglo
