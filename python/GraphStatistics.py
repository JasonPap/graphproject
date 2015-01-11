__author__ = 'Jason'

from collections import deque


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
        distances = graph.graph_bfs(node_id)
        for path in distances:
            if path[1] > max_path:
                max_path = path[1]

    return max_path


def average_path_length(graph):
    sum_of_paths = 0
    paths_number = 0

    """
    option 2
    nodes_ids = []
    for i in graph.dictionary:
        nodes_ids.append(i)
    l_size = len(nodes_ids)
    for i in range(l_size):
        for j in range(i+1, l_size):
            paths = graph.dijkstra_shortest_paths_from(nodes_ids[i], nodes_ids[j])
            for path in paths:
                paths_number += 1
                sum_of_paths += len(path)

    """

    for node_id in graph.dictionary:
        distances = graph.graph_bfs(node_id)
        for path in distances:
            paths_number += 1
            sum_of_paths += path[1]

    average = float(sum_of_paths)/float(paths_number)
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


def get_connected_components(graph):
    visited_nodes = []
    connected_components = []
    for node_id in graph.dictionary:
        if node_id not in visited_nodes:
            cc = [node_id]
            bfs_generator = graph.graph_bfs(node_id)
            visited_nodes.append(node_id)
            for path in bfs_generator:
                if path[0] not in visited_nodes:
                    visited_nodes.append(path[0])
                    cc.append(path[0])

            connected_components.append(cc)

    return connected_components


def density(graph):
    den = float((2*graph.number_of_edges))/float((graph.number_of_nodes*(graph.number_of_nodes - 1)))
    return den


def closeness_centrality(graph, node_id):
    bfs_generator = graph.graph_bfs(node_id)
    cc = 0.0
    i = 0
    for path in bfs_generator:
        if path[1] >= 0:
            i += 1
            cc += 1.0/float(path[1])

    normalized_cc = float(cc)/float(graph.number_of_nodes - 1)
    return normalized_cc


def closeness_centrality_2(graph, node_id):
    cc = 0.0
    for i in graph.dictionary:
        if i != node_id:
            dij = graph.dijkstra_shortest_paths_from(node_id, i)
            for path in dij:
                cc += 1.0/float(len(path))

    norma = float(cc)/float((graph.number_of_nodes - 1))
    return norma


def betweenness_centrality(graph):
    CB = dict()
    for s in graph.dictionary:
        S = []  # stack
        P = dict()
        sigma = dict()
        d = dict()
        delta = dict()
        for i in graph.dictionary:
            sigma[i] = 0
            d[i] = -1
            P[i] = []
            delta[i] = 0
        sigma[s] = 1
        d[s] = 0
        Q = deque()
        Q.append(s)
        while Q:
            v = Q.popleft()
            S.append(v)
            node_v = graph.lookup_node(v)
            for W in node_v.links:
                w = W.edge_end
                if d[w] < 0:
                    Q.append(w)
                    d[w] = d[v] + 1

                if d[w] == (d[v] + 1):
                    sigma[w] += sigma[v]
                    P[w].append(v)

        # delta[v] = 0 v in V
        while S:
            w = S.pop()
            for v in P[w]:
                delta[v] += (float(sigma[v])/float(sigma[w]))*(1 + delta[w])
            if w != s:
                if w in CB:
                    CB[w] += delta[w]
                else:
                    CB[w] = delta[w]
            elif w not in CB:
                CB[w] = 0

    size = len(graph.dictionary)
    param = float((size - 1)*(size - 2))    # alagi logo directed graph
    for i in CB:
        CB[i] = float(CB[i])/float(param)
    return CB


def betweenness_centrality_slow(graph, node_id):
    paths_with_node = 0
    paths_num = 0

    nodes_ids = []
    for i in graph.dictionary:
        nodes_ids.append(i)
    l_size = len(nodes_ids)
    for i in range(l_size):
        for j in range(i+1, l_size):
            paths = graph.dijkstra_shortest_paths_from(nodes_ids[i], nodes_ids[j])
            for path in paths:
                paths_num += 1
                if node_id in path:
                    paths_with_node += 1

    CB = float(paths_with_node)/float(paths_num)
    tmp = float((l_size - 1)*(l_size - 2))/2.0
    CB = CB/tmp

    return CB


def edge_betweeness_centrality(graph):
    CB = dict()
    Q = deque()
    S = []  # stack
    delta = dict()
    for s in graph.dictionary:
        # single-source shortest-paths problem
        # initialization
        Pred = dict()
        dist = dict()
        sigma = dict()
        for w in graph.dictionary:
            Pred[w] = []
            dist[w] = float("inf")
            sigma[w] = 0

        dist[s] = 0
        sigma[s] = 1
        Q.append(s)

        while Q:
            v = Q.pop()
            S.append(v)

            links = graph.dictionary[v].links
            neibghours = []
            for edge in links:
                neibghours.append(edge.edge_end)

            for neibghour in neibghours:
                # path discovery
                if dist[w] == float("inf"):
                    dist[w] = dist[v] + 1
                    Q.append(w)

                #path counting
                if dist[w] == dist[v] + 1:
                    sigma[w] = sigma[w] + sigma[v]
                    Pred[w].append(v)

        #accumulation
        for v in graph.dictionary:
            delta[v] = 0

        while S:
            w = S.pop()
            for v in Pred[w]:
                delta[v] = delta[v] + (float(sigma[v])/float(sigma[w])) * (1 + delta[w])

            if w != s:
                CB[w] = CB[w] + delta[w]
            elif w not in CB:
                CB[w] = 0

    return CB

