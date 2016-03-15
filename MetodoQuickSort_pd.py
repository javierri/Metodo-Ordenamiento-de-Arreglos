# Metodo de Ordenamiento por Selección 
# Observación: Pivote a la derecha
# Ver en ... https://repl.it/BuVO
# Autor: Javier Rivera (UNEFA Mérida)

def OrdQuickSort(arreglo):
    
    if (len(arreglo) <= 1):
        return arreglo
    
    i = 0
    pivote = len(arreglo)-1
    while (i < pivote):
        if (arreglo[i] > arreglo[pivote]):
            elem = arreglo[i]
            del arreglo[i]
            arreglo.append(elem)
            pivote = pivote-1
        else:
            i = i + 1
            
    a1 = OrdQuickSort(arreglo[0:pivote])
    a2 = OrdQuickSort(arreglo[pivote+1:])
    
    return a1 + [arreglo[pivote]] + a2

# PRINCIPAL

arreglo = [4,6,2,8,3,5,1,7,9,5]
print "Inicial", arreglo
arreglo = OrdQuickSort(arreglo)        
print "Ordenado", arreglo
