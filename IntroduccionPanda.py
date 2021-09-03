# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 20:28:16 2021

@author: lemit
"""
#el as es una abreviación 
import pandas as pd
#lo de arriba los titulos
data = pd.read_excel('Info (1).xlsx')# lo de la izquierda los indices 
print(data['Fondo'])

data.replace(1000,40, inplace=True)#Una forma 
#x= data.replace(1000,40)//Otra forma 

print(data)

# data.dropna(inplace = True)#Borro la que estaba vacia
# print (data)

import numpy as np
data.replace(np.nan,0, inplace=True)#Remplazar lo que esta vacio
print (data)


y= data[data['Monto']>1000 ]
print (y)