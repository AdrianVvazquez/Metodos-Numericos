# -*- coding: utf-8 -*-
"""
Created on Monday Oct 31 2022

@author: Adrian V
Gauss-Seidel
"""
import numpy as np
from  math import exp, sqrt

def x1_n_func(x2_0):
    return (12-(x2_0**3)) / 7

def x2_n_func(x1_n, x2_0):
    return (12 - x1_n + exp(-(x1_n*x2_0))) / 8

def error_func(x1_n, x1_0, x2_n, x2_0):
    error_tmp1 = abs((x1_n - x1_0) / x1_n)**2
    error_tmp2 = abs((x2_n - x2_0) / x2_n)**2
    
    return sqrt(error_tmp1 + error_tmp2)


x1_0 = 1
x2_0 = 1
error = 1
target_error = 0.01
iteracion_n = 0

while(error > target_error):
    x1_n = x1_n_func(x2_0)
    x2_n = x2_n_func(x1_n, x2_0)
    error = error_func(x1_n, x1_0, x2_n, x2_0)

    x1_0 = x1_n
    x2_0 = x2_n
    iteracion_n += 1

    print("error -> ", error)
    print("x1 -> ", x1_n)
    print("x2 -> ", x2_n)

print("Iteraciones -> ", iteracion_n)

