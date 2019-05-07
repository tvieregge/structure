import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D

FORCE_CONST = 0.05

class Point:
    def __init__(self, x, y, z):
        self.l = np.array([x,y,z])
        self.force = np.array([0.0,0.0,0.0])


class Edge:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

g_points = [Point(1.0,1.0,1.0), Point(3.0,1.0,1.0), Point(1.5, 1.5, 1.0)]
g_edges = [Edge(g_points[0],g_points[1]), Edge(g_points[0], g_points[2]), Edge(g_points[1], g_points[2])]
# g_points = [Point(10.0,10.0,10.0), Point(30.0,10.0,10.0)]
# g_edges = [Edge(g_points[0],g_points[1])]

fig = plt.figure()
ax = Axes3D(fig, xlim=(0,3), ylim=(0,3), zlim=(0,3))
# lines = sum([ax.plot([], [], [], '-', c=c) for c in colors], [])
lines = sum([ax.plot([],[],[], lw=2) for e in g_edges], [])
print(lines)


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


# def start(fname):
#     with open(fname) as f:
#         content = f.readlines()
#         edges = parse_points(content)

#         points = [Point(1.0,1.0,1.0), Point(3.0,1.0,1.0), Point(1.5, 1.5, 1.0)]
#         edges = [Edge(points[0],points[1]), Edge(points[0], points[2]), Edge(points[1], points[2])]

#         fig = plt.figure()
#         ax = fig.gca(projection='3d')

#         for e in edges:
#             ax.plot([e.p1.l[0], e.p2.l[0]], [e.p1.l[1], e.p2.l[1]], [e.p1.l[2]+1, e.p2.l[2]+1])

#         calc_forces(edges, points)
#         apply_forces(points)

#         for e in edges:
#             ax.plot([e.p1.l[0], e.p2.l[0]], [e.p1.l[1], e.p2.l[1]], [e.p1.l[2], e.p2.l[2]])

#         calc_forces(edges, points)
#         apply_forces(points)

#         for e in edges:
#             ax.plot([e.p1.l[0], e.p2.l[0]], [e.p1.l[1], e.p2.l[1]], [e.p1.l[2]+2, e.p2.l[2]+2])

#         calc_forces(edges, points)
#         apply_forces(points)

#         for e in edges:
#             ax.plot([e.p1.l[0], e.p2.l[0]], [e.p1.l[1], e.p2.l[1]], [e.p1.l[2]+3, e.p2.l[2]+3])

#         plt.show()


def calc_forces(edges, points):
    for p in points:
        for other_p in points:
            if p == other_p:
                continue
            p.force = calc_repulsion(p, other_p)

    for e in edges:
        attraction = calc_attraction(e)
        e.p1.force -= attraction
        e.p2.force += attraction


def apply_forces(points):
    print('----')
    for p in points:
        print(p.l)
        print(p.force)
        print('**')
        p.l += FORCE_CONST * p.force
        print(p.l)
        print('****')


def calc_dist(p1, p2):
    diff = p1.l - p2.l
    return (diff**2).sum()**0.5


def calc_repulsion(p1, p2):
    dist = calc_dist(p1, p2)
    unit = ((p1.l-p2.l)/dist)
    return  unit/(dist**2)


def calc_attraction(edge):
    p1 = edge.p1
    p2 = edge.p2
    dist = calc_dist(p1, p2)
    unit = ((p1.l-p2.l)/dist)
    return dist * unit


# def parse_points(lines):
#     return [(e.split()[0], e.split()[1]) for e in lines]


if __name__ == '__main__':
    anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=5, interval=500, blit=False)
    plt.show()
