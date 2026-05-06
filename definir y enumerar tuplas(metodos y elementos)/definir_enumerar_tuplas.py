#tuplas son similares a las listas, una tupla es una coleccion ordenada de onjetos
#la diferencia enntre tuplas y lisas son:
#las tuplas no se pueden cambiar (inmutables) a diferencia de lass listas
#la tuplas usan parentesis, pero las listas usan corchetes
# las tuplas se crean utilizando valores separados por comas entre parentesis o sin parentesis

#tuplaONE = ('sol' , 'luna', 1917 , 20)
# tuplaTwo = (1,2,3,4,4,5)
# tuplaThree = "x","b","w","d" 


tuplaList = [('jhon','smih') , ('jim','Oliver')]
for index, (firstName, lastName) in enumerate(tuplaList):#enumerate() es una función que recorre la lista y añade un índice automático
    print(index,firstName,lastName)

tupleTwo = (1,2,3,4,4,5)
print(len(tupleTwo)) 
#es una función integrada de Python que sirve para contar cuántos elementos hay en una estructura (lista, tupla, string, etc.).