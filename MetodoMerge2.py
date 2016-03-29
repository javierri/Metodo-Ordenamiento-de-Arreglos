# Metodo de Ordenamiento por Mezcla
# Observación: Fuente en .. http://www.codeskulptor.org/#user41_Z2MkDt8K1K_3.py
# Ordenamiento por Merge con mezcla en el mismo vector
# Autor: Javier Rivera (UNEFA Mérida)

def Mezclar (a,pi,pm,pf):

    i = pi
    j = pm + 1
    
    while (i <= pm and j <= pf):
        if (a[i] > a[j]):
            elem = a[j]
            del a[j]
            a.insert(i,elem)
            j = j + 1
            pm = pm + 1
        
        i = i + 1
    
def OrdMerge (a,pi=0,pf=None):
    
    if (pf == None):
        pf = len(a)-1
        
    if (pi >= pf):
        return
    
    pm = (pi + pf)/2
    
    OrdMerge (a,pi,pm)
    OrdMerge (a,pm+1,pf)
    Mezclar (a,pi,pm,pf)
    
    
# PRINCIPAL

a = [4, 6, 10, 2, 8, 3, 5, 1, 7, 9, 4, 5] 

print a
OrdMerge(a)
print a
