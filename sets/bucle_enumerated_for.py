#Se creará un conjunto a partir de una cadena utilizando el método set():
char_set = set("hola")
print(char_set)
#Como la función enumerate devuelve dos valores por cada iteración, un índice y un valor, 
#podemos usar un bucle de la siguiente manera:
for ind,val in enumerate(char_set):
    print(ind,val)