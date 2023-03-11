# Capitulo 30 for - El tipo de dato range() 
'''El range() nos ayudara a incrementar los valores de una variable
Sintaxis: range(Veces a incrementar)
Sintaxis 2: range(inicio del valor de incremento, final de incremento)
Sintaxis 3: range(inicio del valor de incremento, final de incremento, cantidad de incremento o decremento)'''

#Crea un bucle for con un range() que vaya desde el valor 
# 7 hasta el valor 700 en saltos de 100. 
# Basta con que imprimas el valor de cada iteración.
for x in range(7,700,100):
    print('Valor de x'+ x)
