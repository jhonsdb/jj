#Los conjuntos son otro tipo de objetos que almacenan una colección de elementos. 
# ¿En qué se diferencian los conjuntos de las listas?

#Los conjuntos son colecciones desordenadas
#Los elementos del conjunto son inalterables
#Los conjuntos no están indexados
#Los conjuntos no tienen valores duplicados {}
#Los conjuntos utilizan llaves en lugar de corchetes

#Para crear un conjunto, debe agregar los elementos separados por comas dentro de llaves. 
# Puede contener tipos inmutables como enteros, flotantes, cadenas, booleanos y tuplas, 
# pero no puede contener tipos de elementos mutables como listas o conjuntos

mySet = {1, 2, 3}

myMixedSet = {1, "Bueno", ('a','b','c'), False}

print(mySet)

print(myMixedSet)
#add() se utiliza cuando se agrega un solo elemento al conjunto.
mySet.add(8)
mySet.add(2)
print(mySet)


#update() se utiliza si se van a añadir dos o más elementos a un Set. A continuación se muestra un ejemplo:

mySet.update({10,11})
print(mySet)