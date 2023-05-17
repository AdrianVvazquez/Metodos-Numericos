#CODIGO METODO DE FALSA POSICION
# from distutils.log import error
from math import exp

error = 1
target_error = 0.01
x0 = 0
num = 1

def funcion(x):
    return(0.4* exp(x**2))

while(error > target_error):
    x1 = funcion(x0)
    error = abs((x1-x0)/x1)

    print("iteración: ",num,"error:",error*100,"%"," con una x de: ", x1)
    
    x0=x1
    num=num+1
