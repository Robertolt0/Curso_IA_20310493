#Capitulo 19 Crear y manejar tuplas
'''Las tuplas son una serie de datos que no estan sujetas a cambios
como en el caso de las listas. 
Sintaxis: tupla=('Datos') se diferencias de las listas por el parentesis'''

#Imprime la segunda posición de esta tupla.
colores = ('rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja') #es una tupla por tener los datos en parentesis
print('El color es:',colores[1])

#Utiliza los símbolos de suma y resta para obtener el resultado 25
numeros = (10, 1, 5, 11)
operacion= numeros[3]-numeros[1]+numeros[0]+numeros[2]
print('El resultado de la operacion es:',operacion)