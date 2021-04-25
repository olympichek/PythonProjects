import numpy as np

A = np.array(
    [ [1,  2,  3, 4]
    , [2, -2, -4, 5]
    ])

B = np.array(
    [ [ 1, -1, 1, 2]
    , [-2,  3, 5, 6]
    ])

C = 3*A - 4*B
print(C)
print(np.sum(C))
