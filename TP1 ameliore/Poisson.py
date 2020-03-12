# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 10:44:26 2020

@author: lenovo
"""


#Loi de Poisson
import math
import numpy as np
import matplotlib.pyplot as plt

lambdas=int(input("Saisir Lambda: "))
while lambdas<=0:
   lambdas=int(input("Saisir Lambda: "))
def poissons(k):
    k=int(k)
    return math.exp(-1*lambdas)*(lambdas**k)/ math.factorial(int(k))
abs=np.linspace(0,lambdas+50,200)
y=[poissons(x) for x in abs]
plt.plot(abs,y, color="darkgreen")
plt.title("Loi de Poisson de paramètre lambda = "+str(lambdas), color="darkgreen")