# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 18:07:27 2021

@author: lemit
"""

x=["Emill", "Jorge","Naomi"]
print(x[-2])
print (1+1)
print(len(x))

y=[1,2,3,4,5]
# print(y[0])
# print(y[1])
# print(y[2])
# print(y[3])
# print(y[4])

for elemento in y: #y es el iterable --elemento es la variable
    print ('[' + str(elemento) + ']' + '\n')
    
y=[1,2,3,4,5]
y=y[0:-1]
#Permite repetir una serie de acciones n veces 
for elemento in y: #y es el iterable --elemento es la variable
    print (elemento)
    
print (elemento)

#Repetir secuencias de acciones pero con una condicion 
a=0
b=1
while(a<b):
    print(str(a) + " es mayor que  b ")
    break

while(a<b):
    a=b
    b=a-b
print(b)
    
    
y= range(1,100,2)#Empieza, termina, saltos 
for elemento in y: #y es el iterable --elemento es la variable
    print (elemento)
    
