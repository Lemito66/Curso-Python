# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 18:10:53 2021

@author: lemit
"""
#Importar librerias 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress


#Importar la informacion contenida en el archivo

df = pd.read_excel('Archivos Excel\Data.xlsx')# lo de la izquierda los indices

#Sacar un subset de datos correspondientes a los años 
#2015-2019
df_5 =df[df['Año']>=2015]
df_5 =df[df['Año']<=2019]
#print(df_5)



#Sacar los valores unicos de variedad

variedades = df_5['Variedad'].unique()
paises=df_5['País'].unique()
years=df_5['Año'].unique()
#print(paises)



#Filtra por variedad 

for variedad in variedades:
    filtroVariedad=df_5[df_5['Variedad']==variedad]
    #print(filtroVariedad)

#filtrar por país
    for pais in paises:
        filtroPaises=filtroVariedad[filtroVariedad['País']==pais]
        print (filtroPaises)
#filtras por año
        toneladas=[]
        ingresos=[]
        for year in years:
            filtroYears= filtroPaises[filtroPaises['Año'] == year]

#sumas las toneladas por año 
            toneladas.append(filtroYears['Toneladas'].sum())
 
#sumar los usd
            ingresos.append(filtroYears['USD'].sum())
        #print(ingresos)
    


#hacer una regresión lineal entre periodo de años y toneladas de las ultimos 5 años
        slope_tnd, intercept,r,p,stderr = linregress(years,toneladas)
        
        slope_usd, intercept,r,p,stderr = linregress(years,ingresos)
        


#Comprobar que las pendientes de ambar regresiones sean posivtivas 
        if slope_tnd > 1 and slope_usd > 1:
            

#Graficar un scatter plot donde en x están los años y en las toneladas
            plt.scatter(years,toneladas)
            plt.xlabel('Años')
            plt.ylabel('toneladas')                       
            plt.title('{} {}'.format(variedad,pais))
            plt.show()
#Graficar un scatter plot donde en x están los años y en las toneladas
            plt.scatter(years,ingresos)
            plt.title('{} {}'.format(variedad,pais))
            plt.xlabel('Años')
            plt.ylabel('USD') 
            plt.show()