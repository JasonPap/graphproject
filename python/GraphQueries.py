

def match_suggestion(graph, node, interests, hops, age_diff, limit):

    if node not in graph.dictionary:
        print 'Node ' + node + ' is not in the graph'
        return -1

    bfs_generator = graph.graph_bfs(node)

    for result in bfs_generator:
        temp = graph.lookup_node(graph, result[0])
        for attr in node.attributes:
            if attr in temp.att