myTuple = (13,21,34,94,10,65)
print(myTuple[2])
print(myTuple[1:4])
print(myTuple[-2])

#cambiar tuplas
#Las tuplas son uno de los tipos de datos inmutables en Python, lo que significa que no 
# podemos cambiar sus valores o agregarles. En el siguiente método,
# explicamos cómo cambiar los elementos tupla, utilizando los métodos list() y tuple().


tempList = list(myTuple)
tempList[3] = 999
tempList.append(777)
myTuple = tuple(tempList)
print(myTuple)