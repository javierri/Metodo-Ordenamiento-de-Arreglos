# Metodo de Ordenamiento por Inserción 
# Observación: Ninguna
# Autor: Javier Rivera (UNEFA Mérida)

arreglo = [5,3,4,2,6,1,7,9,3,8,6]

i = 1
for elem in arreglo[1:]:
    j = i - 1
    while (j >= 0):
        if (arreglo[j] < elem):
            del arreglo[i]
            arreglo.insert(j+1,elem)
            break
        
        if (j == 0 and arreglo[j] >= elem):
            del arreglo[i]
            arreglo.insert(0,elem)
            
        j = j - 1
           
    i = i + 1

print arreglo
