#Capitulo 37 Clases y objetos

class Autos():          #Creacion de la clase Autos
     modelo= 'Ferrari 488'  #Creacion de las propiedades
     color1= 'Rojo'
     color2= 'Blanco'
     numero= "1/150"
     cilindraje= 12
     activar=True
     aleron= True
     camara=False
     audio= True
    
    #El uso de self es necesario para la creacion del objetos
     def encender(self):  
        self.activar=True
    
     def apagar(self):
        self.activar=False
    
     def prender_audio(self):
        self.audio=True
        return "Audio activado, seleccione su dispositivo\n"

     def apagar_audio(self):
        self.audio=False
        return "Pantalla de despedida"
    
     def prender_camara(self):
        self.camara=True
        print('Reversa activada')
        print('Los objetos pueden estar mas cerca de lo que parece\n')

auto1= Autos()                  #Se crea el objeto auto1 de la clase Autos

auto1.encender()                #Encendido del auto

auto1.prender_audio()           #Encendido de audio
print(auto1.prender_audio())    #Mensaje de pantalla

auto1.prender_camara()          #Activacion de camara de reversa

print('Modelo:', auto1.modelo, '\n')
print('Color:', auto1.color1, '\n')
print('Numero de serie:', auto1.numero)



