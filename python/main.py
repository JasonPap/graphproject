__author__ = 'Jason'

from GraphQueries import *
from forums import *
from Clique_Percolation_Method import *
from multiprocessing import Pool
import multiprocessing


def main():

    proc_pool = Pool(processes=multiprocessing.cpu_count())

    pkp_graph = create_graph_from_file("person_knows_person.csv")
    populate_person_graph(pkp_graph, "person.csv", "person_hasInterest_tag.csv")

    fucking_dick = edge_betweeness_centrality(pkp_graph)
    print fucking_dick[(25, 9805)]
    print fucking_dick[(9805, 25)]

    return

    r = find_top_n_forums(6)
    list_of_comm_graphs = create_forums_graphs(r, pkp_graph, proc_pool)
    for community_graph in list_of_comm_graphs:
        cl = percolation_method(community_graph, 3, proc_pool)
        print cl

    return 0

    print "graph diameter = " + str(diameter(pkp_graph))
    print "average path length = " + str(average_path_length(pkp_graph))
    print "number of CC = " + str(number_of_connected_components(pkp_graph))
    print "size of max CC = " + str(max_connected_component(pkp_graph))
    print "density = " + str(density(pkp_graph))

    # closeness centrality
    print "closeness centrality of nodes 1734, 38, 8899, 3501 and 75:"
    print closeness_centrality(pkp_graph, 1734)
    print closeness_centrality(pkp_graph, 38)
    print closeness_centrality(pkp_graph, 8899)
    print closeness_centrality(pkp_graph, 3501)
    print closeness_centrality(pkp_graph, 75)

    # betweenness centrality
    print "betweenness centrality of nodes 1734, 38, 8899, 9900 and 75:"
    results = betweenness_centrality(pkp_graph)
    print results[1734]
    print results[38]
    print results[8899]
    print results[9900]
    print results[75]

    # query one
    print match_suggestion(pkp_graph, 3755, 1, 3, 30, 1)

    # query two
    stalkers = []
    stalkers_graph = get_top_stalkers(pkp_graph, 7, 1, 1, stalkers)
    print "scored stalkers:"
    print stalkers

    # query three
    men_trends = []
    women_trends = []
    find_trends(4, pkp_graph, women_trends, men_trends)
    print "men trends:"
    print men_trends
    print "women trends:"
    print women_trends

    # query four
    trust_graph = build_trust_graph("Wall of Xiomara Fernandez", pkp_graph)
    print "trust 30 -> 9805:"
    print estimate_trust(30, 9805, trust_graph)
    print "trust 30 -> 9700:"
    print estimate_trust(30, 9700, trust_graph)

    return


def fun():
    print "hahaha"

if __name__ == '__main__': main()
