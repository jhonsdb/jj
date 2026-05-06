sample = "A Sample String"
print(len(sample))###cuenta  los caracteres dentro de un string
print(sample.lower())#convierte texto en minuscula
print(sample.upper())#convierte texto en mayusculas
print(sample.split())#separa el string en divisoria 
splitted = sample.split()
separador = " "
print(separador.join(splitted))#une lo separadoe por espacios en este caso
print(sample.find("ple"))#encuntra la suv¡bcadena y nos dice su posicion
print(sample.replace("ple" , "e"))#remlplaza la subcadena "ple" por "e"
