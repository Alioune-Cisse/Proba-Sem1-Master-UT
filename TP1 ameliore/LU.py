# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 08:03:26 2020

@author: lenovo
"""

#Densité Loi uniforme contiue sur [a,b]
import numpy as np
import matplotlib as plt
a=int(input("Saisir la borne gauche de l'intervalle: "))
b=int(input("Saisir la borne droite de l'intervalle: "))
while a>=b:
    b=int(input("Saisir un nombre superieur a la premiere: "))
def uniforme(x):
    if x<a or x>b:
        return 0
    else:
        return 1/(b-a)
abs=np.linspace(a-5, b+5, 300)
y=[uniforme(x) for x in abs]
plt.pyplot.plot(abs,y, color="darkblue", label="densite loi uniforme")
plt.pyplot.grid()
plt.pyplot.xlabel("Axes des abscisses", color="red", size=16)
plt.pyplot.ylabel("Axes des ordonnees", color="red", size=16)
plt.pyplot.title("Loi uniforme continue sur l'intervalle ["+str(a)+", "+str(b)+"]", color="red", size=14)
plt.pyplot.legend()