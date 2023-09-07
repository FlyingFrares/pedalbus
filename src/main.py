import data_parser
import os
import graph
import greedy
import plot

test_file = "pedibus_10"  # edit this if you do not want to pass a command line arg.

file_path = ".." + os.path.sep + "instances" + os.path.sep + test_file + ".dat"

data = data_parser.get_data(file_path)

gr = graph.Graph(data)

leaves, edges = greedy.min_distance(gr)

print(f"Il numero minimo di percorsi è {leaves}")

plot.plot_graph(edges)
