import matplotlib.pyplot as plt
import networkx as nx

# X and Y coordinates of the 10 points
x_coordinates = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y_coordinates = [5, 3, 8, 4, 9, 1, 6, 2, 7, 10]

# Distances between points
distances = [2.5, 1.8, 3.2, 1.5, 2.7, 3.0, 2.2, 2.9, 1.3, 2.0]

# Create the graph
G = nx.Graph()

# Add nodes to the graph
for i in range(len(x_coordinates)):
    G.add_node(i, pos=(x_coordinates[i], y_coordinates[i]))

# Add edges with distances as attributes
for i in range(len(x_coordinates)):
    for j in range(i + 1, len(x_coordinates)):
        distance = distances[i] if i < j else distances[j]  # Choose the smaller distance between the two points
        G.add_edge(i, j, weight=distance)

# Get node positions
node_positions = nx.get_node_attributes(G, 'pos')

# Create the plot
plt.figure(figsize=(8, 6))
nx.draw(G, pos=node_positions, with_labels=True, node_size=3000, node_color='lightblue', font_size=10, font_color='black')

# Add distance labels on the edges
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos=node_positions, edge_labels=edge_labels)

# Show the plot
plt.show()
