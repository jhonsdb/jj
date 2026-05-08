#A diferencia de las listas o las tuplas, no se puede utilizar un índice para acceder a un elemento de un conjunto, pero se puede:
#Iterar a través de los elementos de conjunto
#Realice una verificación de membresía usando la palabra clave en

mySet = {1,2,3}
for num in mySet:
    print(num)
print(1 in mySet)

#Eliminar elementos de un conjunto
#remove() elimina un elemento de un Set.  
# Si un elemento no existe en el conjunto, devolverá un error.

mySet.remove(2)
print(mySet)

#discard() es el mismo que remove(), pero cuando se usa discard(), 
#eliminar un elemento que no existe en el conjunto, no produce un error.
mySet.discard(3)
print(mySet)
#pop() se utiliza para eliminar un elemento aleatorio de un conjunto. 
# Por lo general, es el elemento superior en la pila de memoria de 
# conjuntos, pero como los conjuntos no están ordenados,
# no puede estar seguro de qué elemento se va a extraer.
mset = {1,2,3,4,5,6,7}
eliminado = mset.pop()
print(mset)
print("el eliminado es "  , eliminado)