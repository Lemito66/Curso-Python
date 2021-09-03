# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 19:10:52 2021

@author: lemit
"""
#Sacar algoritmo para sacar el promedio de una lista

sumaTotal =0
x=[17,18,19,20]
for suma in x:
    #sumaTotal+=suma
    sumaTotal = sumaTotal + suma #Suma de todos los elementos de x
    
longitud = len(x)
print(longitud)
promedio = sumaTotal/longitud #Realizar promedio
print("El promedio total del estudiante es: " + str(promedio))


#Intento del profe

