# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 19:46:28 2021

@author: lemit
"""
#Lo que traes de otra funcion se puede llamar como quieras
def promedioDeNotas(notasAlumnos): #Sintaxis de funcion El a puede ser diferente a lo que debe traer 
    #Sacar el promedio de un numero     
    suma=0
    for valorQueCambia in notasAlumnos:
        suma= valorQueCambia+suma
    longitud= len(notasAlumnos)
    promedio= suma/longitud
    return promedio, longitud#lo que quiero que me devuelva por eso se usa return 
    
notasAlumnos=[17,18,19,20]
emill, cuenta =promedioDeNotas(notasAlumnos)
otroAlumno=[15,14,13,12,10]
print(promedioDeNotas(notasAlumnos))
#print(promedioDeNotas(longitud))
#print(promedioDeNotas(otroAlumno))

