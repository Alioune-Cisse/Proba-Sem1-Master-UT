# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 22:04:52 2020

@author: lenovo
"""
#Loi normale de parametre mu=moyenne et sigma=ecart type
#Cas particulier mu=0, sigma=1 (Loi normale centree reduite)
import numpy as np
import matplotlib.pyplot as plt
import math
mu=int(input("Saisir la moyenne: "))
sigma=int(input("Saisir l' écart type: "))
while mu<0:
   mu=int(input("Saisir la moyenne: "))
while sigma<0:
   sigma=int(input("Saisir l' écart type: ")) 
def normal(x):
    return (math.exp(-((x-mu)**2)/(2*(sigma**2))))
abs=np.linspace(-20,20,200)
y=[normal(x) for x in abs]
plt.plot(abs,y)
plt.grid()
plt.title("X suit N("+str(mu)+","+str(sigma)+")", color="red", size=14)