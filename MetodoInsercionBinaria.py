# Método de ordenamiento por inserción binaria 
# Observación: ver en.. 
# Autor: Javier Rivera (UNEFA Mérida)

# Busqueda Binaria
def buscar(arreglo, elem):
    
    pi = 0
    pf = len(arreglo) - 1
    pm = 0
    
    while (pi <= pf):
        
        pm = (pi + pf)/2
        if (elem == arreglo[pm]):
            return pm 
        if (elem < arreglo[pm]):
            pf = pm - 1
        else:
            pi = pm + 1

    if (len(arreglo) > pm and elem > arreglo[pm]):
        return pm + 1
        
    return pm 
    
# Ordenamiento por Inserción Binaria
def OrdBinario(arreglo):
    arregloOrd = []
    
    for i in range(len(arreglo)):
        pos = buscar(arregloOrd, arreglo[0])
        arregloOrd.insert(pos, arreglo[0])
        del arreglo[0]
        
    arreglo.extend(arregloOrd)

# PRINCIPAL
    
a = [6,4,1,9,2,8,3,5,7,12,0,11]
OrdBinario(a)
print a
