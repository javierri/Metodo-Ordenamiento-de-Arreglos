# Metodo de Ordenamiento por Burbuja 
# Observación: Método mejorado
# Autor: Javier Rivera (UNEFA Mérida)

arreglo = [2,4,1,7,5,3,8,9,6]

Ordenado = False
while (Ordenado == False):
    i = 0
    Ordenado = True
    for elem in arreglo[0:len(arreglo)-1]:
        if (elem > arreglo[i+1]):
            Ordenado = False
            aux = arreglo[i+1]
            del arreglo[i+1]
            arreglo.insert (i,aux)            
                      
        i = i + 1
        
print arreglo
