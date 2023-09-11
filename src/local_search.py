"""
    file that contains the implementation of the local search phase
"""

import random
import copy

ROOT = 0


def run_algorithm(graph, initial_score, initial_leaves, initial_edges, initial_length, iterations):
    """
    this function executes a first improvement local search phase
    :param graph: the graph on which you want to apply the algorithm
    :param initial_score: the score of the greedy randomized solution
    :param initial_leaves: the number of leaves of the greedy randomized solution
    :param initial_edges: the edges that form the greedy randomized solution
    :param initial_length: the total length of the greedy randomized solution
    :param iterations: the number of iterations that you want to perform
    :return: the best score, the edges that form the best solution path found,
             the best number of leaves and the total length of the best path
    """
    best_score = initial_score
    best_leaves = initial_leaves
    best_edges = copy.deepcopy(initial_edges)
    best_length = initial_length

    for i in range(iterations):
        # Genera una mossa casuale
        new_paths, new_edges = one_to_one_exchange(best_edges)

        # Valuta se la nuova soluzione è ammissibile e calcola il suo score
        new_score, new_leaves, new_length = evaluate_solution(graph, new_paths, new_edges)

        # Verifica se la nuova soluzione è migliore di quella corrente
        if float(new_score) < best_score:
            best_score = float(new_score)
            best_leaves = new_leaves
            best_edges = copy.deepcopy(new_edges)
            best_length = new_length
            break  # Termina la ricerca locale

    return best_score, best_leaves, best_edges, best_length


def one_to_one_exchange(current_edges):
    """
    this function implements the one-to-one exchange for the local search
    :param current_edges: the edges that form the best current solution
    :return: the paths and the edges of the new solution to evaluate
    """

    new_edges = copy.deepcopy(current_edges)
    new_paths = arch_to_path(new_edges)

    # Scegli casualmente due sottoliste diverse
    percorso1 = random.choice(new_paths)
    new_paths.remove(percorso1)
    percorso2 = random.choice(new_paths)
    new_paths.remove(percorso2)

    # Scegli casualmente un nodo da ciascuna sottolista
    arco1 = random.choice(percorso1)
    arco2 = random.choice(percorso2)

    vertice1 = 0
    vertice2 = 0

    while vertice1 == 0:
        vertice1 = random.choice(arco1)
    while vertice2 == 0:
        vertice2 = random.choice(arco2)

    # Sostituisci tutte le occorrenze di vertice1 in percorso1 con vertice2
    for arco in percorso1:
        if vertice1 in arco:
            arco[arco.index(vertice1)] = vertice2
    for arco in percorso2:
        if vertice2 in arco:
            arco[arco.index(vertice2)] = vertice1

    new_paths.append(percorso1)
    new_paths.append(percorso2)

    new_edges = path_to_arch(new_paths)

    return new_paths, new_edges


def evaluate_solution(graph, paths, edges):
    """
    this function evaluates the solution and returns its score
    :param graph: the graph on which you want to apply the algorithm
    :param paths: the paths generated by the one-to-one exchange
    :param edges: the edges generated by the one-to-one exchange
    :return: the score, the number of leaves and the total length of the solution, if feasible
    """
    total_length = 0
    leaves_counter = 0
    for path in paths:
        if is_feasible(graph, path):
            continue
        else:
            return float("inf"), float("inf"), float("inf")

    for edge in edges:
        total_length += graph.get_edge_distance(edge)
        for node in edge:
            if node == ROOT:
                leaves_counter += 1

    score = str(leaves_counter) + "." + str(total_length).replace(".", "")

    return score, leaves_counter, total_length


def arch_to_path(edges):
    paths = []
    path = []

    for edge in edges:
        if edge[0] == 0:
            if path:
                paths.append(path)
            path = [edge]
        else:
            path.append(edge)

    if path:
        paths.append(path)

    return paths


def path_to_arch(paths):
    edges = []
    # Scorrere le liste di liste di liste
    for path in paths:
        edges.extend(path)

    return edges


def is_feasible(graph, path):
    curr_path_length = 0

    for edge in path:
        curr_path_length += graph.get_edge_distance(edge)
        if curr_path_length > graph.get_root_distance(edge[1]) * graph.delta:
            return False

    return True