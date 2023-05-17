import numpy as np
import matplotlib.pyplot as plt
valores = []
def f(x):
    return (np.log(x**2)-0.7)*np.cos(x)

def media(a, b):
    return (a+b)/2

def bis(a, b, x0):
    print(a, b, x0)
    if f(a)*f(x0) < 0:
        b = x0
    else:
        a = x0
    
    valores.append([a, b])
    x1 = media(a, b)
    err = abs((x1 - x0)/x1)
    if err < 0.0005:
        print("err:", err)
    else:
        bis(a, b, x1)

a = 1
b = 3
x0 = media(a, b)

bis(a, b, x0)


