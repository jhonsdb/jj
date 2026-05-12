"""
No se pueden crear conjuntos anidados de forma normal, 
como las listas. Como se explicó anteriormente, 
los conjuntos no pueden contener valores mutables, 
que incluyen conjuntos. En consecuencia, en el caso de que 
necesitemos anidar un conjunto, necesitamos tener un tipo 
inmutable como conjuntos, que es frozenset
"""
inmmutableSet = frozenset({"y","z","x"})
inmmutableSet2 = frozenset({"a","b","c"})
nestedSet = set([inmmutableSet , inmmutableSet2])
print(nestedSet)