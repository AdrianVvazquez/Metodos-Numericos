xs = [0, 0.5, 1]
h = 0.1
derivada_izq = 0
derivada_der = 0
derivada_medio = 0
promedio = 0

def func(x):
  return x**2
  # return x**4 + 3*x**3 + 2*x**2 + x + 10
  
def func_derivada_der(x, h):
  return (func(h+x)-func(x)) / h

def func_derivada_izq(x, h):
  return (func(x) - func(x-h)) / h

def func_derivada_medio(x, h):
  return (func(x+h) - func(x-h)) / (2*h)

for i in xs:
  promedio = (func_derivada_der(i, h) + func_derivada_izq(i, h) + func_derivada_medio(i, h))/3
  print(promedio)