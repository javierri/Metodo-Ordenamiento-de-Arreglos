# Metodo de Ordenamiento por Selección 
# Observación: Pivote a la derecha
# Autor: Javier Rivera (UNEFA Mérida)

def ordenar(a):
    if (len(a) <= 1):
        return a
    
    i = 0
    pivote = len(a)-1
    while (i <= pivote):
        if (a[i] > a[pivote]):
            elem = a[i]
            del a[i]
            a.append(elem)
            pivote = pivote-1
        else:
            i = i + 1
            
    a1 = ordenar(a[0:pivote])
    a2 = ordenar(a[pivote+1:len(a)])
    
    return a1 + [a[pivote]] + a2

# PRINCIPAL

a = [4,6,2,8,3,5,1,7,9,5]
print a
a = ordenar(a)        
print a
