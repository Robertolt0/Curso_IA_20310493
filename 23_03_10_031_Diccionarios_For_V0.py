# Capitulo 32 Diccionarios en for
#Como iterar un diccionario en Python con un bucle for
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
for x in '': #Utilizamos el pass para no afectar el codigo solicitado
    #Interacion de diccionario
    for x in teclado2:
	    print(x)
    #Interacion de valores del diccionario
    for x in teclado2:
	    print(teclado2[x])
    pass
#Itera el diccionario teclado1 con un solo bucle for que muestre esto en la consola
for y in teclado1:
	print(y,'=',teclado1[y]+'.')