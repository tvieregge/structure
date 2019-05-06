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

        # points = numpy.array([[1,2,1],[3,3,1],[3,1,1],[1,3,1]])
        # edges = numpy.array([[0,2],[0,3],[1,2],[1,3]])
        points = [Point(1,1,1), Point(3,3,1)]
        edges = [Edge(points[0],points[1])]

        # x = points[:,0].flatten()
        # y = points[:,1].flatten()
        # z = points[:,2].flatten()
        fig = plt.figure()
        ax = fig.gca(projection='3d')

        for e in edges:
            ax.plot([e.p1.x, e.p2.x], [e.p1.y, e.p2.y], [e.p1.z, e.p2.z])
        # for i in range(len(edges)):
        #     x_of_edge = (x[edges.T].T[i])
        #     y_of_edge = (y[edges.T].T[i])
        #     z_of_edge = (z[edges.T].T[i])
        #     ax.plot(x_of_edge, y_of_edge, z_of_edge)#, linestyle='-', color='y',
        #          # markerfacecolor='red', marker='o')
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
