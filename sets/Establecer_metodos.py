#Los siguientes son algunos métodos que puede usar con conjuntos 
# para varios propósitos. Algunos son métodos de python incorporados, 
#otros son métodos establecidos

#len(), un método incorporado, devuelve 
# el número de elementos en el conjunto, como en el siguiente ejemplo:
sampleSet = {"escritorio","asiento","tabkero"}
print(len(sampleSet))

#type(), un método incorporado, se utiliza para devolver 
# el tipo de datos de la variable set, como en el siguiente ejemplo:
print(type(sampleSet))

#set() construye un conjunto a partir de otras estructuras de datos, 
#como en el siguiente ejemplo creamos un conjunto a partir de una tupla

mySet = set(("a","b","c"))
print(mySet)

numbers = set([11, 22, 33, 44])
for index,value in enumerate(numbers):
    print(index, value)

mySet = {'This', 'is', 'a'}  
mySet.update(['small', 'set'])
print(mySet) 