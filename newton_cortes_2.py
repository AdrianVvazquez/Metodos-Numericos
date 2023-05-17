# xs = [0, 0.5, 1]
x_0 = 5
h = 3
derivada_izq = 0
derivada_der = 0
derivada_medio = 0
promedio = 0

def func(x):
#   return x**2
  return x**2 + x + 1
  
def func_derivada_der(x, h):
  return (func(h+x)-func(x)) / h

def func_derivada_izq(x, h):
  return (func(x) - func(x-h)) / h

def func_derivada_medio(x, h):
  return (func(x+h) - func(x-h)) / (2*h)

promedio = (func_derivada_der(x_0, h) + func_derivada_izq(x_0, h) + func_derivada_medio(x_0, h))/3
 
print("\nx_0 =", x_0)
print("h =", h)
print("\nDerecha =", func_derivada_der(x_0, h))
print("Izquierda =", func_derivada_izq(x_0, h))
print("Central =", func_derivada_medio(x_0, h))
print("Derivada =", promedio)
print("\n")
