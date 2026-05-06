str1 = "El codigo incorrecto  peuede limpiar.Pero es muy caro"
str2 = "Se el cambio que deseas ver en el mundo"
str3 = "El gran secreto de la vida es que no hay secreto"
con_str = str1 + str2 + str3
print(con_str)
ext_str = con_str[10:20]#extraer un rango de caracteres en dichas posiciones
print(ext_str)
print(ext_str.replace("e" , "a"))#mira la cadena y remplaza la letra "e" por la "a"
print("secreto" in con_str)#mira la cadena y compruba si dentro tenemos el texto "secreto"
print(con_str.lower())
#print(con_str.split(" "))
print("/".join(con_str.split(" ")))
