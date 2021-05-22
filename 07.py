import matplotlib.pyplot as plt
import numpy as np

nx = 21 # кількість клітинок по горизонталі
nt = 50 # кількість точок по часу

u = [None for i in range(nt+1)] # заготовка для збереження (nt+1) станів автомату

u[0] = np.zeros(nx) # створюємо нульовий масив
u[0][round(nx/2)-1] = 1 # середній елемент робимо 1

def rule30(x, i, nx):
    if (i == nx-1) and (x[i-1] * x[i] == 1 or (x[i] == 0) * (x[i-1] == x[0])):
        a = 0
    elif (i != nx-1) and (x[i-1] * x[i] == 1 or (x[i] == 0) * (x[i-1] == x[i+1])):
        a = 0
    else:
        a = 1
    return a

for k in range(nt):
    u[k+1] = np.zeros(nx)
    for i in range(nx):
        u[k+1][i] = rule30(u[k], i, nx)

print(u)

plt.rcParams['image.cmap'] = 'binary'
plt.matshow(u)
plt.axis(False)

plt.show()
