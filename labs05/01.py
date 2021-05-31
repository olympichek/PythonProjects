import numpy as np
import sympy as sym
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

k = 0.3
l = 1580
tf = 0.5

t = sym.symbols('t')

x = sym.Function('x')
x1 = sym.Derivative(x(t), t)
x2 = sym.Derivative(x(t), t, t)
eq_x = sym.Eq(x2 + k*x1, 0)

y = sym.Function('y')
y1 = sym.Derivative(y(t), t)
y2 = sym.Derivative(y(t), t, t)
eq_y = sym.Eq(y2 + k*y1, -9.8)

x_fun = sym.dsolve(eq_x, x(t), ics={ x(0): 0, x(tf): l }).rhs
y_fun = sym.dsolve(eq_y, y(t), ics={ y(0): 0, y(tf): 0 }).rhs

v_x = sym.diff(x_fun, t)
v_y = sym.diff(y_fun, t)

v_x_0 = v_x.subs(t, 0)
v_y_0 = v_y.subs(t, 0)
v_0 = sym.sqrt(v_x_0**2 + v_y_0**2)
alpha_0 = sym.atan(v_y_0/v_x_0)

print(f'v0 = { v_0 }')
print(f'alpha = { alpha_0 }')

t_range = np.arange(0.0, tf + 0.01, 0.01)
x_range = np.array([float(x_fun.subs(t, t_i)) for t_i in t_range])
y_range = np.array([float(y_fun.subs(t, t_i)) for t_i in t_range])

fig = plt.figure()

def animate(i):
    plt.cla()
    x_range_i = x_range[0:i + 1]
    y_range_i = y_range[0:i + 1]
    x_i = x_range[i]
    y_i = y_range[i]
    h = 0.01
    plt.title('Рух тіла')
    plt.xlim(0, 1600)
    plt.ylim(0, 0.32)
    plt.plot(x_range_i, y_range_i)
    plt.plot(x_i, y_i, 'ro')
    plt.xlabel('x')
    plt.ylabel('y')
    v_x_i = float(v_x.subs(t, i*h))
    v_y_i = float(v_y.subs(t, i*h))
    v_i = sym.sqrt(v_x_i**2 + v_y_i**2)
    alpha_i = sym.atan(v_y_i/v_x_i)
    label = '\n'.join(
        [ f't = { round(i*h, 2) }'
        , f'x = { round(x_i, 0) }'
        , f'y = { round(y_i, 2) }'
        , f'v = { round(v_i, 2) }'
        , f'$\\alpha$ = { round(alpha_i, 5) }'
        ])
    plt.text(1500, 0.3, label, ha='right', va='top')
    return fig

anim = FuncAnimation(fig, animate, frames=51, interval=10)
anim.save('01.gif', writer='pillow')
plt.show()

# plt.plot(x_range, y_range)
# plt.show()
