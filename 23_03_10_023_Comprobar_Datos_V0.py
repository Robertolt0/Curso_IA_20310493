#Capitulo 24 Comprobar datos en listas y tuplas 
'''Para al comprobacion del dato usamos la palabra "in"
para verificar que se encuentre dentro de la lista o tupla'''

#Haz una tupla que contenga cuatro colores de tu elección. 
# Tendrás que poner una condición con el condicional if para 
# cada color que le avise al usuario que el color está en la 
# tupla con un mensaje como este: print('El color rojo está 
# admitido') y una condición False para contemplar cualquier 
# color que no esté en la tupla con un mensaje como este: 
# print('Color no admitido'). No puedes utilizar el operador 
# ==. Además tendrás que hacer esto 
# con un input() que permita introducir un color al usuario

new=input('Ingrese el color a verificar:\n')
colores=('rojo', 'azul', 'verde', 'negro')

if new in colores:
    print('El color',new,'está admitido')
else:
    print('Color', new, 'no admitido')