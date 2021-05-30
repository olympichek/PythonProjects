import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

(x, h) = np.linspace(0, 10, 101, retstep=True)
N = 6
x = 0.1*N*x
y = N*np.sin(0.3*x*N) + N

fig = plt.figure(figsize=(100, 100))

def animate(i):
    plt.cla()
    Y = y[0:i + 1]
    X = x[0:i + 1]
    plt.title('Рух матеріальної точки')
    plt.xlim(0, 6.5)
    plt.ylim(0, 13)
    plt.plot(X, Y, c='gray', linestyle='--')
    plt.plot(x[i], y[i], marker='o', markersize=20, c='r')
    plt.text(6, 12, f'Time = { round(i * h, 2) } sec', fontsize=10, ha='right', va='top')
    return fig

anim = FuncAnimation(fig, animate, frames=100, interval=20)
plt.show()
