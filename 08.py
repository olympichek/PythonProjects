import numpy as np
import matplotlib.pyplot as plt

A = 3
T = 1
length = 100
step = 0.05

x = np.arange(0, length, step)
signal = A * np.sin(2 * np.pi * T * x)

N = int(length / step)

rng = np.random.default_rng()
# noise = (rng.random(N) - 0.5) * 2*A
noise = rng.uniform(-A, A, N)

res_signal = signal + noise

plt.plot(x, res_signal)
plt.show()

def get_a(n):
    sum = 0
    for k in range(N):
        t = step * k
        sum += res_signal[k] * np.sin(2 * np.pi * n * t / T)
    return (2 / N) * sum

print(f'A1 = { get_a(1) }')
