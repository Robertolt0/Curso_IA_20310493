#Capitulo 16 Insertar elementos con insert()

'''El método insert() funciona con dos parámetros, primero el número de posición 
donde quieres posicionar el elemento y después, el elemento a añadir
Sintaxis: "lista.insert(posicion,'Valor')"     '''

#Añade a la siguiente lista los colores 'magenta' y 'turquesa' utilizando insert(). 
# Tendrás que posicionar 'magenta' en la posición siguiente a la de 'lila' y 'turquesa' en la penúltima posición. 
# Deberás hacer esto utilizando posiciones de lista negativas.
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
colores.insert(-4,'margenta')
colores.insert(-1,'turquesa')
print('La nueva lista es:',colores)