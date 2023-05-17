# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 13:35:38 2022

@author: Morales Rergis
Gauss-Jordan
"""
import numpy as np

A=np.array([[1,-2,1],
            [0,2,-8],
            [-4,5,9]])

B=np.array([[0],
            [8],
            [9]])

AB=np.concatenate((A,B),axis=1) # axis=1 : Concatena verticalmente
AB0=np.copy(AB) # Copia de matriz original para imprimir

dimen=np.shape(AB) # (3, 4)
n=dimen[0] # Filas
m=dimen[1]

#Código que cambia filas por haber ceros
for k in range(n):
    AB[k,:]=AB[k,:]/AB[k,k] #Convierte en 1 el pivote
    for j in range(n):
        if j!=k:
            AB[j,:]=AB[j,:]-AB[j,k]*AB[k,:]

print('Matriz aumentada')
print(AB0)
print('Solución :')
print(AB)
    
    
    
    
    
    
    
