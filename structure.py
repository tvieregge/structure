import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D

class Point:
    def __init__(self, x, y, z):
        self.l = np.array([x,y,z])
        self.force = np.array([0.0,0.0,0.0])


class Edge:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

fig = plt.figure()
ax = Axes3D(fig, xlim=(0,5), ylim=(0,5), zlim=(0,5))
line, = ax.plot([1,2],[3,4], lw=2)

g_points = [Point(1.0,1.0,1.0), Point(3.0,1.0,1.0), Point(1.5, 1.5, 1.0)]
g_edges = [Edge(g_points[0],g_points[1]), Edge(g_points[0], g_points[2]), Edge(g_points[1], g_points[2])]


def init():
    line.set_data([1,2], [3,4])
    return line,

def animate(i):
    print('Tick')
    line.set_data([g_edges[0].p1.l[0], g_edges[0].p2.l[0]], [g_edges[0].p1.l[1], g_edges[0].p2.l[1]])
    line.set_3d_properties([g_edges[0].p1.l[2], g_edges[0].p2.l[2]])
    return line,

if __name__ == '__main__':
    anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=5, interval=1000, blit=False)
    plt.show()
