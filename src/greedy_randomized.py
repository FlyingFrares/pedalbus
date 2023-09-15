"""
file that contains the implementation of the greedy randomized algorithm
"""

import random

ROOT = 0


def rcl(seed, graph, previous_node, not_visited, path_length):
    """
    this function finds the next node to add to the path.
    :param seed: the seed that you want to use to perform this iteration. It decides the entity of the randomization
    :param graph: the object that contains the information about the graph
    :param previous_node: the previous node in the path
    :param not_visited: nodes that have not been visited yet
    :param path_length: the current path length
    :return: the next node to add to the path
    """

    curr_min_path_length = float("inf")

    # distance between the previous_node and the node that is closer to it among the not visited ones
    curr_prev_node_min_distance = float("inf")

    candidate_list = []  # nodes that you can add to the current path
    for node_x in not_visited:
        new_path_length = path_length + graph.get_distance(previous_node, node_x)
        node_x_min_distance = graph.get_root_distance(node_x)

        if new_path_length < node_x_min_distance * graph.delta:  # the node if feasible
            candidate_list.append(node_x)
            if new_path_length < curr_min_path_length:
                curr_min_path_length = new_path_length
                curr_prev_node_min_distance = graph.get_distance(previous_node, node_x)

    if candidate_list:  # if there are nodes that you can add to the current path
        restricted_candidate_list = []
        # I select only the nodes that has a distance from the previous node which
        # is <= than curr_prev_node_min_distance * seed
        for node_x in candidate_list:
            new_node_distance = graph.get_distance(previous_node, node_x)
            if new_node_distance <= curr_prev_node_min_distance * seed:
                restricted_candidate_list.append(node_x)

        # I select one node randomly among the best ones
        rand = random.randint(0, len(restricted_candidate_list) - 1)
        return restricted_candidate_list[rand]
    else:
        return -1


def run_algorithm(graph, seed):
    """
    It executes an iteration of the greedy randomized algorithm
    :param graph: the graph on which you want to apply the algorithm
    :param seed: the seed that you want to use to perform this iteration. It decides the entity of the randomization
    :return: the edges that form the solution path, the number of leaves and the total length of the path
    """

    previous = ROOT
    curr_path_length = 0
    nodes_not_visited = set(range(1, graph.n))
    edges = []
    leaves_counter = 1  # I initialize this to one to add the last one
    total_length = 0

    while nodes_not_visited:  # while nodes_not_visited is not empty
        next_node = rcl(seed, graph, previous, nodes_not_visited, curr_path_length)
        if next_node != -1:  # I found a feasible node that can be added to the current path
            nodes_not_visited.remove(next_node)
            new_edge = [previous, next_node]
            edges.append(new_edge)
            previous = next_node
            curr_path_length += graph.get_edge_distance(new_edge)
        else:  # you cannot add other nodes to the current path, so I create a new path starting from the root
            total_length += curr_path_length
            curr_path_length = 0
            previous = ROOT
            leaves_counter += 1

    total_length += curr_path_length

    return leaves_counter, edges, total_length
