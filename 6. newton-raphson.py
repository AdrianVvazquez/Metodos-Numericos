# Dada la función f(x) = e^(-x)-x, obtener una raíz aproximada con el método de Newton-Raphson, con un valor incial x_0 = , y un error e = 0.01(1%)
# 1. Funcion
# 2. Derivada
# 3. Error
# 4. 

from  math import cos, sin, exp, sqrt

x_0 = 0
error = 1
target_error = 0.01 # 1%
iteracion_n = 0

def func(x):
    return exp(-x) - x # e^-x - x

def derivada_func(x):
    return -exp(-x) - 1 # -e^-x - 1

def newt_raph_func(x_0, fx, fdx):
    return x_0-(fx/fdx)

def printError(error):
    error = str(round(error*100, 5))
    return error+"%"

while(error > target_error):
    fx = func(x_0)
    fdx = derivada_func(x_0)
    x_i = newt_raph_func(x_0, fx, fdx)
    error = abs((x_i - x_0)/x_i)

    x_0 = x_i
    iteracion_n += 1
    
print("x_i_final: ", x_i)
print("Iteraciones: ", iteracion_n)
print("Error: ", printError(error))