import numpy as np

print("#21")
rows = np.tile([0, 1], 4), np.tile([1, 0], 4)
m1 = np.tile(np.stack(rows), (4, 1))
print(m1)

# print("#22")
# m2 = np.random.random_sample((5, 5))
# m2_mean = np.mean(m2)
# m2_var  = np.var(m2)
# m2_norm = (m2 - m2_mean) / np.sqrt(m2_var)
# print(m2_norm)

print("#23")
rgba = np.dtype(
    [ ('R', 'u1')
    , ('G', 'u1')
    , ('B', 'u1')
    , ('A', 'u1')
    ])
print(type(rgba))

print("#24")
m3 = np.array(
    [ [5, 3, 7, 6, 2]
    , [6, 2, 4, 7, 4]
    , [8, 1, 3, 9, 4]
    ])
m4 = np.array(
    [ [3, 2, 7]
    , [1, 3, 8]
    ])
m5 = m4 @ m3 # np.matmul(m4, m3)
print(m5)

print("#25")
a1 = np.arange(11)
# a1 = (lambda x: -x if 3 <= x < 8 else x)(a1)
# a1 = np.vectorize(lambda x: -x if 3 <= x <= 8 else x)(a1)
# for i in range(len(a1)):
#     if a1[i] >= 3 and a1[i] < 8:
#         a1[i] = -a1[i]
cond = (a1 >= 3) & (a1 <= 8)
a1[cond] = -a1[cond]
print(a1)

print("#26")
print(   sum(range(5), -1)) # 9
print(np.sum(range(5), -1)) # 10

print("#27")
Z = np.array(range(10))
print\
    ( Z ** Z
    , 2 << Z >> 2
    , Z < -Z
    , 1j * Z
    , Z / 1 / 1
#   , Z < Z > Z
    , sep="\n"
    )

print("#28")
print\
    ( np.array(0) /  np.array(0)
    , np.array(0) // np.array(0)
    , np.array([np.nan]).astype(int).astype(float)
    , sep="\n"
    )

print("#29")
a2 = np.array([0.3, 1.5, 2.7])
a2 = np.ceil(a2)
print(a2)

print("#30")
a3 = np.array([1, 3, 4, 5])
a4 = np.array([3, 2, 6, 4])
a5 = np.intersect1d(a3, a4)
print(a5)
