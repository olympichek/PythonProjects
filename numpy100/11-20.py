import numpy as np

print("#11")
m1 = np.identity(3)
print(m1)

rng = np.random.default_rng()

print("#12")
t1 = rng.integers(low=0, high=10, size=(3, 3, 3))
print(t1)

print("#13")
m2 = rng.integers(low=0, high=500, size=(10, 10))
print(m2)
print(m2.max(), m2.min())

print("#14")
a1 = rng.integers(low=0, high=100, size=30)
print(a1)
print(a1.mean())

print("#15")
a2 = np.ones((5, 5))
a2[1:-1, 1:-1] = 0
print(a2)

print("#16")
a3 = np.pad\
    ( np.ones((5, 5))
    , pad_width=1
    , mode='constant'
    , constant_values=0
    )
print(a3)

print("#17")
print\
    ( 0 * np.nan
    , np.nan == np.nan
    , np.inf > np.nan
    , np.nan - np.nan
    , np.nan in set([np.nan])
    , 0.3 == 3 * 0.1
    )

print("#18")
m3 = np.diag([1, 2, 3, 4], -1)
print(m3)

print("#19")
m4 = np.zeros((8, 8))
m4[1::2, 0::2] = 1
m4[0::2, 1::2] = 1
print(m4)

print("#20")
i = np.unravel_index(100, (6, 7, 8))
print(i)
