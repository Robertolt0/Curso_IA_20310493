#Capítulo 28 While-If
'''El uso de continue es para saltar instrucciones'''

'''
x=0             #Valor inicial y debemos de +=1
while x<=30:    #Valor de salida del bucle mayor o igual a 30
    if x==4 or x==6 or x==10:
        x+=1        #Incremento en 1
        print('El valor del bucle es: ',x) #Impresion de valor
    
        print('Se saltó el valor ',x ,' de x')
        continue
    if x==15:   #Romprer ejecucion en x=15
        break   #Salimos del ciclo
print('Se rompió la ejecución del bucle cuando x valía ',x)
'''
x=0                 #Valor inicial de x
while x <= 30:      # Condicion de While
    x+=1            # Incremento de x en 1
    if x==4 or x==6 or x==10:   #If condicional
        print('Se saltó el valor ',x ,' de x')
        continue                #Aplicacion de salto de las condicionantes
    if x==15:       #If condicion x igual a 15
        print('Se rompió la ejecución del bucle cuando x valía ',x)
        break       #Roptura del ciclo
    print('El valor del bucle es: ',x)     #Impresion de valores
       
    