#Capitulo 39 Cambio de valores en objetos
'''El self funciona como un this, es palabra reservada de python'''

class Usuario:
	def __init__(user, name, password):  #Asignamos el nombre user al self
		user.name = name
		user.password=password

	def imprime_datos(self):            #Self diferente al anterior y a este no lo renombramos
		print('Nombre:', self.name, '\nContraseña:', self.password, '\n')

usuario001 = Usuario('Julian', 'Quinonez33.')    #Asiganacion de argumentos a objeto usuario1

usuario002 = Usuario('Omar', 'Reyes54_23')      #Asiganacion de argumentos a objeto usuario2

usuario002.name = 'Jacinto'                      #Cambiamos nombre a objeto usuario2

usuario001.imprime_datos()
usuario002.imprime_datos()                      #Impresion de datos