import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-5, 5.1, 0.1)

fig, a = plt.subplots()

plt.plot(np.sin(x), label="y = sin(x)")
# plt.plot(np.exp(x))
# plt.plot(x ** 2)

plt.legend()
plt.show()

fig.savefig("sin(x)")
