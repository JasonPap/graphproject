__author__ = 'Jason'

from GraphQueries import *
from forums import *
from Clique_Percolation_Method import *
from multiprocessing import Pool
import multiprocessing
from Girvan_Newman import *


def main():

    proc_pool = Pool(processes=multiprocessing.cpu_count())

    pkp_graph = create_graph_from_file("person_knows_person.csv")
    populate_person_graph(pkp_graph, "person.csv", "person_hasInterest_tag.csv")

    r = find_top_n_forums(6)
    list_of_comm_graphs = create_forums_graphs(r, pkp_graph, proc_pool)
    print "CPM:"
    for community_graph in list_of_comm_graphs:
        print percolation_method(community_graph, 3, proc_pool)

    print "GM:"
    for community_graph in list_of_comm_graphs:
        cl = girvan_newman(community_graph, 1)
        print cl

    return 0


if __name__ == '__main__': main()
