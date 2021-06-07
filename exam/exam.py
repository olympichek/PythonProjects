import numpy as np
import matplotlib.pyplot as plt

# Створити матрицю 7*7, у якої по головній діагоналі міститься номер рядка у
# квадраті, по діагоналі на 3 справа від головної – номер поточного рядка починаючи з
# 1, по діагоналі на 1 зліва від головної – сума номерів рядка та стовпця, інші елементи
# – нулі.

size = 7
M1 = np.zeros((size, size))

d1 = np.diag_indices(size)
M1[d1] = np.arange(1, size + 1) ** 2

k1 = 3
d2 = np.diag_indices(size - k1)
d2 = d2[0], d2[1] + k1
M1[d2] = np.arange(1, size - k1 + 1)

k2 = 1
d3 = np.diag_indices(size - k2)
d3 = d3[0] + k2, d3[1]
rows = np.arange(k2 + 1, size + 1)
cols = np.arange(1, size - k2 + 1)
M1[d3] = rows + cols

# До кожного елемента п’ятого рядка додати 2. Транспонувати матрицю та
# помножити вихідну на транспоновану. Результат кожного кроку вивести на екран
# через print() та візуалізувати за на сітці у градаціях сірого.
k3 = 5
M2 = M1.copy()
M2[k3 - 1] += 2
M3 = M2.T
M4 = M2 @ M3 # np.matmul(M2, M3)

print(M1, M2, M3, M4, sep='\n\n')

plt.rcParams['image.cmap'] = 'binary'
fig, axs = plt.subplots(2, 2)

MS = [M1, M2, M3, M4]
r1 = range(0, 7)
r2 = range(1, 8)
for i, (ax, M) in enumerate(zip((axs.flat), MS)):
    ax.set_title(f'#{ i }')
    ax.set_xticks(r1)
    ax.set_xticklabels(r2)
    ax.set_yticks(r1)
    ax.set_yticklabels(r2)
    ax.matshow(M)

fig.tight_layout()
plt.savefig('plot.png')
plt.show()
