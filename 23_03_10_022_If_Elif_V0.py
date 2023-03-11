#Capitulo 23 El condicional if elif else e input
'''El metodo input sirve para soplicitar datos al usuario
El metodo input recibe informacion en strings
La instruccion elif nos ayuda a dar parametros sobre si es cierto o verdadero'''

#Al siguiente código añádele un par de rangos de edad. Uno de 18 años hasta 45 y otro de más de 100 años hasta 120.
edad = int(input('¿Cuál es tu edad?\n'))
if edad <= 0:
	print('Nadie puede tener esa edad.')
	
elif edad >= 1 and edad <= 18:
	print('Eres menor de edad.')
	
elif edad >= 18 and edad <= 45:
	print('Eres un adulto entre 18 y 45 años.')
	
elif edad >= 45 and edad <= 100:
	print('Eres un adulto mayor')
	
elif edad >= 100 and edad <= 120:
	print('Eres mayor de edad que muchas personas.')
else:
	print('Edad no válida.')