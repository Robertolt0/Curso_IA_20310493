#Capitulo 17 Ordenar elementos con sort() y sorted()
'''El metodo sort nos ayuda a aordenar alfabeticamente 
de forma ascendete los datos de una lista
Sintaxis: lista.sort()
Para realizarlo de forma descendente sera de la siguiente forma:
lista.sort(reverse=True)

El metodo sort es permante y el metodo sorted es temporal'''

#Ordena la siguiente lista en orden alfabético descendente
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón',
          'lila', 'negro', 'rosa', 'blanco', 'naranja']

colores.sort(reverse=True)
print(colores)