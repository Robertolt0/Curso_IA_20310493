#Capitulo 34 Crear y llamar funciones
'''Utilizaremos def para crear la funcion
Sintaxis: def Funcion(argumentos):'''

#Crea una función que realice una suma. Para ello, 
# tendrás que añadir dos argumentos (numero1 y numero2). 
# En su interior, especificarás un print() que muestre el 
# resultado de la suma. Deberás hacer tres llamadas que como 
# resultado de la suma den los valores 30, 50 y 57000.

def suma(num1, num2):
    resul=(num1+num2)
    print('El resultado de la suma es:',resul)

suma(20,10)
suma(25,25)
suma(33000,24000)
