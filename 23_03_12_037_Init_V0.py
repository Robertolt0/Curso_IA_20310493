#Capitulo 38 metodo __init__
'''El metodo __init__ podemos ponerlo en la clases para establecer
los valores iniciales de los objetos
Sintaxis: def __init__(self, argumento1, argumentoN)
Error comun: objeto1= clase()
El error es no poner los argumentos dentro de la clase'''

class Usuarios():                               #Creacion de clase usuario
    def __init__(self, nombre, contraseña):     #Creacion de funcion con init
        self.nombre=nombre                      #Solicitud de nombre
        self.contraseña=contraseña              #Solicitd de contraseña

    def saludo(self):                           #Creacion de funcion saludo
        print('Bienvenido', self.nombre, "Ingresaste correctamente.\n")

    def cierre(self):                           #Creacion de funcion cierre
        print(self.nombre, 'cerraste sesión correctamente.\n')

usuario1=Usuarios('Roberto', '160420')          #Creacion de objeto usuario1

usuario2=Usuarios('Jimena', '156234')           #Creacion de objeto usuario2

usuario1.saludo()                               #Llamado a funcion saludo con usuario1
usuario1.cierre()                               #Llamado a funcion cierre con usuario1
usuario2.saludo()                               #Llamado a funcion saludo con usuario2