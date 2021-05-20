import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig = plt.figure(figsize=(12, 10))

N = 2
x = y = np.linspace(-5, 5, 101)
x1, y1 = np.meshgrid(x, y)

def Function3d(t):
    return 0.2 * N * np.cos(x1*x1 + y1*y1 + t)

zcont = [-1.5 + 0.3*i for i in range(11)]

def Animate(i):
    plt.gcf().clear()
    plt.title('Анімація')
    plt.xlabel('x')
    plt.ylabel('y')
    h = 0.1
    z = Function3d(i * h)
    plt.contourf(x, y, z, zcont)
    plt.colorbar()
    plt.text\
        ( 4.5
        , 4.5
        , f'Time = { round(i * h, 2) } sec'
        , fontsize=16
        , ha='right'
        , va='top'
        )
    return fig

anim = FuncAnimation(fig, Animate, frames=100, interval=1)
anim.save('03 а).gif', writer='pillow')
