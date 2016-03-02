# Metodo de Ordenamiento por Inserción 
# Observación: Ninguna
# Autor: Javier Rivera (UNEFA Mérida)

arreglo = [5,3,4,2,6,1,7,9,3,8,6]

i = 1
for elem in arreglo[1:]: # Recorre los elementos del arreglo la pos 1 hasta el fin
    j = i - 1
    while (j >= 0): # Recorre los elementos del arreglo desde posicion de elem-1 hasta 0
        # Busca posiciòn donde va a insertar elem
        if (arreglo[j] < elem):
            del arreglo[i]
            arreglo.insert(j+1,elem) 
            break
        # Inserta al inicio (posiciòn 0) en caso de ser menor que el primer elemento
        if (j == 0 and arreglo[0] >= elem):
            del arreglo[i]
            arreglo.insert(0,elem)
        j = j - 1
    i = i + 1

print arreglo
