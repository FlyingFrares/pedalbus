# TODO: individuare un valore di seed adatto
# TODO: individuare un valore di iterations adatto
# TODO: individuare un valore di ls_iterations adatto

import parser
import time
import os
import graph
import greedy
import plot
import grasp

test_file = "pedibus_10"  # edit this if you do not want to pass a command line arg.

file_path = ".." + os.path.sep + "instances" + os.path.sep + test_file + ".dat"

data = parser.get_data(file_path)

gr = graph.Graph(data)

print("\n")

print("Greedy search")
greedy_leaves, greedy_edges, greedy_length = greedy.run_algorithm(gr)
print(f"numero di percorsi: {greedy_leaves}, lunghezza: {greedy_length}\n")
plot.plot_graph(greedy_leaves, greedy_edges, gr.delta, (test_file + "_greedy"))

seed = 1.5
iterations = 100

print("Almost GRASP")
start_time = time.time()
bg_score, bg_leaves, bg_edges, bg_length = grasp.basic_grasp(gr, iterations, seed)
end_time = time.time()
elapsed_time = end_time - start_time
print(f"numero di percorsi: {bg_leaves}, lunghezza: {bg_length}")
print(f"Tempo di esecuzione: {elapsed_time} secondi\n")
plot.plot_graph(bg_leaves, bg_edges, gr.delta, (test_file + "_almost_grasp"))

ls_iterations = 1000

print("GRASP")
start_time = time.time()
grasp_score, grasp_leaves, grasp_edges, grasp_length = grasp.full_grasp(gr, iterations, seed, ls_iterations)
end_time = time.time()
elapsed_time = end_time - start_time
print(f"numero di percorsi: {grasp_leaves}, lunghezza: {grasp_length}")
print(f"Tempo di esecuzione: {elapsed_time} secondi\n")
plot.plot_graph(grasp_leaves, grasp_edges, seed, (test_file + "_grasp"))

