import numpy as np

A = np.array(
    [ [4,    2, -3]
    , [0.5, -2,  0]
    ])

B = np.array([1, 11, 0])

print(np.linalg.solve(A, B))
