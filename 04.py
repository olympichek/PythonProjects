import numpy as np

A = np.array(
    [ [ 2, -4]
    , [ 3,  5]
    , [-1,  0]
    ])

B = np.array(
    [ [ 1,  2, 7]
    , [-3, -4, 0]
    , [ 5,  2, 1]
    ])

C = np.array(
    [ [6, -3, 9]
    , [4, -5, 2]
    , [8,  1, 5]
    ])

D = A.T - 2 * A.T @ B.T
print(D)

print(np.linalg.det(C))
