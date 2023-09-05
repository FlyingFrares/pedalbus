import networkx as nx
import matplotlib.pyplot as plt

# Creazione di un grafo
G = nx.Graph()

# Aggiungi i collegamenti e le rispettive distanze
edges = [
    (0, 10, 5.0),
    (0, 8, 6.4),
    (1, 5, 7.6),
    (2, 9, 7.6),
    (4, 8, 9.2),
    (2, 4, 12.2),
    (1, 3, 12.4),
    (0, 3, 15.0),
    (5, 7, 26.2),
    (5, 6, 27.8),
]

for edge in edges:
    G.add_edge(edge[0], edge[1], weight=edge[2])

# Disegna il grafo
pos = nx.spring_layout(G)  # Layout del grafo
labels = nx.get_edge_attributes(G, 'weight')
nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue')
plt.show()