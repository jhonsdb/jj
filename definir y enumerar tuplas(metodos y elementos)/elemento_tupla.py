myTuple = (13,21,34,94,10,65)


#cambiar tuplas
#Las tuplas son uno de los tipos de datos inmutables en Python, lo que significa que no 
# podemos cambiar sus valores o agregarles. En el siguiente método,
# explicamos cómo cambiar los elementos tupla, utilizando los métodos list() y tuple().


tempList = list(myTuple)#cambia la tupla en lissta y la almacena en la variable
print(type(tempList))# muetra el tipo de datto que hay en la variable en estet caso la lista
tempList[3] = 999#sustituye en la posicion 3 el dattoo por el 333
tempList.append(777)# añade a la lista el 777 en su ultimo indixe
myTuple = tuple(tempList)#convierte la listya en tupla y lo alamacena en la variable
print(myTuple)#muestra la tupla su  valor