
import numpy as np


f1 = x**2 + x + 1
x0 = 5
h = 1

print("==================================")
print("Diferencia central")
print(f1)
print("==================================")

while h > 0.05:
    dval = (f1.subs(x,x0+h) - f1.subs(x,x0-h))/(2*h)
    dval = float(dval)
    print(f"h =  {h:.4f} ; ~diff(f,5) = {dval:.4f}")
    h = h / 2
