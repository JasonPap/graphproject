__author__ = 'Jason'

import itertools
import Graph
from Graph import *


def get_cliques(graph, k, proc_pool):
    persons = []
    for idx in graph.dictionary:
        persons.append(idx)

    cliques = []
    combinations = itertools.combinations(persons, k)
    arg = []
    for comb in combinations:
        arg.append((comb, graph))
    results = proc_pool.map(test, arg)
    for result in results:
        if result[0] is True:
            cliques.append(result[1])

    return cliques


def test(arg):
    combination = arg[0]
    graph = arg[1]
    local_comb = list(combination)
    for idx in combination:
        others = list(local_comb)
        others.remove(idx)
        links = graph.dictionary[idx].links
        linked_ids = []
        for edge in links:
            linked_ids.append(edge.edge_end)

        for neighbour in others:
            if neighbour not in linked_ids:
                return False

        local_comb.remove(idx)

    return True, combination


def get_hyper_cliques(graph, k, proc_pool):
    l_cliques = get_cliques(graph, k, proc_pool)
    g_cliques = Graph()
    for i in range(len(l_cliques)):
        node = Node(i, [], [])
        g_cliques.insert_node(node)

    for i in g_cliques.dictionary:
        # homework