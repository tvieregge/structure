import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = plt.axes(xlim=(0,5), ylim=(0,5))
# for e in edges:
line, = ax.plot([],[], lw=2)


def init():
    line.set_data([], [])
    return line,

def animate(i):
    # x = np.linspace(0, 2, 1000)
    # y = np.sin(2 * np.pi * (x - 0.01 * i))
    # line.set_data(x, y)
    # return line,
    # line.set_data([g_edges[0].p1.l[0], g_edges[0].p2.l[0]], [g_edges[0].p1.l[1], g_edges[0].p2.l[1]])
    print('Tick')
    line.set_data([1,2],[1,3])
    return line,

if __name__ == '__main__':
    anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=5, interval=1000, blit=False)
    plt.show()
