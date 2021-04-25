import numpy as np
import time
import sys

print("#41")
a1 = np.arange(1000001)

def sum_with_function(sum_function):
    begin_time = time.time()
    sum = sum_function(a1)
    end_time = time.time()
    time_diff = 1000 * (end_time - begin_time)
    print("sum:", sum)
    print("time:", time_diff)

sum_with_function(sum)
sum_with_function(np.sum)
sum_with_function(np.add.reduce)

print("#42")

a2 = np.arange(10)
a3 = np.arange(10)
check = np.array_equal(a2, a3)
print(check)

a2 = np.random.random_sample()
a3 = np.random.random_sample()
check = np.array_equal(a2, a3)
print(check)

print("#43")
a4 = np.zeros(10)
a4.flags.writeable = False
try:
    a4[0] = 1
except ValueError as e:
    print("Error:", e)

print("#44")
m1 = np.random.random_sample((10, 2))
x, y = m1[:, 0], m1[:, 1]
r = np.sqrt(x ** 2 + x ** 2)
t = np.arctan2(y, x)
print(x, y, "", r, t, sep="\n")

print("#45")
a5 = np.random.random_sample(10)
print(a5)
# a5[a5 == np.max(a5)] = 0
a5[a5.argmax()] = 0
print(a5)

print("#46")
m2 = np.zeros((5, 5), [('x', float), ('y', float)])
m2['x'], m2['y'] = np.meshgrid\
    ( np.linspace(0, 1, 5)
    , np.linspace(0, 1, 5)
    )
print(m2)

print("#47")
X = np.random.random((5, 5))
Y = np.random.random((5, 5))
C = 1 / (X - Y)
print(C)
print(np.linalg.det(C))

print("#48")
for dtype in [np.int8, np.int32, np.int64]:
    inf = np.iinfo(dtype)
    print(inf.min, inf.max)
for dtype in [np.float32, np.float64]:
    inf = np.finfo(dtype)
    print(inf.min, inf.max, inf.eps)

print("#49")
np.set_printoptions(threshold=sys.maxsize)
a6 = np.random.randint(1, 10, (10, 10))
print(a6)

print("#50")
v = 52.356
a7 = np.arange(100)
i = np.abs(a7 - v).argmin()
print(a7[i])
