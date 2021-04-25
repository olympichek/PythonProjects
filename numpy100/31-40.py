import numpy as np

# 31
# np.seterr(all="ignore")

print("#32")
print(np.sqrt(-1) == np.emath.sqrt(-1))

print("#33")
today     = np.datetime64('today', 'D')
daydiff   = np.timedelta64(1, 'D')
yesterday = today - daydiff
tomorrow  = today + daydiff
print\
    ( yesterday
    , today
    , tomorrow
    , sep="\n"
    )

print("#34")
dates = np.arange('2016-07', '2016-08', dtype='datetime64[D]')
print(dates)

print("#35")
A = np.ones(3) * 1
B = np.ones(3) * 2
np.add(A, B, out=B)
np.divide(A, 2, out=A)
np.negative(A, out=A)
np.multiply(A, B, out=A)
print(A)

print("#36")
a1 = np.random.uniform(-10, +10, 10)
a2 = np.trunc(a1)
# a2 = a1.astype(np.int32)
print(a1, a2, sep="\n")

print("#37")
m1  = np.zeros((5, 5))
m1 += np.arange(5)
print(m1)

print("#38")
def generator():
    for i in range(10):
        yield i
a3 = np.fromiter(generator(), dtype=np.float32)
print(a3)

print("#39")
a4 = np.linspace(start=0, stop=1, num=10, endpoint=False)
print(a4)

print("#40")
a5 = np.random.random_sample(10)
a5.sort()
print(a5)
