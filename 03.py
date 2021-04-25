import numpy as np

A = np.array(
    [ [2, -1, 4, 5]
    , [3,  1, 2, 4]
    ])

B = np.array(
    [ [1,  4,  5]
    , [2,  3,  4]
    , [5,  6, -1]
    , [2, -1,  3]
    ])

C = np.array(
    [ [1, 2, 3]
    , [4, 5, 4]
    ])

X  = np.matmul(A, B)
X_ = A @ B
print(X_)

# Y = np.matmul(A, C)
# print(Y)
