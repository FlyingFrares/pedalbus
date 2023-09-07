import data_parser
import os
import graph
import greedy
import plot

test_file = "pedalbus_300"  # edit this if you do not want to pass a command line arg.

file_path = ".." + os.path.sep + "instances" + os.path.sep + test_file + ".dat"

data = data_parser.get_data(file_path)

gr = graph.Graph(data)

print("Greedy search:")

leaves, edges = greedy.min_distance(gr)

print(f"Il numero minimo di percorsi è {leaves}\n")

plot.plot_graph(edges, leaves, gr.delta, test_file)
