"""
file that contains the implementation of all the GRASP variants
"""

import greedy_randomized
import local_search
import copy


ROOT = 0


def almost_grasp(graph, iterations, seed):
    """
    this function executes a GRASP algorithm without the local search phase
    :param graph: the object that contains the information about the graph
    :param iterations: the number of iterations that you want to perform
    :param seed: the seed that you want to use to perform this iteration. It decides the entity of the randomization
    :return: the edges that form the best solution path found,
             the best number of leaves and the total length of the best path
    """

    best_leaves = float("inf")
    best_edges = []
    best_length = float("inf")

    for i in range(iterations):
        leaves, edges, length = greedy_randomized.run_algorithm(graph, seed)
        if leaves <= best_leaves:
            if leaves < best_leaves or length < best_length:
                best_leaves = leaves
                best_edges = copy.deepcopy(edges)
                best_length = length

    return best_leaves, best_edges, best_length


def full_grasp(graph, iterations, seed, ls_iterations):
    """
    this function executes a GRASP algorithm with the local search phase
    :param graph: the object that contains the information about the graph
    :param iterations: the number of iterations that you want to perform
    :param seed: the seed that you want to use to perform this iteration. It decides the entity of the randomization
    :param ls_iterations: the number of iterations that you want to perform for the local search phase
    :return: the edges that form the best solution path found,
             the best number of leaves and the total length of the best path
    """

    best_leaves = float("inf")
    best_edges = []
    best_length = float("inf")

    for i in range(iterations):

        # Solution ← Greedy Randomized Construction(Seed);
        c_leaves, c_edges, c_length = greedy_randomized.run_algorithm(graph, seed)

        # Solution ← Local Search(Solution);
        ls_leaves, ls_edges, ls_length = local_search.run_algorithm(graph, c_leaves, c_edges,
                                                                    c_length, ls_iterations)

        # Update the best solution if an improvement is found
        if ls_leaves <= best_leaves:
            if ls_leaves < best_leaves or ls_length < best_length:
                best_leaves = ls_leaves
                best_edges = copy.deepcopy(ls_edges)
                best_length = ls_length

    return best_leaves, best_edges, best_length
