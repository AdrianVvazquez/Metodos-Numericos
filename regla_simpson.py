
R = 1/3
xs_list = []
fxs_list = []
a = 0
b = 0
n = 0
suma_1 = 0
suma_2 = 0

def fnc(x):
  return x**2

def fnc_h(a, b, n):
  return (b-a)/n

def fnc_xi(a, i, h):
  return a+(i*h)


a = int(input("Ingresa un valor para a: "))
b = int(input("Ingresa un valor para b: "))
n = int(input("Ingresa un valor para n: "))
h = fnc_h(a, b, n)

for i in range(n+1):
  xs_list.append(fnc_xi(a, i, h))

for i in xs_list:
  fxs_list.append(fnc(i))
  
for i in range(1, n, 2):
  suma_1 += fxs_list[i]

for i in range(2, n, 2):
  suma_2 += fxs_list[i]

A = (b-a)*( (fxs_list[0] + (4*suma_1)+(2*suma_2) + fxs_list[n]) / (3*n) )
print("Resultado de la integral de la función en los límites definidos entre",a,"y",b)
print(A)