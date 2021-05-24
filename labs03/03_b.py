import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import mpl_toolkits.mplot3d.axes3d as p3

fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(projection='3d')

N = 2
x = y = np.linspace(-5, 5, 101)
x1, y1 = np.meshgrid(x, y)

def Function3d(t):
    return 0.2 * N * np.cos(x1*x1 + y1*y1 + t)

zcont = [-1.5 + 0.3*i for i in range(11)]

plt.title('Анімація')
plt.xlabel('x')
plt.ylabel('y')

def Animate(i):
    # plt.gcf().clear()
    h = 0.1
    z = Function3d(i * h)
    ax.plot_surface(x1, y1, z)
    return fig

anim = FuncAnimation(fig, Animate, frames=100, interval=1)
anim.save('03 б).gif', writer='pillow')
