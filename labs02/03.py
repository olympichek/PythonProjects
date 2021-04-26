import numpy as np

N = 2

C = np.array(
    [ [  N,   4 - N, -3]
    , [3 - N,  11,   -2]
    , [  0,     8,   -N]
    ])
V = np.array([1, 10 * N, -N])

X = np.linalg.solve(C, V)
print(X)
