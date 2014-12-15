__author__ = 'Jason'

from FileOperations import *
from GraphStatistics import *
from  GraphQueries import *


def main():
    print "hello world"
    pkp_graph = create_graph_from_file("person_knows_person.csv")
    populate_person_graph(pkp_graph, "person.csv", "person_hasInterest_tag.csv")

    # print pkp_graph.lookup_node(37).interests

    tmp = match_suggestion(pkp_graph, 23, 1, 1000, 100, 50)
    for aaa in tmp:
        print aaa

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
