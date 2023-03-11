#Capitulo 13 Eliminar elementos con remove()

'''El metodo remove sirve para eliminar elementos de una lista sin su numero de posicion
En su lugar establecemos literalmente el valor a eliminar
Sintaxis: "lista.remove(Valor a eliminar)" '''

#Elimina de la siguiente lista los elementos 'amarillo' y 'rojo'
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
colores.remove('amarillo')
colores.remove('rojo')
print('La lista actualizada es:',colores)