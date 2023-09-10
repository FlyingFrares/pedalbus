# TODO: individuare un valore di seed adatto

import parser
import time
import os
import graph
import greedy
import plot
import best_greedy_randomized
import grasp

test_file = "pedibus_10"  # edit this if you do not want to pass a command line arg.

file_path = ".." + os.path.sep + "instances" + os.path.sep + test_file + ".dat"

data = parser.get_data(file_path)

gr = graph.Graph(data)

print("Greedy search")

greedy_leaves, greedy_edges, greedy_length = greedy.run_algorithm(gr)

print(f"numero di percorsi: {greedy_leaves}, lunghezza: {greedy_length}\n")


print("Greedy randomized")
seed = 1.5
iterations = 1000
start_time = time.time()
ls_score, ls_leaves, ls_edges, ls_length = best_greedy_randomized.run_algorithm(gr, iterations, seed)
end_time = time.time()
elapsed_time = end_time - start_time
print(f"numero di percorsi: {ls_leaves}, lunghezza: {ls_length}\n")
print(f"Tempo di esecuzione: {elapsed_time} secondi")


# TODO: GRASP
"""
print("GRASP")
seed = 1.5
iterations = 1000
grasp_score, grasp_leaves, grasp_edges, grasp_length = grasp.graspframework(gr, iterations, seed)
print(f"numero di percorsi: {grasp_leaves}, lunghezza: {grasp_length}\n")
"""

"""
plot.plot_graph(greedy_leaves, greedy_edges, gr.delta, (test_file + "_greedy"))

plot.plot_graph(grasp_leaves, grasp_edges, seed, (test_file + "_grasp"))
"""