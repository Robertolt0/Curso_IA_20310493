#Capitulo 40 clases vacías con pass y eliminar objetos
class Pagina:    #Dejar una clase vacia 
	pass

class Usuario:
	def __init__(user, name, password):  #Asignamos el nombre user al self
		user.name = name
		user.password=password

	def imprime_datos(self):            #Self diferente al anterior y a este no lo renombramos
		print('Nombre:', self.name, '\nContraseña:', self.password, '\n')

usuario001 = Usuario('Julian', 'Quinonez33.')    #Asiganacion de argumentos a objeto usuario1

usuario002 = Usuario('Omar', 'Reyes54_23')      #Asiganacion de argumentos a objeto usuario2

#del usuario001                                 Borrar objeto
#del usuario001.name                            Borrar propiedad
#usuario001.imprime_datos()                     #Impresion de datos
usuario002.imprime_datos()                      #Impresion de datos