#- Capítulo 31 ¿Qué son los diccionarios de Python? 
'''Para la creacion de un diccionario usaremos {}'''
teclado1 = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}

teclado2 = {
	'Categoría': 'Teclados',
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59,99'
}

model= teclado2['Modelo']
price= teclado2['Precio']

print('El modelo', model, 'cuesta', price, '$.')
