
def calcular(n):

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (calcular(n-2)+calcular(n-1))

for i in range(0, 11):
    suma = calcular(i)
    print("\nSUMA: ", suma)
