# Metodo de Ordenamiento por Selección 
# Observación: Pivote al Centro
# Autores: Euduar Zerpa, GGepsy Ortiz

def OrdQS (a):
	if (len(a)<=1) :
		return a
	pivote = len(a)/2
	i=0
	while (i < pivote):
		if (a[i] > a [pivote]):
			elem = a[i]
			del a[i]			
			a.append(elem)		
			pivote = pivote - 1
		else:
			i = i+1
	i = len(a)-1
	while (i > pivote):
		if (a[i] < a [pivote]):
			elem = a[i]
			del a[i]			
			a.insert(0,elem)		
			pivote = pivote + 1
		else:
			i = i-1
	a1 = OrdQS (a[:pivote])
	a2 = OrdQS (a[pivote+1:])
	return a1 + [a[pivote]] + a2
	
# PRINCIPAL

arreglo = [4,6,2,8,3,5,1,7,9,5]
print arreglo

arreglo = OrdQS(arreglo)
print arreglo
