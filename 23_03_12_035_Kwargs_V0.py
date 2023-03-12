#Capitulo 36 **kwargs
'''El **kwagrs es para el uso de argumentos arbitrarios
en diccionarios '''

def paises(**kwargs):
    print("El proximo país a visitar sera", kwargs['pais3']+".\n")

paises(pais1='México', pais2='Colombia', pais3='Inglaterra', pais4='Islandia')
#El diccionario tiene que ser escribo de la forma anterior y no en corchetes

#Ejemplo de return
def suma(x,y):                      #definicion de funcion
    return x+y                      #realizamos la suma con return
total = suma(27, 33)                #nombramos a total = a la funcion con sus args
print("El valor final es:", total)  #realizamos impresion de resultaod

