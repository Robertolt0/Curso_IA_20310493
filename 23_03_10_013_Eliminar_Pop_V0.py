#Capitulo 14 Eliminar elementos con pop()

'''El metodo pop() nos ayudara a eliminar un elemento sin nombrar
la posición o el elemento a borrar. Puedes utilizar este método para eliminar 
y almacenar el valor eliminado en una variable 

Ejemplo: 
colores = ['rojo', 'azul', 'verde', 'amarillo']
almacena_valor = colores.pop(2)
print('El color eliminado y almacenado es:',  almacena_valor)

'''
#Elimina de la siguiente lista los elementos 'azul' y 'blanco'. Solo puedes eliminarlos utilizando el método pop().
#Además, tendrás que guardar esos dos colores en una nueva lista.
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
color1=colores.pop(1)
color2=colores.pop(-2)

lista_nueva=[color1, color2]
print('Los colores guardados son:',lista_nueva)