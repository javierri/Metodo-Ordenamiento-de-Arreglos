# Metodo de Ordenamiento por Selección 
# Observación: Pivote a la Izquierda
# Autores: Roentgen Pereira, Yorbelis Davila

def OrdQuickSort(arreglo):
    #condicion de parada
    if (len(arreglo)<=1):
        return arreglo
    print arreglo
    pivote=len(arreglo)-1
    i=0
    #recorrido y ordenamiento
    while (i<=pivote):
        if (arreglo[i]>arreglo[pivote]):
            elem=arreglo[i]
            del arreglo[i]
            arreglo.insert(pivote,elem)
            while pivote<len(arreglo)-1:
                pivote=pivote+1
        else:
            i=i+1
    a1 = OrdQuickSort(arreglo[:pivote])
    a2 = OrdQuickSort(arreglo[pivote+1:])
    
    return a1 + [arreglo[pivote]] + a2
        
        
# PRINCIPAL
print "Ejercicio de método Quick Sort presestado por:"
print "Roentgen Pereira, Yorbelis Davila"

arreglo = [4,6,2,8,3,5,1,7,9,5]
print arreglo
arreglo = OrdQuickSort(arreglo)        
print arreglo
