import networkx as nx
import matplotlib.pyplot as plt
import os


def plot_graph(leaves, edges, delta, filename):
    plt.title(f"nodi: {len(edges)}; delta: {delta}; foglie: {leaves}")
    G = nx.Graph()
    G.add_edges_from(edges)
    pos = nx.spring_layout(G, iterations=500)
    if len(edges) <= 10:
        nx.draw(G, pos, with_labels=True, node_size=500, node_color='skyblue', font_size=12, font_color='black')
    elif len(edges) <= 20:
        nx.draw(G, pos, with_labels=True, node_size=100, node_color='skyblue', font_size=10, font_color='black')
    else:
        nx.draw(G, pos, with_labels=False, node_size=50, node_color='skyblue')

    """
    # save the graph
    file_path = (".." + os.path.sep + "images" + os.path.sep + filename + "_" + str(delta) + ".png")
    plt.savefig(file_path, format="png", dpi=600)
    """
    # show the graph
    plt.show()
