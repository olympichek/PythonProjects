import numpy as np

N = 2

A = np.array(
    [ [1 - N,   4,   2 + N]
    , [  0,    -N,     1  ]
    , [  1,     3,   4 + N]
    ])
B = np.array(
    [ [  N,   N + 1, N + 2]
    , [N + 3, N + 4, N + 5]
    , [N + 6, N + 7, N + 8]
    ])
C = np.array(
    [ [  N,     N,     N  ]
    , [  N,     N,     N  ]
    , [  N,     N,   N - 3]
    ])

print(A, B, C, sep="\n")

print("а)")
A1 = A + 5
print(A1)

print("б)")
B1 = B * 2
print(B1)

print("в)")
C1 = np.copy(C)
d = np.diag_indices(3)
C1[d] = C1[d] + 3
print(C1)

print("г)")
M1 = 2 * A + 3 * B @ C
print(M1)

print("д)")
M2 = A.T @ A - 8 * B
print(M2)

print("е)")
A_, B_, C_ = A.tolist(), B.tolist(), C.tolist()

def transpose(matrix):
    n = len(matrix)
    m = len(matrix[0])
    matrix_ = [[0] * n for i in range(m)]
#   matrix_ = [[0] * n] * m
    for i in range(n):
        for j in range(m):
            matrix_[j][i] = matrix[i][j]
    return matrix_

def multn(x, matrix):
    return [
        [a * x for a in row]
        for row in matrix
    ]

def subtract(matrix1, matrix2):
    if len(matrix1) != len(matrix2)\
    or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Sizes don't match!")
    return [
        [a1 - a2 for a1, a2 in zip(row1, row2)]
        for row1, row2 in zip(matrix1, matrix2)
    ]

def matmul(matrix1, matrix2):
    n1, m1 = len(matrix1), len(matrix1[0])
    n2, m2 = len(matrix2), len(matrix2[0])
    if(m1 != n2):
        raise ValueError("Sizes don't match!")
    matrix3 = [[0] * m2 for i in range(n1)]
    for i in range(n1):
        for j in range(m2):
            matrix3[i][j] = sum([
                matrix1[i][k] * matrix2[k][j]
                for k in range(m1)
            ])
    return matrix3

M2_ = subtract(matmul(transpose(A_), A_), multn(8, B_))
print(M2_)

print("э)")
d1 = np.linalg.det(A)
d2 = np.linalg.det(B)
d3 = np.linalg.det(C)
print(d1, d2, d3, sep="\n")
