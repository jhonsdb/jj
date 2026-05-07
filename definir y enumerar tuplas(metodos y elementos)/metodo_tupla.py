#En esta sección, consideraremos diferentes métodos 
# que se pueden usar con Tuplas.

#metodo len()  un método integrado de Python, devuelve el número de elementos de una tupla
tupleTwo = (1,2,4,4,5)
print(len(tupleTwo))
#El método max(), un método incorporado de python, devuelve el elemento más grande en una tupla
print(max(tupleTwo))
#El método min(), un método incorporado de Python, devuelve el elemento más pequeño de una tupla.
print(min(tupleTwo))
#El método index() es un método de tupla utilizado para encontrar un índice de un valor, 
# pero si no hay ningún elemento que contenga el valor, el método devolverá un error, aquí hay un ejemplo:
tulpeThree = "x","b","w","d"
print(tulpeThree.index("b"))
#count() método como en las listas, devuelve el número de veces que aparece un valor 
# en una tupla. En el caso de que un elemento no esté en la tupla, devuelve cero
print(tupleTwo.count(4))
#El método tuple() crea una tupla a partir de una colección de valores.
inTtuple =tuple([3,5,8]) 
print(inTtuple)
print(type(inTtuple))


#ACTIVIDAD TUPLA

horario = [("lunes","mañana","john"),("lunes","noche","Collin"),("martes","mañana","Sedney"),("martes","noche","Carla")]
nuevaTupla = horario[1] + horario[3]
print(nuevaTupla.count("noche"))
print(nuevaTupla.index("martes"))
nombre = ("john","Collin","sedney","carla")
print(max(nombre))