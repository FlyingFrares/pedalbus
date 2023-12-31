import math
import numpy as np
from operator import itemgetter

ROOT = 0


class Graph:
    """
    It provides useful methods to get information about the graph
    """

    def __init__(self, data):
        self.n = int(data.n) + 1  # number of nodes of the graph
        self.delta = data.delta  # delta parameter
        self.coordX = data.coordX  # X coordinates of the points
        self.coordY = data.coordY  # Y coordinates of the points
        self.dist = np.zeros([self.n, self.n])
        self.__init_dist_matrix()

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
        The element 0 of the vector, therefore, is the nearest node to the root, while the last one will be farthest
        :param nodes: the nodes that you want to compare
        :return: returns an ordered list based on the distance with the root node.
        """

        vector = []
        for n in nodes:
            vector.append([n, self.get_root_distance(n)])
        vector.sort(key=itemgetter(1))
        return [item[0] for item in vector]  # I take only the nodes, not their distance


def euclidean_distance(p1_x, p2_x, p1_y, p2_y):
    dist = math.sqrt(math.pow(p1_x - p2_x, 2) + math.pow(p1_y - p2_y, 2))
    return dist
