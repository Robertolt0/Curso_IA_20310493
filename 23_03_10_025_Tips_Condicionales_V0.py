# Capitulo 26 Tips para condicionales
'''Para el uso del and debe de cumplirse ambas condiciones
para el uso de or puede cumplirse cualquiera de las dos'''

a = 100
b = 200

if a < b:
	print('a es menor que b.')

x = 10000
y = 200

print('x es menor que y.') if x < y else print('x no es menor que y')