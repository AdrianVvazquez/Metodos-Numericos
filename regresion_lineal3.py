# Buscar la regresión lineal de los países más felices en relación a
# la libertad que los habitantes tienen para tomar decisiones de vida

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = np.genfromtxt("data/happiest_countries_data.csv",delimiter=",")

x = data[:,1] # puntuación
y = data[:,0] # libertad para tomar decisiones en la vida propia [0 - 1]

plt.scatter(x, y, alpha=0.3)

x = np.array([np.ones(x.shape[0]), x]).T
bias = np.linalg.inv(x.T @ x) @ x.T @ y
print(bias)

x_axis = [0, 1] # Rango en x
y_axis = [bias[0] + bias[1] * x_axis[0], bias[0] + bias[1] * x_axis[1]] # Obtener los dos extremos de la línea recta

plt.plot(x_axis, y_axis, c="red") # Línea recta
plt.title("Puntuación de los paises más felices en relación \na la libertar de sus habitantes para tomar decisiones")
plt.show()

