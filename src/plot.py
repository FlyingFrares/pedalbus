# TODO: Rendi il plot adattivo al codice sorgente

import networkx as nx
import matplotlib.pyplot as plt


def plot_graph(edges):
    G = nx.Graph()
    G.add_edges_from(edges)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=500, node_color='skyblue', font_size=10, font_color='black')
    plt.show()
