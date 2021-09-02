# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 19:37:22 2021

@author: lemit
"""

#Aqui se escribe los programas 
#En python se usa funciones 
#Una libreria es una coleccion de funciones
#no hay diferencia con '' o ""
#No hay problemas con espacios
print('Hola')
print(1+1)

#variable es algo que tiene una informarcion
#Juan Esteban=1 asi no se declara
juanEsteban=1
print(juanEsteban)
'''
a=1
b='1'
print(a+b)

a=1
b=int('1')
print(a+b)

a="1"
b='1'
print(a+b)
'''
#listas
x=["Emill","Jorge",1,200,[1,2,3]]
print (len(x)) #Imprimir longitud

print(x[2])#Imprimir posicion 
print(x[-1])
print(x[-1][1])#Dentro de una lista
print(x[-1][-2])
day=31
month='Agosto'
year=2021
print("Hoy es: " + str(day)+ " de " + month + " " + str(year))

print('Hoy es {} de {} del {}' .format(day,month,year))#Sin convertir y solo con strings

print('Este es el resultado de: \n {} y {}'.format(x[-1][-2],x[-1]))

#loops 
y=[1,2,3,4,5]
print(y[0])
print(y[1])
print(y[2])
print(y[3])
print(y[4])

for elemento in y:
    print ('[' + str(elemento) + ']' + '\n')
    
