__author__ = 'Jason'

import itertools
from Graph import *
from GraphStatistics import *


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
        if result[0] == True:
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
                return False, None

        local_comb.remove(idx)

    return True, combination


def percolation_method(graph, k, proc_pool):
    l_cliques = get_cliques(graph, k, proc_pool)
    g_cliques = Graph()
    for i in range(len(l_cliques)):
        node = Node(i, [], [])
        g_cliques.insert_node(node)

    arg = []
    for i in range(len(l_cliques)):
        arg.append((i, l_cliques, k))
    results = proc_pool.map(get_hyper_edges, arg)

    for result in results:
        for hyper_edge in result:
            edge = Edge(hyper_edge[1], [])
            g_cliques.insert_edge(hyper_edge[0], edge)

    cc = get_connected_components(g_cliques)
    communities = []
    counter = 1
    for component in cc:
        persons = []
        for clique_id in component:
            for p_id in l_cliques[clique_id]:
                if p_id not in persons:
                    persons.append(p_id)

        persons.sort()
        communities.append((counter, persons))
        counter += 1

    return communities


def get_hyper_edges(arg):
    clique_id = arg[0]
    l_cliques = arg[1]
    k = arg[2]
    result = []

    main_clique = l_cliques[clique_id]
    for i in range(len(l_cliques)):
        counter = 0
        if i != clique_id:
            for val in main_clique:
                if val in l_cliques[i]:
                    counter += 1
            if counter >= k - 1:
                result.append((clique_id, i))

    return result


