import random
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D
from itertools import chain

FORCE_CONST = 0.05

class Point:
    def __init__(self, x, y, z):
        self.l = np.array([x,y,z])
        self.force = np.array([0.0,0.0,0.0])


class Edge:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2


def init():
    for line in lines:
        line.set_data([], [])
        line.set_3d_properties([])
    return lines

def animate(i):
    for p in enumerate(lines):
        edge, line = p
        line.set_data([g_edges[edge].p1.l[0], g_edges[edge].p2.l[0]], [g_edges[edge].p1.l[1], g_edges[edge].p2.l[1]])
        line.set_3d_properties([g_edges[edge].p1.l[2], g_edges[edge].p2.l[2]])

    calc_forces(g_edges, g_points)
    apply_forces(g_points)

    return lines


def calc_forces(edges, points):
    for p in points:
        p.force = np.array([0.0,0.0,0.0])
        for other_p in points:
            if p == other_p:
                continue
            p.force += calc_repulsion(p, other_p)

    for e in edges:
        attraction = 0.5*calc_attraction(e)
        e.p1.force -= attraction
        e.p2.force += attraction


def apply_forces(points):
    # print('----')
    for p in points:
        # print(p.l)
        # print(p.force)
        # print('**')
        p.l += FORCE_CONST * p.force
        # print(p.l)
        # print('****')


def calc_dist(p1, p2):
    diff = p1.l - p2.l
    return (diff**2).sum()**0.5


def calc_repulsion(p1, p2):
    dist = calc_dist(p1, p2)
    unit = ((p1.l-p2.l)/dist)
    return  unit/(dist**1.5)


def calc_attraction(edge):
    p1 = edge.p1
    p2 = edge.p2
    dist = calc_dist(p1, p2)
    unit = ((p1.l-p2.l)/dist)
    return dist * unit


def parse_points(lines):
    return [(int(e.split()[0]), int(e.split()[1])) for e in lines]


if __name__ == '__main__':
    with open('data') as f:
        content = f.readlines()

    # edges = parse_points(content)
    # num_edges = len(edges)
    edges = []
    num_edges = 30
    points_for_edges = random.sample(range(num_edges), num_edges)
    points_for_edges.extend(random.sample(range(num_edges), num_edges))
    points_for_edges.extend(random.sample(range(num_edges), num_edges))
    points_for_edges.extend(random.sample(range(num_edges), num_edges))
    for i in range(len(points_for_edges)//2):
        p1 = points_for_edges.pop()
        p2 = points_for_edges.pop()
        edges.append((p1, p2))

    points = list(set(chain.from_iterable(edges))) # Flatten list of edges and take unique points
    points.sort()

    # print(edges)
    # print(points)
    scale = max(7, num_edges**(1/3)*4)
    g_points = []
    for p in points:
        x = random.uniform(0,scale//2)+scale//4
        y = random.uniform(0,scale//2)+scale//4
        z = random.uniform(0,scale//2)+scale//4
        g_points.append(Point(x,y,z))

    g_edges = []
    for e in edges:
        g_edges.append(Edge(g_points[e[0]], g_points[e[1]]))

    fig = plt.figure()
    ax = Axes3D(fig, xlim=(0, scale), ylim=(0, scale), zlim=(0, scale))
    lines = sum([ax.plot([],[],[], lw=2) for e in g_edges], [])

    anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=150, interval=20, blit=False)
    # anim.save('cube_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'], dpi=200)
    plt.show()
