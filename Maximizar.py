# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 18:31:41 2021

@author: lemit
"""

import lp

funcionObjetivo = [0.6, 0.1, 0.09]
rhs = [100, 1400, 1000, 180, 175]
lhs = [[1, 0, 0],
       [0, 1, 0],
       [0, 0, 1],
       [0.375, 0.05, 0.0045],
       [1, 0.15, 0.045]
       ]
#'min' 'max'
solution, objetivo =lp.ILP(funcionObjetivo, lhs, rhs,'', 'max')
#Que sea lineal '' que sea entera 'Integer'
import matplotlib as plt 
x=[2,4]
y=[4,8]

plt.plot(x,y)
plt.show()