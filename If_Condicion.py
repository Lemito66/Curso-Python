# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 18:51:42 2021

@author: lemit
"""

#Condiciones 
#En un while siempre hay ciclos dependiendo la condicion 
c=2
d=2
if c>d:
    print ('Esto es lo correcto')
elif c<d:
    print('Esto es incorrecto')
elif c==d:
    print ('me da igual')
    

c=2
d=5
if c>d:
    print ('Esto es lo correcto')
else:
    print("Todo el resto")
    

c=8
d=5
if c>d and d==5 :#las dos se deben cumplir para que funcione con and
    print ('Esto es lo correcto')
    

if c>d or d==5 :#Solo una se debe cumplir 
    print ('Esto es lo correcto')
    
    
