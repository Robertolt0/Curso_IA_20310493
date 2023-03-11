# Capitulo 12 Eliminar elemendo con del()
'''El comando del() nos ayudara a elminar elemento de una lista
se puede usar por posiciones positivas y negativas
Sintaxis: "del(lista[posicion])"  '''

#De esta lista, elimina los colores 'azul', 'marrón', 'negro' y 'rosa'. 
# Debes utilizar al menos una vez las posiciones negativas para eliminar un color.
# Después, imprime la lista para ver los colores que se han eliminado.
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']


#Cuando borramos un elemento la lista se modifica, debemos de tomar en cuenta las nuevas posiciones
del(colores[-3],colores[6],colores[4],colores[1])

print("Los colores que existentes son:",colores)