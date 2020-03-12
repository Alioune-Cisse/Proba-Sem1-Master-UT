# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 22:26:24 2020

@author: lenovo
"""

#Loi de Binomiale de parametre n et p
#Cas particulier n=1 (Loi de Bernouilli)

import numpy as np
import matplotlib.pyplot as plt
import math
n=int(input("Saisir n: "))
p=float(input("Saisir p: "))
while n<0:
    n=int(input("Saisir un n positif"))
while p<0 or p>1:
    p=float(input("Saisir p (compris entre 0 et 1): "))
def Ber(k):
    k=int(k)
    return float((math.factorial(n)/(math.factorial(n-k)*math.factorial(k)))* (p**k)* ((1-p)**(n-k)))
abs=np.linspace(0,n,200)
y=[Ber(x) for x in abs]
plt.plot(abs,y, label="fonctin densité")
plt.title("Loi Binomiale de parametre n="+str(n)+" et p="+str(p), color="aqua", size=14)
plt.legend()