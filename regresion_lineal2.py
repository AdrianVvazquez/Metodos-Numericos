# Buscar la regresión lineal de las muertes por exposición 
# ambiental al calor y al frío en México.

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = np.genfromtxt("data/cause_of_deaths.csv",delimiter=",")
# data = pd.read_csv("cause_of_deaths.csv")

x = data[:,0] # año
y = data[:,1] # núm. muertes
x_2 = data[:15,2]
y_2 = data[:15,3]
# print(x)
# print(y)

plt.scatter(x, y, alpha=0.3)

x = np.array([np.ones(x.shape[0]), x]).T
bias = np.linalg.inv(x.T @ x) @ x.T @ y

x_axis = [1990, 2020] # Rango en x
y_axis = [bias[0] + bias[1] * x_axis[0], bias[0] + bias[1] * x_axis[1]] # Obtener los dos extremos de la línea recta

plt.plot(x_axis, y_axis, c="blue") # Línea recta
plt.title("Muertes en México por exposición ambiental al calor y frío. [1990 - 2020]")
plt.show()

plt.scatter(x_2, y_2, alpha=0.3)

x_2 = np.array([np.ones(x_2.shape[0]), x_2]).T
bias_2 = np.linalg.inv(x_2.T @ x_2) @ x_2.T @ y_2

x_axis_2 = [2005, 2020] # Rango en x
y_axis_2 = [bias_2[0] + bias_2[1] * x_axis_2[0], bias_2[0] + bias_2[1] * x_axis_2[1]] # Obtener los dos extremos de la línea recta

plt.plot(x_axis_2, y_axis_2, c="red") # Línea recta
plt.title("Muertes en México por exposición ambiental al calor y frío. [2005 - 2020]")
plt.show()