import math
import numpy as n
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class Point:
    def __init__(self, x, y, z):
        self.l = n.array([x,y,z])
        self.force = n.array([0.0,0.0,0.0])


class Edge:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2


def start(fname):
    with open(fname) as f:
        content = f.readlines()
        edges = parse_points(content)

        points = [Point(1.0,1.0,1.0), Point(3.0,1.0,1.0), Point(1.5, 1.5, 1.0)]
        edges = [Edge(points[0],points[1]), Edge(points[0], points[2]), Edge(points[1], points[2])]

        fig = plt.figure()
        ax = fig.gca(projection='3d')

        for e in edges:
            ax.plot([e.p1.l[0], e.p2.l[0]], [e.p1.l[1], e.p2.l[1]], [e.p1.l[2]+1, e.p2.l[2]+1])

        calc_forces(edges, points)
        apply_forces(points)

        for e in edges:
            ax.plot([e.p1.l[0], e.p2.l[0]], [e.p1.l[1], e.p2.l[1]], [e.p1.l[2], e.p2.l[2]])

        calc_forces(edges, points)
        apply_forces(points)

        for e in edges:
            ax.plot([e.p1.l[0], e.p2.l[0]], [e.p1.l[1], e.p2.l[1]], [e.p1.l[2]+2, e.p2.l[2]+2])

        calc_forces(edges, points)
        apply_forces(points)

        for e in edges:
            ax.plot([e.p1.l[0], e.p2.l[0]], [e.p1.l[1], e.p2.l[1]], [e.p1.l[2]+3, e.p2.l[2]+3])

        plt.show()


def calc_forces(edges, points):
    for p in points:
        for other_p in points:
            if p == other_p:
                continue
            p.force = calc_repulsion(p, other_p)
            print(p.force)
    print('--')

    for e in edges:
        attraction = calc_attraction(e)
        e.p1.force -= attraction
        e.p2.force += attraction
        print(e.p1.force)
        print(e.p2.force)
    print('----')

def apply_forces(points):
    for p in points:
        p.l += (0.2) * p.force

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


def parse_points(lines):
    return [(e.split()[0], e.split()[1]) for e in lines]


if __name__ == '__main__':
    fname = 'data'
    start(fname)
