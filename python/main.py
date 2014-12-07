__author__ = 'Jason'

from FileOperations import *
from GraphStatistics import *


def main():
    print "hello world"
    pkp_graph = create_graph_from_file("person_knows_person.csv")
    # populate_person_graph(pkp_graph, "person.csv")

    # print number_of_connected_components(pkp_graph)
    # print diameter(pkp_graph)
    # print average_path_length(pkp_graph)
    # print max_connected_component(pkp_graph)
    print closeness_centrality(pkp_graph, 38)


def fun():
    print "hahaha"

if __name__ == '__main__': main()
