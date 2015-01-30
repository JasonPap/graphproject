__author__ = 'Jason'

from GraphStatistics import *
import itertools
import copy


def girvan_newman(given_graph, limit):
    graph = copy.deepcopy(given_graph)
    ecb = edge_betweeness_centrality(graph) # ecb is a dictionary (edge start, edge end) : centrality
    Q = -1
    prev_Q = -100
    while True:
        remove_max_edge(ecb, graph)
        ecb = edge_betweeness_centrality(graph)
        Q = compute_modularity(graph)
        # print "Q = " + str(Q)

        if Q > limit:
            # print "limit"
            break

        if (Q - prev_Q) < 0.00001:
            # print "dif"
            break

        prev_Q = Q

    # get and return connected components of the remaining graph
    components = get_connected_components(graph)
    communities = []
    i = 1
    for component in components:
        communities.append((i, component))
        i += 1

    return communities


def remove_max_edge(edge_centrality_betweeness_dict_bi, graph):
    max_val = 0
    max_edge = ()

    edge_centrality_betweeness_dict = dict()
    for edge in edge_centrality_betweeness_dict_bi:
        if edge not in edge_centrality_betweeness_dict and (edge[1], edge[0]) not in edge_centrality_betweeness_dict:
            edge_centrality_betweeness_dict[edge] = edge_centrality_betweeness_dict_bi[edge] \
                                                    + edge_centrality_betweeness_dict_bi[(edge[1], edge[0])]

    for edge in edge_centrality_betweeness_dict:
        if edge_centrality_betweeness_dict[edge] > max_val:
            max_val = edge_centrality_betweeness_dict[edge]
            max_edge = edge

    if max_edge != ():
        graph.remove_edge(max_edge[0], max_edge[1])
        graph.remove_edge(max_edge[1], max_edge[0])

    return


def compute_modularity(graph):
    # print "-----start-----"
    m = graph.number_of_edges
    total = 0.0
    node_ids = graph.get_node_ids()
    node_combinations = itertools.combinations(node_ids, 2)
    for combination in node_combinations:
        node = graph.dictionary[combination[0]]
        node_1_degree = len(node.links)
        node_2_degree = len(graph.dictionary[combination[1]].links)
        alpha = 0
        for edge in node.links:
            if edge.edge_end == combination[1]:
                alpha = 1

        delta = 0
        if graph.reach_node_1(combination[0], combination[1]) != -1:
            delta = 1

        total += (alpha - (float(node_1_degree*node_2_degree))/float(m)) * delta
        # print "total = " + str(total)
    # print "-----end-----"
    return float(total)/float(m)


