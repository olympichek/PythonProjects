import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

N = 2

fig = plt.figure()

t = np.arange(0.0, 10.0, 0.01)
x = 0.1 * N * t
y = N * (1 + np.sin(0.3 * N * t))

plt.plot(x, y)

redDot, = plt.plot([0], [N * (1 + np.sin(0))], 'ro')

plt.title('Рух матеріальної точки')
text = plt.text\
    ( 2.0
    , 4.0
    , f'Time = 0.0 sec'
    , ha='right'
    , va='top'
    )

def animate(i):
    redDot.set_data(0.1 * N * i, N * (1 + np.sin(0.3 * N * i)))
    text.set_text(f'Time = { round(i, 2) } sec')
    return redDot,

frames = np.arange(0.0, 10.0, 0.1)
anim = FuncAnimation(fig, animate, frames=frames, interval=10)
anim.save('02.gif', writer='pillow')
