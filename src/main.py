import parser
import time
import os
import graph
import greedy
import plot
import grasp


# Configuration parameters
FILE_LIST = ["pedalbus_10", "pedalbus_20", "pedalbus_50", "pedalbus_100", "pedalbus_300"]
# TEST_FILE = "pedalbus_100"  # file su cui eseguire il test
SEED_FOR_SMALL_INSTANCES = 2  # seed per le istanze con N < 30
SEED_FOR_BIG_INSTANCES = 1.25  # seed per le istanze con N >= 30
seed = 1.5
ITERATIONS = 10000  # numero di iterazioni per GRASP
LS_ITERATIONS = 100  # numero di iterazioni per la local search
for TEST_FILE in FILE_LIST:


    print("istanza: ", TEST_FILE)
    # Main
    test_file = TEST_FILE

    file_path = ".." + os.path.sep + "instances" + os.path.sep + test_file + ".dat"

    data = parser.get_data(file_path)

    gr = graph.Graph(data)

    print("\n")

    print("Greedy search")
    greedy_leaves, greedy_edges, greedy_length = greedy.run_algorithm(gr)
    print(f"numero di percorsi: {greedy_leaves}, lunghezza: {greedy_length}\n")
    #plot.plot_graph(greedy_leaves, greedy_edges, gr.delta, (test_file + "_greedy"))
    """
    if gr.n < 30:
        seed = SEED_FOR_SMALL_INSTANCES
        iterations = ITERATIONS
    else:
        seed = SEED_FOR_BIG_INSTANCES
        iterations = ITERATIONS
    """
    iterations = ITERATIONS

    print("Almost GRASP")
    start_time = time.time()
    bg_leaves, bg_edges, bg_length = grasp.basic_grasp(gr, iterations, seed)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"numero di percorsi: {bg_leaves}, lunghezza: {bg_length}")
    print(f"Tempo di esecuzione: {elapsed_time} secondi\n")
    #plot.plot_graph(bg_leaves, bg_edges, seed, (test_file + "_almost_grasp"))

    ls_iterations = LS_ITERATIONS

    print("GRASP")
    start_time = time.time()
    grasp_leaves, grasp_edges, grasp_length = grasp.full_grasp(gr, iterations, seed, ls_iterations)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"numero di percorsi: {grasp_leaves}, lunghezza: {grasp_length}")
    print(f"Tempo di esecuzione: {elapsed_time} secondi\n")
    #plot.plot_graph(grasp_leaves, grasp_edges, seed, (test_file + "_grasp"))
