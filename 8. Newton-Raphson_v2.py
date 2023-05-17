from  math import cos, sin, exp, sqrt
import numpy as np


def adjunta_func(x_0): 
    x = x_0[0][0]
    y = x_0[1][0]

    e = exp(-(x*y))
    
    m_adj = np.array([
        [8+(x*e), -3*(y**2)],
        [-1-(y*e), 7]
    ])
    # m_adj = np.array([
    #     [1, -2*y],
    #     [2*x, 2*x]
    # ])

    det = 1 / (56 + 7*(x*e) - 3*(y**2) + 3*((y**3)*e)) # |A|
    # det = 1/(2*x + 4*x*y) 
    
    return np.dot(det, m_adj) # [|A|]^-1

def newt_raph_func(x_0, adj, fx):
    op = np.matmul(adj, fx)

    return x_0-op
    
def error_func(x_n, x_0):
    x1_0 = x_0[0][0]
    x2_0 = x_0[1][0]
    x1_n = x_n[0][0]
    x2_n = x_n[1][0]
    
    error_tmp1 = abs((x1_n - x1_0) / x1_n)**2
    error_tmp2 = abs((x2_n - x2_0) / x2_n)**2
    
    return sqrt(error_tmp1 + error_tmp2)

def printError(error):
    error = str(round(error*100, 5))
    return error+"%"

x_0 = np.array([
    [1],
    [1]
])
error = 1
target_error = 0.0001 # 1%
iteracion_n = 0

while(error > target_error):
    fx = np.array([
        [7*x_0[0][0] + x_0[1][0]**3-12],
        [x_0[0][0] + 8*x_0[1][0] - exp(-(x_0[0][0]*x_0[1][0]))-12]
    ])
    # fx = np.array([
    #     [x_0[1][0]**2 + x_0[0][0]**2 - 1],
    #     [x_0[1][0] - x_0[0][0]**2]
    # ])

    adj = adjunta_func(x_0) # 2x2
    x_n = newt_raph_func(x_0, adj, fx) # 1x2

    error = error_func(x_n, x_0)
    # print(error)
    x_0 = x_n
    iteracion_n += 1
    print("Iteración #: ", iteracion_n)
    print(x_n)
    print("Error: ", printError(error))
    
print("\nx_final: ->\n", x_n)
print("Iteraciones: ", iteracion_n)
print("Error: ", printError(error))