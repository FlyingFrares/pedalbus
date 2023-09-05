# TODO: Rendi il plot adattivo al codice sorgente

import networkx as nx
import matplotlib.pyplot as plt

# Definisci i nodi e gli archi
edges = [(0, 10), (0, 8), (1, 5), (2, 9), (4, 8), (2, 4), (1, 3), (0, 3), (5, 7), (5, 6)]

# Crea un grafico
G = nx.Graph()

# Aggiungi nodi e archi al grafico
G.add_edges_from(edges)

# Disegna il grafico
pos = nx.spring_layout(G)  # Calcola le posizioni dei nodi
nx.draw(G, pos, with_labels=True, node_size=500, node_color='skyblue', font_size=10, font_color='black')
plt.show()
