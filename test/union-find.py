# A class to represent a graph object
class Graph:

	# Constructor
	def __init__(self, edges, n):
		self.adjList = [[] for _ in range(n)]

		# add edges to the undirected graph (add each edge once only to avoid
		# detecting cycles among the same edges, say x -> y and y -> x)
		for (src, dest) in edges:
			self.adjList[src].append(dest)


# A class to represent a disjoint set
class DisjointSet:

	parent = {}

	# perform MakeSet operation
	def makeSet(self, n):

		# create `n` disjoint sets (one for each vertex)
		for i in range(n):
			self.parent[i] = i

	# Find the root of the set in which element `k` belongs
	def find(self, k):

		# if `k` is root
		if self.parent[k] == k:
			return k

		# recur for the parent until we find the root
		return self.find(self.parent[k])

	# Perform Union of two subsets
	def union(self, a, b):

		# find the root of the sets in which elements `x` and `y` belongs
		x = self.find(a)
		y = self.find(b)

		self.parent[x] = y


# Returns true if the graph has a cycle
def findCycle(graph, n):

	# initialize `DisjointSet` class
	ds = DisjointSet()

	# create a singleton set for each element of the universe
	ds.makeSet(n)

	# consider every edge (u, v)
	for u in range(n):

		# Recur for all adjacent vertices
		for v in graph.adjList[u]:

			# find the root of the sets to which elements `u` and `v` belongs
			x = ds.find(u)
			y = ds.find(v)

			# if both `u` and `v` have the same parent, the cycle is found
			if x == y:
				return True
			else:
				ds.union(x, y)

	return False


# Union–find algorithm for cycle detection in a graph
if __name__ == '__main__':

	edges = [
		(0, 1), (0, 6), (0, 7), (1, 2), (1, 5), (2, 3),
		(2, 4), (7, 8), (7, 11), (8, 9), (8, 10), (10, 11)
		# edge (10, 11) introduces a cycle in the graph
	]

	# total number of nodes in the graph (labelled from 0 to 11)
	n = 12

	# construct graph
	graph = Graph(edges, n)

	if findCycle(graph, n):
		print('Cycle Found')
	else:
		print('No Cycle is Found')
