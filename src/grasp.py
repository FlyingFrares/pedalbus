import random

ROOT = 0


def find_next(seed, graph, previous_node, not_visited, path_length):
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


def greedy_rand(graph, seed):
    """
    It executes an iteration of the algorithm and returns the score and the edges associated to it
    :param graph: the graph on which you want to apply the algorithm
    :param iterations: the number of iterations that you want to perform
    :param seed: the seed that you want to use to perform this iteration. It decides the entity of the randomization
    :return: the score, the edges that form the solution path, the number of leaves and the total length of the path
    """
    previous = ROOT
    curr_path_length = 0
    nodes_not_visited = set(range(1, graph.n))
    edges = []
    leaves_counter = 1  # I initialize this to one to add the last one
    total_length = 0

    while nodes_not_visited:  # while nodes_not_visited is not empty
        next_node = find_next(seed, graph, previous, nodes_not_visited, curr_path_length)
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

def graspframework(graph, iterations, seed):
    best_score = float("inf")
    best_leaves = float("inf")
    best_edges = []
    best_length = float("inf")

    for i in range(iterations):

        # Construction Phase -> constructed solution
        c_leaves, c_edges, c_lenght = greedy_rand(graph, seed)

        # Local Search Phase -> improved solution
        is_leaves, is_edges, is_length = local_search(c_edges)

        score = str(is_leaves) + "." + str(is_length).replace(".", "")

        # Update the best solution if an improvement is found
        if float(score) < best_score:
            best_score = float(score)
            best_leaves = is_leaves
            best_edges = is_edges.copy()
            best_length = is_length

    return float(best_score), best_leaves, best_edges, best_length

"""def local_search(edges):
    #local search implementation

    return leaves_counter, edges, total_length"""

def local_search(edges, graph):
    # Initialize the current solution with the provided edges
    current_edges = edges
    current_length = sum(graph.get_edge_distance(edge) for edge in current_edges)
    current_leaves = count_leaves(current_edges, graph)

    best_edges = current_edges
    best_length = current_length
    best_leaves = current_leaves

    # Define a neighborhood search operator (e.g., 2-opt)
    def two_opt_swap(solution_edges):
        # Implement a 2-opt swap operator to explore neighbors
        # Modify the edges to improve the solution
        pass

    # Local search parameters
    max_iterations = 1000  # You can adjust this based on your problem and performance requirements

    iteration = 0
    while iteration < max_iterations:
        # Generate a neighboring solution using the 2-opt operator
        neighbor_edges = two_opt_swap(current_edges)

        # Calculate the length and leaves of the neighbor solution
        neighbor_length = sum(graph.get_edge_distance(edge) for edge in neighbor_edges)
        neighbor_leaves = count_leaves(neighbor_edges, graph)

        # Check if the neighbor solution is better
        if neighbor_length < current_length:
            current_edges = neighbor_edges
            current_length = neighbor_length
            current_leaves = neighbor_leaves

            # Update the best solution if an improvement is found
            if neighbor_length < best_length:
                best_edges = neighbor_edges
                best_length = neighbor_length
                best_leaves = neighbor_leaves
        else:
            # Terminate the search if no better neighbor is found
            break

        iteration += 1

    return best_leaves, best_edges, best_length

def count_leaves(edges, graph):
    # Count the number of leaves in the solution
    # You can implement this based on your graph representation
    pass
