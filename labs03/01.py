import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 100)

N = 2

functions = \
    [ np.sin(x + N)
    , np.cos(3 * x - N)
    , 0.4 * np.exp(-N * x)
    , 0.3 * (x + N / 10) ** 3
    ]

labels = \
    [ "y = sin(x + N)"
    , "y = cos(3x - N)"
    , "y = 0.4exp(-N * x)"
    , "y = 0.3(x + N/10)^3"
    ]

# а)
for function, label in zip(functions, labels):
    plt.plot(x, function, label=label)

plt.ylim(-5 , 5)
plt.legend()

plt.savefig("01 а)")
plt.show()

# б)
for function, label, i in\
zip(functions, labels, range(len(functions))):
    plt.plot(x, function, "C" + str(i), label=label)
    plt.legend()
    plt.savefig("01 б) " + str(i + 1))
    plt.show()

# в)
fig, axs = plt.subplots(2, 2)

for ax, function, label, i in\
zip(axs.flat, functions, labels, range(len(functions))):
    ax.set_title(label)
    ax.plot(x, function, "C" + str(i))

fig.tight_layout()

fig.savefig("01 в)")
plt.show()
