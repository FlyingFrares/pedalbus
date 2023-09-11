"""
    file that contains the implementation of the local search phase
"""

import random


def run_algorithm(graph, initial_score, initial_leaves, initial_edges, initial_length):
    current_score = initial_score
    current_leaves = initial_leaves
    current_edges = initial_edges.copy()
    current_length = initial_length

    # Imposta un criterio di arresto, ad esempio, un numero massimo di iterazioni.
    iterations = 100

    for i in range(iterations):
        # Genera una mossa casuale
        new_edges = generate_random_move(current_edges)

        # Valuta se la nuova soluzione è ammissibile e calcola il suo score
        new_score, new_leaves, new_length = evaluate_solution(graph, new_edges)

        # Verifica se la nuova soluzione è migliore di quella corrente
        if new_score < current_score:
            current_score = new_score
            current_leaves = new_leaves
            current_edges = new_edges
            current_length = new_length
            break  # Termina la ricerca locale

    return current_score, current_leaves, current_edges, current_length


def generate_random_move(current_edges):
    #TODO: implementare la funzione

def evaluate_solution(graph, new_edges):
    #TODO: implementare la funzione
