# 01
import numpy as np
import sys

print("#02")
print(np.version.version)
# np.show_config()

print("#03")
a1 = np.empty(10)
print(a1)

print("#04")
print(sys.getsizeof(a1))

# help(np.add)

print("#06")
a2 = np.ones(10)
print(a2)

print("#07")
# a3 = np.array(range(10, 50))
a3 = np.arange(10, 50)
print(a3)

print("#08")
a4 = np.flip(a3)
print(a4)

print("#09")
m1 = np.arange(0, 9).reshape((3, 3))
print(m1)

print("#10")
a5 = np.array([1, 2, 0, 0, 4, 0]).nonzero()[0]
print(a5)
