__author__ = 'Jason'


def degree_distribution(graph):
    distribution = dict()
    for node_id in graph.dictionary:
        n = len(graph.dictionary[node_id].links)
        if n in distribution:
            val = distribution[n]
            val += 1
            distribution[n] = val
        else:
            distribution[n] = 1

    total_nodes = len(graph.dictionary)
    results = []
    for val in distribution:
        results.append((val, distribution[val]/total_nodes))

    """Use GnuPlot to display distribution"""
    return


def diameter(graph):
    max_path = 0
    for node_id in graph.dictionary:
        distances = graph.reach_node_n(node_id)
        for path in distances:
            if path[1] > max_path:
                max_path = path[1]

    return max_path


def average_path_length(graph):
    sum_of_paths = 0
    paths_number = 0

    for node_id in graph.dictionary:
        distances = graph.reach_node_n(node_id)
        for path in distances:
            paths_number += 1
            sum_of_paths += path[1]

    average = sum_of_paths/paths_number
    return average


def number_of_connected_components(graph):
    visited_nodes = []
    number_of_cc = 0
    for node_id in graph.dictionary:
        if node_id not in visited_nodes:
            bfs_generator = graph.graph_bfs(node_id)
            visited_nodes.append(node_id)
            for path in bfs_generator:
                if path[0] not in visited_nodes:
                    visited_nodes.append(path[0])

            number_of_cc += 1

    return number_of_cc


def max_connected_component(graph):
    visited_nodes = []
    max_cc = 0
    for node_id in graph.dictionary:
        if node_id not in visited_nodes:
            cc_size = 1
            bfs_generator = graph.graph_bfs(node_id)
            visited_nodes.append(node_id)
            for path in bfs_generator:
                if path[0] not in visited_nodes:
                    cc_size += 1
                    visited_nodes.append(path[0])

            if cc_size > max_cc:
                max_cc = cc_size

    return max_cc


def density(graph):
    den = (2*graph.number_of_edges)/(graph.number_of_nodes*(graph.number_of_nodes - 1))
    return den


def closeness_centrality(graph, node_id):
    bfs_generator = graph.graph_bfs(node_id)
    cc = 0
    for path in bfs_generator:
        if path[1] > 0:
            cc += 1/path[1]

    normalized_cc = cc/(graph.number_of_nodes - 1)
    return normalized_cc

