#Capitulo 35 *Args
'''Los *args o argumentos albitrarios nos ayudan a usarlo
cuantas veces queramos dentro del codigo'''

#¿Cuántos argumentos se utilizan en cada una de estas llamadas?
def colores(*args):  #Uso de args
	pass             #Funcion pass o salto

colores('rojo', 'azul', 'verde', 'amarillo') #Contiene 4 argumentos
colores('lila', 'negro', 'rojo')             #Contiene 3 argumentos
colores('rosa')                              #Contiene 1 argumento
colores('marrón', 'naranja')                 #Contiene 2 argumentos

#Completa el siguiente fragmento de código:
def colores(*args):
	print('El color', args[1], 'es mi favorito.', 'El color', args[0], 'tampoco está mal.')

colores('negro', 'azul') #agregamos los argumentos 

#Crea una función que realice la suma de cinco números utilizando solo *args.
def suma(*args):
    resul= args[0]+args[1]+args[2]+args[3]+args[4]
    print('\nEl resultado de la suma es:', resul, '\n')

suma(3,7,5,5,6)