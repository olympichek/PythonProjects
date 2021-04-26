import numpy as np
import matplotlib.pyplot as plt

# x = np.arange(-5, 5.1, 0.1)
x = np.linspace(-5, 5, 100)


fig, a = plt.subplots()

plt.plot(x, np.sin(x), label="y = sin(x)")

plt.legend()
plt.show()

# fig.savefig("sin(x)")
