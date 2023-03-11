#Capitulo 20 Cómo convertir tuplas a listas y viceversa
'''Para convertir una lista a tupla con "tuple" 
Sintaxis: nombre_de_la_tupla= tuple(lista)

Para ver el tipo de dato "type"  
Sintaxis: print(type(nombre del dato a revisar))" 

Para convertir una tupla a lista con "list" 
Sintaxis: nombre_de_la_lista= list(tupla)
'''
#Convierte la siguiente lista en una tupla y asegúrate que se haya convertido en tupla
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
col_tupla= tuple(colores)
print(type(col_tupla))