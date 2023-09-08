# TODO: individuare un valore di seed adatto

import parser
import os
import graph
import greedy
import plot
import grasp

test_file = "pedibus_50"  # edit this if you do not want to pass a command line arg.

file_path = ".." + os.path.sep + "instances" + os.path.sep + test_file + ".dat"

data = parser.get_data(file_path)

gr = graph.Graph(data)

print("Greedy search")
greedy_leaves, greedy_edges, greedy_length = greedy.greedy_algorithm(gr)
print(f"numero di percorsi: {greedy_leaves}, lunghezza: {greedy_length}\n")

print("Greedy randomized")
seed = 1.5
iterations = 1000
score, grasp_leaves, grasp_edges, grasp_length = grasp.greedy_randomized(gr, iterations, seed)
print(f"numero di percorsi: {grasp_leaves}, lunghezza: {grasp_length}\n")

plot.plot_graph(greedy_leaves, greedy_edges, gr.delta, (test_file + "_greedy"))

plot.plot_graph(grasp_leaves, grasp_edges, seed, (test_file + "_grasp"))
