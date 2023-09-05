import math
import numpy as np
from operator import itemgetter

ROOT = 0


def union(parent, rank, x, y):

    # Attach smaller rank tree under root of
    # high rank tree (Union by Rank)
    if rank[x] < rank[y]:
        parent[x] = y
    elif rank[x] > rank[y]:
        parent[y] = x

    # If ranks are same, then make one as root
    # and increment its rank by one
    else:
        parent[y] = x
        rank[x] += 1


class Graph:
    """
    It provides useful methods to get information about the graph
    """

    def __init__(self, data):
        self.n = int(data.n) + 1    # number of nodes of the graph
        self.delta = data.delta     # delta parameter
        self.coordX = data.coordX   # X coordinates of the points
        self.coordY = data.coordY   # Y coordinates of the points
        self.dist = np.zeros([self.n, self.n])
        self.graph = []
        self.__init_dist_matrix()

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def get_root_vector(self):
        """
        get the distances from the root to the other nodes
        :return: a tuple that contains the distances from the root to the other nodes
        """
        return tuple(self.dist[ROOT, 0:self.n])

    def __init_dist_matrix(self):
        for i in range(0, self.n):
            for j in range(i, self.n):
                if i == j:
                    continue
                dis = round(euclidean_distance(self.coordX[i], self.coordX[j], self.coordY[i], self.coordY[j]), 1)
                self.dist[i, j] = dis
                self.dist[j, i] = dis

    def get_root_distance(self, node):
        return self.dist[ROOT, node]

    def get_distance(self, node1, node2):
        return self.dist[node1, node2]

    def get_edge_distance(self, edge):
        return self.get_distance(edge[0], edge[1])

    def get_ordered_vector(self, nodes):
        """
        Get an ordered vector based on the distance with the root node.
        The element 0 of the vector, therefore, is the nearest node to the root, while the last one will be the farthest
        :param nodes: the nodes that you want to compare
        :return: returns an ordered list based on the distance with the root node.
        """

        vector = []
        for n in nodes:
            vector.append([n, self.get_root_distance(n)])
        vector.sort(key=itemgetter(1))
        return [item[0] for item in vector]  # I take only the nodes, not their distance

    def find(self, parent, i):
        if parent[i] != i:
            # Reassignment of node's parent
            # to root node as
            # path compression requires
            parent[i] = self.find(parent, parent[i])
        return parent[i]

    def kruskal(self):
        # initialize the graph
        n = len(self.dist)

        for na in range(n):
            for nb in range(n):
                if na != nb:
                    distance = (self.dist[na][nb])
                    self.add_edge(na, nb, distance)

        # This will store the resultant MST
        result = []

        # An index variable, used for sorted edges
        i = 0

        # An index variable, used for result[]
        e = 0

        # Sort all the edges in
        # non-decreasing order of their
        # weight
        self.graph = sorted(self.graph,
                            key=lambda item: item[2])

        parent = []
        rank = []

        # Create n subsets with single elements
        for node in range(self.n):
            parent.append(node)
            rank.append(0)

        # Number of edges to be taken is less than to n-1
        while e < self.n - 1:

            # Pick the smallest edge and increment
            # the index for next iteration
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            # If including this edge doesn't
            # cause cycle, then include it in result
            # and increment the index of result
            # for next edge
            if x != y:
                e = e + 1
                result.append([u, v, w])
                union(parent, rank, x, y)
        # Else discard the edge

        minimumcost = 0
        print("Edges in the constructed MST")
        for u, v, weight in result:
            minimumcost += weight
            print("%d -- %d == %.1f" % (u, v, weight))
        print("Minimum Spanning Tree", round(minimumcost, 1))


def euclidean_distance(p1_x, p2_x, p1_y, p2_y):
    dist = math.sqrt(math.pow(p1_x - p2_x, 2) + math.pow(p1_y - p2_y, 2))
    return dist
