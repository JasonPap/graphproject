__author__ = 'Jason'

from FileOperations import *
from GraphStatistics import *
from  GraphQueries import *


def main():
    print "hello world"
    pkp_graph = create_graph_from_file("person_knows_person.csv")
    populate_person_graph(pkp_graph, "person.csv", "person_hasInterest_tag.csv")

    # print diameter(pkp_graph)
    # print average_path_length(pkp_graph)
    # print number_of_connected_components(pkp_graph)
    # print max_connected_component(pkp_graph)
    # print density(pkp_graph)
    # print closeness_centrality(pkp_graph, 10)
    # print closeness_centrality(pkp_graph, 75)

    g = build_trust_graph("Wall of Xiomara Fernandez", pkp_graph)
    for node_id in g.dictionary:
        node = g.lookup_node(node_id)
        for edge in node.links:
            print edge.properties["weight"]

    print len(g.dictionary)

    print estimate_trust(30, 9700, g)


    """
    for i in g.dictionary:
        print "---"
        print "from " + str(i)
        for e in g.lookup_node(i).links:
            print "to " + str(e.edge_end)
            print e.properties["weight"]
            print "--"
    """
    # print estimate_trust(30, 9805, g)

    """
    for i in g.dictionary:
        for j in g.dictionary:
            x = estimate_trust(i, j, g)
            if x > 0:
                print "----"
                print i
                print j
                print x
        print i
    """

    # print number_of_connected_components(pkp_graph)
    # print diameter(pkp_graph)
    # print average_path_length(pkp_graph)
    # print max_connected_component(pkp_graph)
    # print closeness_centrality(pkp_graph, 38)
    # CB = betweenness_centrality(pkp_graph)
    # for x in CB:
        # print "node " + str(x)
        # print CB[x]

    """
    graph = Graph()
    node = Node(1, [], [])
    graph.insert_node(node)
    node = Node(2, [], [])
    graph.insert_node(node)
    node = Node(3, [], [])
    graph.insert_node(node)
    node = Node(4, [], [])
    graph.insert_node(node)
    node = Node(5, [], [])
    graph.insert_node(node)
    edge = Edge(2, [])
    graph.insert_edge(1, edge)
    edge = Edge(3, [])
    graph.insert_edge(2, edge)
    edge = Edge(4, [])
    graph.insert_edge(2, edge)
    edge = Edge(5, [])
    graph.insert_edge(4, edge)

    dick = betweenness_centrality(graph)
    for node_id in dick:
        print "------"
        print node_id
        print dick[node_id]
    """



def fun():
    print "hahaha"

if __name__ == '__main__': main()
