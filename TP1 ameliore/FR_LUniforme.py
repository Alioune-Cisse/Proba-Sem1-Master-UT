# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 08:03:26 2020

@author: lenovo
"""

#Fonction de répartition Loi uniforme contiue sur [a,b]
import numpy as np
import matplotlib as plt
a=int(input("Saisir la borne gauche de l'intervalle: "))
b=int(input("Saisir la borne droite de l'intervalle: "))
while a>=b:
    b=int(input("Saisir un nombre superieur a la premiere: "))
def fr(z):
    if z<a:
        return 0
    elif a<=z and z<=b:
        return (float((z-a)/(b-a)))
    else:
        return 1
abs=np.linspace(a-10, b+10, 300)
y2=[fr(z) for z in abs]
plt.pyplot.plot(abs,y2, color="black", label='Fonction de repartition')
plt.pyplot.xlabel("Axes des abscisses", color="darkblue", size=16)
plt.pyplot.ylabel("Axes des ordonnees", color="darkblue", size=16)
plt.pyplot.title("F.R. Loi uniforme continue sur l'intervalle ["+str(a)+", "+str(b)+"]", color="darkblue", size=13)
plt.pyplot.legend()