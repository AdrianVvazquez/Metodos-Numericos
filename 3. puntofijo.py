# Aplicar el método del punto fijo para establecer una aproximación de la raíz de 2e^(x^2) - 5x, con un valor de x_0 = 0, y un error de e = 0.01
# 1. Igualar f(x) = 0
# 2. Despejar para g(x), x = g(x)
# 3. Derivar g(x). Evaluar g(x_0) y calcular error.
# 4. Iterar hasta que el error se acerque a 0.01.

from  math import cos, sin, exp, sqrt

x_0 = 0
error = 1
target_error = 0.01
iteracion_n = 0

def func(x):
    return (2/5)*exp(x**2) # 0.4e^(x^2)

while(error > target_error):
    x_i = func(x_0)
    print("x_i_actual: ", x_i)
    error = abs((x_i - x_0)/x_i)

    x_0 = x_i
    iteracion_n += 1
    
print("x_i_final: ", x_i)
print("Iteraciones: ", iteracion_n)
print("Error: ", error)