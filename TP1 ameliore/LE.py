# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 08:25:39 2020

@author: lenovo
"""

#Densité Loi exponentielle
import numpy as np
import matplotlib.pyplot as plt
import math

lambdas=int(input("Saisir Lambda: "))
while lambdas<0:
    lambdas=int(input("Saisir Lambda (lambdas positif): "))
def exp(x):
    return lambdas* math.exp(-1*lambdas*x)
abs=np.linspace(0,3,200)
y=[exp(x) for x in abs]
plt.plot(abs,y, color="orange", label="densité de probabilité")
plt.grid()
plt.title("Loi exponentielle de paramètre lambda="+str(lambdas), color="blue")
plt.xlabel("abscisses", color="orange", size=16)
plt.ylabel("ordonnees", color="orange", size=16)
#Fonction de répartition
def fr(a):
    if a<0:
        return 0
    else:
        return 1-math.exp(-1*lambdas*a)
abs=np.linspace(0,5,200)
y2=[fr(a) for a in abs]
plt.plot(abs,y2, label='fonction de répartition', color="blue")
plt.legend()