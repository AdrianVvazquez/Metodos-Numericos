from sklearn.datasets import load_boston
import matplotlib.pyplot as plt
import numpy as np

boston = load_boston()
# print(boston)

# (data, target) : tuple if ``return_X_y`` is True
#     A tuple of two ndarrays. The first contains a 2D array of shape (506, 13)
#     with each row representing one sample and each column representing the features.
#     The second array of shape (506,) contains the target samples.
# print(boston.DESCR)
x = boston.data[:,5] # Todas las filas, columna 5
y = boston.target

plt.scatter(x, y, alpha=0.3) # Graficar puntos
# plt.show()

x = np.array([np.ones(x.shape[0]), x]).T
print(x)

bias = np.linalg.inv(x.T @ x) @ x.T @ y 
# print(bias) 

x_axis = [4, 9] # Rango en x
y_axis = [bias[0] + bias[1] * x_axis[0], bias[0] + bias[1] * x_axis[1]] # Obtener los dos extremos de la línea recta
plt.plot(x_axis, y_axis, c="red") # Línea recta
plt.show()