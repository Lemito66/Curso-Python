# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 20:28:16 2021

@author: lemit
"""
#el as es una abreviación 
import pandas as pd
#lo de arriba los titulos
data = pd.read_excel('Archivos Excel\Info (1).xlsx')# lo de la izquierda los indices 
print(data['Fondo'])


data.replace(1000,40, inplace=True)#Una forma 
#x= data.replace(1000,40)//Otra forma 

x=data.dropna()
print(data)
print(x)

# data.dropna(inplace = True)#Borro la que estaba vacia
# print (data)

import numpy as np
data.replace(np.nan,0, inplace=True)#Remplazar lo que esta vacio
print (data)


y= data[data['Monto']>1000 ]
print (y)

#Crear columnas 
data['Euros']=data['Monto']* 0.84
print(data)

data.drop(['Euros'],'columns', inplace=True)#Borrar columna
print (data)

data.drop([2],'rows', inplace=True)#Borrar fila
print (data)

# data.rename(columns=({'Fondo': 'Fondito','Año':'Añio', 'Monto':'Montio', inplace=True}))
# print(data) Renombrar columna

data.to_excel('Archivos Excel\Resultados_Pandas.xlsx', sheet_name='resultado',index=False) #Enviar a excel

#Se usa llaves cuando se usa diccionario
#Listas con corchetes
#Ver si la demanda ha ido creciendo en los ultimos 5 años 
#e ingresos 

print ("-------------------")
from scipy.stats import linregress
x=[1,2,3,4,5]
y=[322,435,7679,8978,5467]
slope,intercept, r, p,stderr = linregress(x,y)
print (slope)

import matplotlib.pyplot as plt

plt.scatter(x,y)
#plt.plop(x,y,linestyle='solid')
plt.title('Orquideas Alemania')
plt.xlabel('Años')
plt.ylabel('Monto')
plt.show()