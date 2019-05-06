import numpy
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class Edge:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2


def start(fname):
    with open(fname) as f:
        content = f.readlines()
        edges = parse_points(content)

        points = [Point(1,1,1), Point(3,3,1)]
        edges = [Edge(points[0],points[1])]

        fig = plt.figure()
        ax = fig.gca(projection='3d')

        for e in edges:
            ax.plot([e.p1.x, e.p2.x], [e.p1.y, e.p2.y], [e.p1.z, e.p2.z])

        plt.show()


def calc_dist(p1, p2):
    return math.hypot(p1.x - p2.x, p1.y - p2.y)


def calc_repulsion(p1, p2):
    return 1/(calc_dist(p1, p2)**2)


def calc_attration(edge):
    return calc_dist(edge.p1, edge.p2)


def parse_points(lines):
    return [(e.split()[0], e.split()[1]) for e in lines]


if __name__ == '__main__':
    fname = 'data'
    start(fname)
