import numpy as np

size = 10
M = np.zeros((size, size))

d1 = np.diag_indices(size)
M[d1] = np.arange(1, size + 1)

k1 = 2
d2 = np.diag_indices(size - k1)
d2 = d2[0], d2[1] + k1
M[d2] = np.arange(k1 + 1, size + 1)

k2 = 3
d3 = np.diag_indices(size - k2)
d3 = d3[0] + k2, d3[1]
rows = np.arange(k2 + 1, size + 1)
cols = np.arange(1, size - k2 + 1)
M[d3] = rows * cols

print(M)
