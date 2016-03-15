# Metodo de Ordenamiento por Selección 
# Observación: Pivote en el centro
# Ver en ... https://repl.it/BwK2/2
# Autor: Cruz ricardo, Nestor Peña, Vanessa Suarez, Alan Atencio (UNEFA Mérida)

def OrdQuickSort(arreglo):
    
    if (len(arreglo) <= 1):
        return arreglo
    
    i = 0
    pivote = (len(arreglo))/2
    while (i < pivote):
        if (arreglo[i] > arreglo[pivote]):
            elem = arreglo[i]
            del arreglo[i]
            arreglo.insert(pivote,elem)
            pivote = pivote-1
#            print "Arreglo Izquiero ",arreglo
#     borrar el # Para mostrar cada cambio Efectuado  
            
        else:
            i = i + 1
    
    pivote = (len(arreglo))/2
    j=len(arreglo)-1
    while (j > pivote):
        if (arreglo[pivote] < arreglo[j]):
            j=j-1
        else:
            elem = arreglo[j]
            del arreglo[j]
            arreglo.insert(pivote,elem)
            pivote = pivote+1
#            print "Arreglo Derecho ",arreglo
#     borrar el # Para mostrar cada cambio Efectuado  
            
    a1 = OrdQuickSort(arreglo[0:pivote])
    a2 = OrdQuickSort(arreglo[pivote+1:])
    
    a= a1 + [arreglo[pivote]] + a2
#    print "\n Arreglo por Orden ",a
    return a
# PRINCIPAl
arreglo = [4,6,2,8,3,5,1,7,9,5]
print "Arreglo Original sin Ordenar ",arreglo
arreglo = OrdQuickSort(arreglo) 
print "\n Arreglo Final Ordenado ",arreglo
