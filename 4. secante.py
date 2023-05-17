# Usar el método de la secante para aproximar la raíz de f(x) = x^3 + x + 16 = 0, iniciando con x_0 = -3, x_1 = -2. Hasta que el error sea menor o igual a e=0.005 (0.5%)
# 1. Igualar f(x) = 0
# 2. Despejar para g(x), x = g(x)
# 3. Derivar g(x). Evaluar g(x_0) y calcular error.
# 4. Iterar hasta que el error se acerque a 0.01.

from  math import cos, sin, exp, sqrt

x_0 = -3 # xi-1
x_i = -2
error = 1
target_error = 0.005
iteracion_n = 0

def func(x):
    return (x**3)+ x + 16 # x^3 + x + 16

def secante_func(x_0, x_i, fx_0, fx_i):
    r1 = x_0-x_i
    r2 = fx_0-fx_i
    m = fx_i*r1
    return x_i-(m/r2)

def printError(error):
    error = str(round(error*100, 5))
    return error+"%"

while(error > target_error):
    fx_0 = func(x_0)
    fx_i = func(x_i)
    x_2 = secante_func(x_0, x_i, fx_0, fx_i)
    error = abs((x_i - x_0)/x_i)

    x_0 = x_i
    x_i = x_2
    iteracion_n += 1
    
print("x_2_final: ", x_2)
print("Iteraciones: ", iteracion_n)
print("Error: ", printError(error))