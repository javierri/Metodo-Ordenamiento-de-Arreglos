# Metodo de Ordenamiento por Mezcla
# Observación: 
# Ver en: http://www.codeskulptor.org/#user41_7aRfnkPnjH_1.py
# Autor: Javier Rivera (UNEFA Mérida)

def Mezclar (a,b):

    la = len(a)
    lb = len(b)
    
    i = 0
    j = 0
    c = []
    #print a,b
    while (i < la and j < lb):
        
        #print i,j
        if (a[i] < b[j]):
            c.append(a[i])
            i = i + 1
        else:
            c.append(b[j])
            j = j + 1
    
    while (i < la):
        c.append(a[i])
        i = i + 1
    
    while (j < lb):
        c.append(b[j])
        j = j + 1
    
    return c

def OrdMerge (a):
    pi = 0
    pf = len(a)-1
    
    if (pf == 0):
        return a
    
    pm = (pi + pf)/2
    a1 = OrdMerge (a[pi:pm+1])
    a2 = OrdMerge (a[pm+1:pf+1])
    a = Mezclar (a1,a2)
    
    return a
    
    
# PRINCIPAL

a = [4,2,5,8,1,3,9,7,6,12,0] 

print a
a = OrdMerge(a)
print a
